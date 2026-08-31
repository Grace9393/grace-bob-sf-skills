---
name: ibm-sf-help
description: Search Salesforce Help Center documentation using FTS5 full-text search. Use when users ask about Salesforce features, configuration, administration, Einstein AI, Sales Cloud, Service Cloud, Experience Cloud, Marketing Cloud, or any Salesforce product documentation. Supports filtering by product, app area, and release version.
---

# IBM Salesforce Help

## PREREQUISITES - MANDATORY

Use the cross-platform Python runtime scripts from `$SKILL_DIR/scripts/` for all database access.

Do not use shell HEREDOC SQL patterns in this skill (they are not reliable on Windows).

## Context Management

ALWAYS write search results to `./tmp/ibm-sf-help.md` immediately after retrieval. This prevents context saturation when chaining with other skills. Only copy final deliverables to `./outputs` at completion.

## Quick Reference

| Item               | Value                        |
| ------------------ | ---------------------------- |
| Database           | `$SKILL_DIR/docs.sqlite` |
| FTS5 Table         | `entries_fts`                |
| Primary Products   | Sales Cloud, Service Cloud, Experience Cloud, Marketing Cloud, Commerce Cloud, and more |
| Release Versions   | Multiple (Winter, Spring, Summer releases) |

## Overview

Salesforce Help Center documentation stored in a SQLite database (`docs.sqlite`) with full-text search (FTS5). All documentation content (titles, descriptions, product metadata) is stored in the database for fast, efficient searching.

## Search Workflow

### Step 1: Expand Query Terms (Default)

**Apply simplified query expansion before searching to improve recall:**

1. **Generate synonym variants** (5-7 alternatives for each core concept):
   - "lead scoring" → add "prospect evaluation", "lead ranking", "contact qualification"
   - "cloud migration" → add "cloud transformation", "cloud adoption", "cloud modernization"
   - "customer portal" → add "self-service portal", "client portal", "customer hub"

2. **Add phrasal alternatives** (rephrase using common variations):
   - "how to implement X" → also search "X implementation", "deploying X", "X rollout"
   - "benefits of X" → also search "X advantages", "X outcomes", "X results"
   - Technical terms → add colloquial equivalents users actually type

3. **Construct OR-joined FTS5 query** (combine variants for better recall):
   ```bash
   # Original query: "lead scoring healthcare"
   # Expanded query: "(lead OR prospect OR contact) AND (scoring OR ranking OR evaluation OR qualification) AND (healthcare OR medical OR clinical OR hospital)"
   ```

**This 3-step expansion takes ~10 seconds and significantly improves search results.**

### Step 2: Execute Search

Use only the Python scripts in `$SKILL_DIR/scripts/`.

- `info.py` (schema/metadata checks)
- `search.py` (FTS search)
- `get.py` (retrieve full record by ID)

```bash
DB_PATH="$SKILL_DIR/docs.sqlite"

# Confirm schema/table availability
uv run $SKILL_DIR/scripts/info.py "$DB_PATH"

# Expanded keyword search
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(data OR object OR entity) AND (model OR schema OR structure)" --json

# Product-specific query
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(workflow OR flow OR process) AND (automation OR builder OR automated) AND \"Sales Cloud\"" --json

# Release-focused query
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "API AND (\"Winter '25\" OR \"Spring '25\")" --json

# App area-focused query
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "Einstein AND Sales_Cloud_Einstein" --json

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
- Filter by product/app area/release terms
- Review top 10-15
- Retrieve full content for shortlisted IDs only

### Step 4: Retrieve Entry by ID

Use `get.py` from `$SKILL_DIR/scripts/`:

```bash
DB_PATH="$SKILL_DIR/docs.sqlite"

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

## App Area Filtering

The `app_area` field is semicolon-delimited (for example: `Einstein;Sales_Cloud_Einstein`).

Use combined terms in the search query to target specific app areas.

See `references/app-areas.md` for the complete app area list and filtering patterns.

## Reference Files

- [references/sqlite-fts5-query.md](references/sqlite-fts5-query.md) - FTS5 syntax and dataset-specific query notes
- [references/search-strategies.md](references/search-strategies.md) - retrieval coverage loop, triage rubric, and post-filter patterns

## Workflow

1. **Search**: Query by keyword, product, or app area using `search.py`
2. **Retrieve**: Use `get.py` for full document content
3. **Present**: Include ID, title, product, and URL for citations

## Integration with Other Skills

1. `ibm-sf-help` - Search Salesforce documentation (this skill)
2. `ibm-sf-solution-architect` - Apply documentation to solution design
3. `ibm-bid-strategy-and-capabilities-2026` - Align with IBM Salesforce capabilities
4. `ibm-bid-customer-stories` - Find proof points for similar implementations
5. `ibm-bid-writer` - Draft technical responses

## Quality Checklist

When presenting Salesforce documentation, ensure you:
- ✓ Used `$SKILL_DIR/scripts/search.py` and `get.py` for all database access
- ✓ Selected documentation that genuinely matches the user's criteria
- ✓ Avoided duplicate entries
- ✓ Included document ID, title, and product context
- ✓ Provided source URL for verification when available
- ✓ Checked product release version for currency
- ✓ Explained relevance to the user's specific needs
- ✓ Used British English spelling and professional tone
- ✓ Avoided fabricating or embellishing details beyond what's in the database

## Important Notes

- **Always use Python runtime scripts** - Use `uv run $SKILL_DIR/scripts/search.py` and `get.py` for all searches/retrieval
- **App areas are semicolon-delimited** - Use combined query terms to target multiple app areas
- **Check release version** - Ensure documentation matches the Salesforce version being implemented
- **Cross-reference** - Combine with other skills for comprehensive responses
