# Database Creation

This directory contains the scripts to create and populate the Salesforce Help Center SQLite database.

## Prerequisites

- Python 3.13+
- Required packages: `beautifulsoup4`, `lxml`

```bash
pip install beautifulsoup4 lxml
```

## Files

| File | Description |
|------|-------------|
| `db.sql` | Database schema (FTS5 table for full-text search) |
| `create_db.py` | Python script to populate database from XML sitemap |
| `../docs.sqlite` | Generated SQLite database (not in repo - see `.gitignore`) |

## Database Schema

The database contains a single FTS5 (full-text search) table:

```sql
CREATE VIRTUAL TABLE help_articles_fts USING fts5(
    url,
    title,
    content,
    app_areas,
    products
);
```

## Recreating the Database

The database is **not stored in the repository** (excluded via `.gitignore`). To recreate it:

### Step 1: Create the schema

From the `src/` directory:

```bash
cd skills/ibm-sf-help/src
sqlite3 ../docs.sqlite < db.sql
```

Or if starting fresh (removes existing database):

```bash
cd skills/ibm-sf-help/src
rm -f ../docs.sqlite
sqlite3 ../docs.sqlite < db.sql
```

### Step 2: Populate from Salesforce Help Center

Run the creation script:

```bash
cd skills/ibm-sf-help/src
python3 create_db.py
```

This will:
1. Fetch the Salesforce Help Center XML sitemap from `https://help.salesforce.com/sitemap.xml`
2. Parse all article URLs from the sitemap
3. Fetch each article's HTML content
4. Extract title, content, app areas, and products from each page
5. Insert all entries into the FTS5 database for fast full-text search

**Note:** This process may take several minutes as it fetches hundreds of articles from the Salesforce Help Center.

### Step 3: Verify

```bash
sqlite3 -readonly ../docs.sqlite \"SELECT COUNT(*) FROM help_articles_fts;\"
sqlite3 -readonly ../docs.sqlite \"SELECT title FROM help_articles_fts LIMIT 5;\"
```

## Database Contents

Each row in the database represents a Salesforce Help Center article with:

| Column | Description |
|--------|-------------|
| `url` | Full URL to the help article |
| `title` | Article title |
| `content` | Full article text content |
| `app_areas` | Comma-separated list of applicable app areas |
| `products` | Comma-separated list of applicable products |

## Usage

Once created, the database is used by the search scripts in `../scripts/` to perform fast full-text searches across all Salesforce Help Center content.
