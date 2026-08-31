# Salesforce Help FTS5 Query Reference

Use this reference for `$SKILL_DIR/docs.sqlite`.

## Database profile

- DB path: `$SKILL_DIR/docs.sqlite`
- FTS table: `entries_fts`
- Tokenizer: `porter unicode61`
- Columns:
  - `app_area` (0)
  - `dc_identifier` (1)
  - `product` (2)
  - `product_release_name` (3)
  - `title` (4)
  - `url` (5, UNINDEXED)
  - `contents` (6)

## Runtime and preflight (run first)

```bash
DB_PATH="$SKILL_DIR/docs.sqlite"
uv run $SKILL_DIR/scripts/info.py "$DB_PATH"
```

Search options (sqlite-skill):
- `--offset <n>` pagination
- `--show-status` or `--json-pretty` for query status/warnings
- `--show-scores` or `--min-score <0-1>` for normalized scores
- `--snippet`, `--snippet-length <n>`, `--snippet-column <col>`
- `--query-timeout-ms <ms>`

Get options:
- `--preview-length <n>` (>= 1)

Exit codes:
- `2` database path errors
- `3` invalid/empty query or timeout (also invalid preview length)
- `4` no results / not found

- Use Python runtime scripts for all database access in this skill.
- Do not use direct `sqlite3` shell/HEREDOC patterns here.

## MATCH and NEAR quick rules

- Phrase search: `'"exact phrase"'`
- Boolean logic: `AND`, `OR`, `NOT` (space-separated terms are implicit `AND`)
- Prefix search: `autom*`
- Column-scoped search: `product:"Sales Cloud"` or `app_area:Einstein`
- Multi-column scope: `'{title contents app_area}:governance'`
- Proximity: `NEAR(term1 term2, 5)` (FTS5 does not support `NEAR/1 5` range syntax)

## Ranking quick rules

- Default runtime search returns BM25 ranked matches; keep query structure consistent when comparing runs.

## Constraints and caveats

- Tighten results first and then expand
- Use `MATCH` for full-text conditions (not `LIKE`/`=` for relevance search).
- Build MATCH expressions as constants or bound parameters.
- Applying many non-FTS filters can reduce FTS performance.
- Very long single terms can fail (SQLite FTS term length limits apply).

## Notes

- In this dataset, snippets should use column `6` (`contents`).
- `url` is for output/citation; do not use it inside MATCH.
