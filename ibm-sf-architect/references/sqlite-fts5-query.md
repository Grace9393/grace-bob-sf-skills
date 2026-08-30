# Salesforce Architect FTS5 Query Reference

Use this reference for `$SKILL_DIR/architect.sqlite`.

## Database profile

- DB path: `$SKILL_DIR/architect.sqlite`
- FTS table: `entries_fts`
- Tokenizer: `porter unicode61`
- Columns:
  - `title` (0)
  - `url` (1, UNINDEXED)
  - `contents` (2)
  - `images_text` (3)
  - `images` (4, UNINDEXED)

## Runtime and preflight (run first)

```bash
DB_PATH="$SKILL_DIR/architect.sqlite"
uv run $SKILL_DIR/scripts/info.py "$DB_PATH"
```

Search options (sqlite-skill) - tighten results first:
- `--offset <n>` pagination
- `--show-status` or `--json-pretty` for query status/warnings
- `--show-scores` or `--min-score <0-1>` for normalized scores
- `--snippet`, `--snippet-length <n>`, `--snippet-column <col>`
- `--query-timeout-ms <ms>`
- `--limit 10`

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
- Prefix search: `integrat*`
- Column-scoped search: `title:"reference architecture"`
- Multi-column scope: `'{title contents images_text}:security'`
- Proximity: `NEAR(term1 term2, 5)` (FTS5 does not support `NEAR/1 5` range syntax)

## Ranking quick rules

- Default runtime search returns BM25 ranked matches; keep query structure consistent when comparing runs.

## Constraints and caveats

- Use `MATCH` for full-text conditions (not `LIKE`/`=` for relevance search).
- Build MATCH expressions as constants or bound parameters.
- Applying many non-FTS filters can reduce FTS performance.
- Very long single terms can fail (SQLite FTS term length limits apply).

## Notes

- In this dataset, snippets should use column `2` (`contents`).
- `url` and `images` are for citation/rendering and should not be used inside MATCH.
