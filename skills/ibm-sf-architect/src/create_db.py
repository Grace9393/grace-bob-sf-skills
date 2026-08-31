#!/usr/bin/env python3
import base64
import argparse
import json
import logging
import os
import re
import sqlite3
from pathlib import Path
from urllib import request

# Import VLM processing utilities from common module
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.vlm_processor import (
    apply_provider_defaults,
    create_vlm_arg_parser,
    create_vlm_client,
    describe_image,
)

DB = "../architect.sqlite"
DOCS_DIR = Path("../docs")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

META_KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):[ \t]*(.*)$")
FRONT_MATTER_MARK = "---"
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^\)]+)\)")


def parse_front_matter(text: str) -> tuple[dict, str]:
    """Parse top-of-file front matter, ignoring later '---' blocks."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONT_MATTER_MARK:
        return {}, text

    meta: dict[str, str] = {}
    contents_start = 0
    for idx in range(1, len(lines)):
        line = lines[idx]
        if line.strip() == FRONT_MATTER_MARK:
            contents_start = idx + 1
            break
        match = META_KEY_RE.match(line)
        if match:
            key, value = match.groups()
            meta[key] = value
    else:
        return meta, ""

    contents = "\n".join(lines[contents_start:])
    return meta, contents


def extract_image_paths(
    client,
    model: str,
    backup_client,
    backup_model: str | None,
    allow_ollama_fallback: bool,
    describe_images_flag: bool,
    markdown_text: str,
    base_path: Path,
    db_path: Path,
) -> list[dict]:
    """Extract images and enrich with alt text and LLM descriptions."""
    images = []
    db_dir = db_path.parent.resolve()

    for match in IMAGE_RE.finditer(markdown_text):
        alt_text, img_path = match.groups()
        # Skip URLs
        if img_path.startswith(('http://', 'https://')):
            logger.info("Skipping remote image %s", img_path)
            images.append({
                "path": img_path,
                "alt": alt_text or None,
                "description": None,
            })
        else:
            # Resolve image path relative to markdown file
            abs_img_path = (base_path.parent / img_path).resolve()
            # Convert to relative path from database location
            try:
                rel_path = abs_img_path.relative_to(db_dir)
                rel_path_str = str(rel_path)
            except ValueError:
                # If paths are on different drives or can't be made relative, use absolute
                rel_path_str = str(abs_img_path)
            description = None
            if describe_images_flag:
                try:
                    description = describe_image(
                        client,
                        model,
                        abs_img_path,
                        "Describe this Salesforce architecture diagram in 1–2 sentences.",
                        allow_ollama_fallback,
                    )
                except Exception:
                    if not backup_client or not backup_model:
                        raise
                    logger.warning("Primary model failed; retrying with backup for %s", abs_img_path)
                    description = describe_image(
                        backup_client,
                        backup_model,
                        abs_img_path,
                        "Describe this Salesforce architecture diagram in 1–2 sentences.",
                        allow_ollama_fallback,
                    )
            images.append({
                "path": rel_path_str,
                "alt": alt_text or None,
                "description": description or None,
            })
    return images


def build_images_text(images: list[dict]) -> str | None:
    descriptions = []
    for image in images:
        description = image.get("description")
        if description:
            descriptions.append(description)
    if not descriptions:
        return None
    return "\n".join(descriptions)


def parse_args() -> argparse.Namespace:
    parser = create_vlm_arg_parser("Build architect.sqlite with image descriptions.")
    args = parser.parse_args()
    apply_provider_defaults(args)
    return args


conn = sqlite3.connect(DB)
conn.execute("PRAGMA journal_mode=WAL;")

insert_row = """
INSERT INTO entries_fts (
  title,
  url,
  contents,
  images_text,
  images,
  vlm_model
) VALUES (?, ?, ?, ?, ?, ?);
"""

inserted = 0
db_path = Path(DB).resolve()
args = parse_args()
allow_ollama_fallback = args.provider == "ollama"
primary_client = create_vlm_client(args.base_url, "lmstudio")
backup_client = None
if args.backup_base_url and args.backup_model:
    backup_client = create_vlm_client(args.backup_base_url, "lmstudio")

for path in sorted(DOCS_DIR.rglob("*.md")):
    text = path.read_text(encoding="utf-8", errors="replace")
    meta, contents = parse_front_matter(text)
    images = extract_image_paths(
        primary_client,
        args.model,
        backup_client,
        args.backup_model,
        allow_ollama_fallback,
        not args.disable_descriptions,
        text,
        path,
        db_path,
    )
    images_json = json.dumps(images) if images else None
    images_text = build_images_text(images)
    conn.execute(insert_row, (
        meta.get("title"),
        meta.get("url"),
        contents,
        images_text,
        images_json,
        args.model,
    ))
    inserted += 1
    if inserted % 1000 == 0:
        print(f"Processed {inserted} files...")

conn.commit()
conn.close()

print("Database updated successfully!")
print(f"Entries inserted: {inserted}")
