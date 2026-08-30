# Database Creation

This directory contains the scripts to create and populate the Salesforce architecture reference SQLite database.

## Prerequisites

- Python 3.13+

```bash
pip install beautifulsoup4 lxml
```

## Files

| File | Description |
|------|-------------|
| `db.sql` | Database schema (FTS5 table for full-text search) |
| `create_db.py` | Python script to populate database from local Markdown docs |
| `../architect.sqlite` | Generated SQLite database (not in repo - see `.gitignore`) |

## Database Schema

The database contains a single FTS5 (full-text search) table:

```sql
CREATE VIRTUAL TABLE entries_fts
USING fts5(
  title,
  url UNINDEXED,
  contents,
  images_text,
  images UNINDEXED,
  tokenize='porter unicode61'
);
```

## Recreating the Database

The database is **not stored in the repository** (excluded via `.gitignore`). To recreate it:

### Step 1: Create the schema

From the `src/` directory:

```bash
cd skills/ibm-sf-architect/src
sqlite3 ../architect.sqlite < db.sql
```

Or if starting fresh (removes existing database):

```bash
cd skills/ibm-sf-architect/src
rm -f ../architect.sqlite
sqlite3 ../architect.sqlite < db.sql
```

### Step 2: Populate from local docs

Run the creation script:

```bash
cd skills/ibm-sf-architect/src
python3 create_db.py
```

This will:
1. Read Markdown documents from `../docs`
2. Parse front matter for `title` and `url`
3. Extract content and image references
4. (Optional) Generate image descriptions with an OpenAI-compatible vision model
5. Store image descriptions in `images_text` (searchable) and JSON metadata in `images`
6. Insert all entries into the FTS5 database for fast full-text search

**Note:** Image description generation can take several minutes if enabled.

### Step 3: Verify

```bash
sqlite3 -readonly ../architect.sqlite \"SELECT COUNT(*) FROM entries_fts;\"
sqlite3 -readonly ../architect.sqlite \"SELECT title FROM entries_fts LIMIT 5;\"
```

## Database Contents

Each row in the database represents a Salesforce Help Center article with:

| Column | Description |
|--------|-------------|
| `title` | Document title (front matter) |
| `url` | Optional source URL (front matter) |
| `contents` | Full document text content |
| `images_text` | Newline-joined image descriptions (searchable) |
| `images` | JSON list of image paths/alt text/LLM descriptions (unindexed) |

## LLM Configuration

By default, `create_db.py` uses LM Studio with the `qwen3-vl-4b-instruct-mlx` model.

Examples:

```bash
# Default (LM Studio)
python3 create_db.py

# Use Ollama instead
python3 create_db.py --provider ollama

# Custom base URL/model
python3 create_db.py --provider custom --base-url http://localhost:11434/v1 --model qwen3-vl:8b
```

Optional environment overrides:

```bash
export LMSTUDIO_BASE_URL=http://localhost:1234/v1
export LMSTUDIO_MODEL=qwen3-vl-4b-instruct-mlx
export OLLAMA_BASE_URL=http://localhost:11434/v1
export OLLAMA_MODEL=qwen3-vl:8b
```

To skip image descriptions:

```bash
python3 create_db.py --disable-descriptions
```

## Usage

Once created, the database is used by the search scripts in `../scripts/` to perform fast full-text searches across all Salesforce Help Center content.
