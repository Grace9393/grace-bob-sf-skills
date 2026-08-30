---
name: ibm-sf-architect
description: This collection provides comprehensive Salesforce architecture guidance from the official Salesforce Architects documentation (architect.salesforce.com), covering essential knowledge for enterprise architects designing and implementing Salesforce solutions. Use when users ask about Salesforce architecture patterns, design best practices, technical architecture, solution design, integration patterns, data modeling, security architecture, or need architectural diagrams and visual documentation. Includes images and diagrams.
---

## PREREQUISITES - MANDATORY

Use the cross-platform Python runtime scripts from `$SKILL_DIR/scripts/` for all database access.

Do not use shell HEREDOC SQL patterns in this skill (they are not reliable on Windows).

## Context Management

ALWAYS write search results to `./tmp/ibm-sf-architect.md` immediately after retrieval. This prevents context saturation when chaining with other skills. Only copy final deliverables to `./outputs` at completion.

## Quick Reference

| Item               | Value                                      |
| ------------------ | ------------------------------------------ |
| Database           | `$SKILL_DIR/architect.sqlite` |
| FTS5 Table         | `entries_fts`                              |
| Source             | architect.salesforce.com                   |
| Content Types      | Architecture patterns, design guides, best practices, diagrams |
| Image Location     | Relative paths from database directory     |

## Overview

Salesforce architecture guidance from architect.salesforce.com is stored in SQLite with FTS5 full-text search, including architecture diagrams and visual documentation metadata.

## Search Workflow

### Step 1: Expand Query Terms (Default)

1. Generate synonym variants (5-7 alternatives per concept)
2. Add phrasal alternatives users actually type
3. Build OR-joined FTS query strings

Example:

```bash
# Original: "integration patterns security"
# Expanded: "(integration OR API OR connectivity) AND (patterns OR architecture OR design) AND (security OR secure OR auth*)"
```

### Step 2: Execute Search

Use only the Python scripts in `$SKILL_DIR/scripts/`:

- `info.py` (schema/metadata checks)
- `search.py` (FTS search)
- `get.py` (retrieve full record by ID)

```bash
DB_PATH="$SKILL_DIR/architect.sqlite"

# Confirm schema/table availability
uv run $SKILL_DIR/scripts/info.py "$DB_PATH"

# Expanded keyword search
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(integration OR API OR connectivity) AND (patterns OR architecture OR design)" --json

# Multi-concept expansion
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(data OR object OR entity) AND (model OR architecture OR schema) AND (security OR access OR permission*)" --json

# Image-heavy architecture content
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "integration patterns diagram" --json

# Retrieve full document by rowid/id from search output
uv run $SKILL_DIR/scripts/get.py "$DB_PATH" 12345 --json
```

Search options (sqlite-skill) - tighten results first:
- `--offset <n>` pagination
- `--show-status` or `--json-pretty` for query status/warnings
- `--show-scores` or `--min-score <0-1>` for normalized scores
- `--snippet`, `--snippet-length <n>`, `--snippet-column <col>`
- `--query-timeout-ms <ms>`
- `--limit 10`


### Step 3: Evaluate Results & Escalate if Needed

If results are poor (<5 relevant hits), use `$query-expansion-strategy` for wider coverage.

If results are good (5+ relevant hits):
- Review top 10-15
- Check associated image metadata where available
- Retrieve full content for shortlisted IDs only

### Step 4: Retrieve Entry by ID

Use `get.py` from `$SKILL_DIR/scripts/`:

```bash
DB_PATH="$SKILL_DIR/architect.sqlite"

# Get complete story by ID
uv run $SKILL_DIR/scripts/get.py "$DB_PATH" 42

# JSON output for structured processing
uv run $SKILL_DIR/scripts/get.py "$DB_PATH" 42 --json
```

Get options:
- `--preview-length <n>` (>= 1)

Exit codes:
- `2` database path errors
- `3` invalid/empty query or timeout (also invalid preview length)
- `4` no results / not found

## Working with Images

Search and get results may include image metadata when diagrams/screenshots are present.

When an image path is returned, construct the full file path as:
- `$SKILL_DIR/{image_path}`

When presenting architecture guidance:
- Mention when diagrams/images are available
- Use images to support architecture explanations
- Include source URL and document ID for traceability

## Database Schema

**FTS5 Table: `entries_fts`**

- `rowid`: Entry ID (implicit primary key)
- `title`: Document title
- `url`: Source URL
- `contents`: Full document text content
- `images`: JSON array with `path`, `alt`, and `description`

## Reference Files

- [references/sqlite-fts5-query.md](references/sqlite-fts5-query.md) - FTS5 syntax and dataset-specific query notes
- [references/search-strategies.md](references/search-strategies.md) - retrieval coverage loop, triage rubric, and post-filter patterns

## Important Notes

- **Always use Python runtime scripts** - Use `uv run $SKILL_DIR/scripts/search.py` and `get.py` for all searches/retrieval
- **Images provide critical context** - Architecture documents often include diagrams
- **Cross-reference** - Combine with `ibm-sf-help` and `ibm-sf-solution-architect` for end-to-end design responses
