import re
import sqlite3
import time
from contextlib import suppress
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "docs.sqlite"
# DOCS_DIR = Path("/Users/telcott/tmp-nosync/Salesforce_help.salesforce.com_20251214/test")
DOCS_DIR = Path("/Users/telcott/tmp-nosync/Salesforce_help.salesforce.com_20251214/output")

META_KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):[ \t]*(.*)$")
FRONT_MATTER_MARK = "---"


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

def execute_with_retry(conn: sqlite3.Connection, query: str, params: tuple, retries: int = 5) -> None:
    for attempt in range(1, retries + 1):
        try:
            conn.execute(query, params)
            return
        except sqlite3.OperationalError as exc:
            message = str(exc).lower()
            transient = "disk i/o error" in message or "database is locked" in message
            if not transient or attempt == retries:
                raise
            with suppress(sqlite3.Error):
                conn.rollback()
            time.sleep(0.25 * attempt)


conn = sqlite3.connect(DB, timeout=60)
conn.execute("PRAGMA journal_mode=DELETE;")
conn.execute("PRAGMA synchronous=NORMAL;")
conn.execute("PRAGMA temp_store=MEMORY;")
conn.execute("PRAGMA busy_timeout=60000;")

insert_row = """
INSERT INTO entries_fts (
  app_area,
  dc_identifier,
  product,
  product_release_name,
  title,
  url,
  contents
) VALUES (?, ?, ?, ?, ?, ?, ?);
"""

inserted = 0
conn.execute("BEGIN")
for path in sorted(DOCS_DIR.rglob("*.txt")):
    text = path.read_text(encoding="utf-8", errors="replace")
    meta, contents = parse_front_matter(text)
    execute_with_retry(conn, insert_row, (
        meta.get("app_area"),
        meta.get("dc_identifier"),
        meta.get("product"),
        meta.get("product_release_name"),
        meta.get("title"),
        meta.get("url"),
        contents,
    ))
    inserted += 1
    if inserted % 1000 == 0:
        conn.commit()
        conn.execute("BEGIN")
        print(f"Processed {inserted} files...")

conn.commit()
conn.close()

print("Database updated successfully!")
print(f"Entries inserted: {inserted}")
