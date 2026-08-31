# Search Strategies

Advanced search patterns for `ibm-sf-help` using Python runtime scripts only.

## Runtime-first approach

```bash
DB_PATH="$SKILL_DIR/docs.sqlite"
uv run $SKILL_DIR/scripts/info.py "$DB_PATH"
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" "<fts_query>" --json
uv run $SKILL_DIR/scripts/get.py "$DB_PATH" <id> --json
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

Do not use direct `sqlite3` or HEREDOC SQL in this skill.

## Coverage loop (default)

Run these passes in order:

1. **Capability pass** - feature/service terms (Flow, API, Einstein, setup).
2. **Metadata pass** - product/app area/release terms.
3. **Outcome pass** - admin/user goal terms (automation, permissions, deployment).

Merge and deduplicate IDs before retrieval.

## Strategy patterns

```bash
# Product + capability
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "product:\"Sales Cloud\" AND (flow OR automation OR process)" --json
```

```bash
# App area targeting
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "app_area:(Einstein OR Sales_Cloud_Einstein) AND (model OR prompt OR prediction)" --json
```

```bash
# Release-scoped triage
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(API OR integration) AND (\"Winter '26\" OR \"Spring '26\")" --json
```

## Result triage rubric

Review top 10-15 and prioritize:

- **Capability fit (0-3)**: directly answers the requested Salesforce capability.
- **Product/app-area fit (0-3)**: correct cloud and app area.
- **Release relevance (0-2)**: current version fit.
- **Implementation utility (0-2)**: actionable setup/config details.

Prioritize entries scoring 7+.

## Failure recovery playbook

If fewer than 5 strong hits:

1. Replace product name with cloud synonyms (`Sales Cloud` -> `sales`, `crm`).
2. Remove one restrictive phrase from the query.
3. Split into two queries: one for feature, one for setup/troubleshooting.
4. Add app-area terms from `references/app-areas.md`.
5. Escalate to `$query-expansion-strategy`.

## Anti-patterns

- **Too broad**: `Salesforce AND setup`.
- **Too narrow**: multiple quoted phrases plus product plus release in one query.
- **Missing metadata terms**: no product/app_area terms when user asks cloud-specific guidance.
- **Single query only**: skip of coverage loop.

## JSON post-filter examples

```bash
# Keep entries with Einstein-related app areas
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(agent OR model OR prompt) AND (setup OR configure)" --json \
  | jq 'map(select((.app_area // "") | test("Einstein"; "i")))'
```

```bash
# Prefer entries tied to a product release string
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(api OR integration) AND (security OR auth)" --json \
  | jq 'map(select((.product_release_name // "") != "")) | .[:10]'
```
