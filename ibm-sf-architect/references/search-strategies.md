# Search Strategies

Advanced search patterns for `ibm-sf-architect` using Python runtime scripts only.

## Runtime-first approach

```bash
DB_PATH="$SKILL_DIR/architect.sqlite"
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

1. **Architecture pass** - pattern, reference architecture, integration pattern terms.
2. **Constraint pass** - security, scale, latency, data residency, governance.
3. **Artifact pass** - diagram/image/blueprint terms for visual support.

Merge and deduplicate IDs before retrieval.

## Strategy patterns

```bash
# Integration and platform architecture
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(integration OR api-led OR event-driven) AND (architecture OR pattern)" --json
```

```bash
# Security-oriented architecture
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(security OR auth OR identity) AND (model OR architecture OR control*)" --json
```

```bash
# Diagram-heavy results
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(reference architecture OR topology) AND (diagram OR image OR visual)" --json
```

## Result triage rubric

Review top 10-15 and prioritize:

- **Pattern fit (0-3)**: direct relevance to requested architecture pattern.
- **Constraint fit (0-3)**: addresses key constraints (security/scale/integration).
- **Implementation depth (0-2)**: concrete design guidance.
- **Visual support (0-2)**: useful image/diagram metadata present.

Prioritize entries scoring 7+.

## Failure recovery playbook

If fewer than 5 strong hits:

1. Replace architecture jargon with simpler alternatives (for example `event-driven` -> `events`).
2. Split query into separate capability and constraint queries.
3. Add deployment context terms (enterprise, multicloud, governance).
4. Run one query optimized for visuals (`diagram`, `reference architecture`).
5. Escalate to `$query-expansion-strategy`.

## Anti-patterns

- **Too broad**: `salesforce architecture`.
- **Too narrow**: heavily quoted multi-phrase query.
- **Ignoring visuals**: no image/diagram pass when user needs diagrams.
- **Single pass**: one query and immediate retrieval.

## JSON post-filter examples

```bash
# Entries with image payloads
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(integration OR security) AND architecture" --json \
  | jq 'map(select(.images != null and .images != ""))'
```

```bash
# Prioritize entries with image text hints
uv run $SKILL_DIR/scripts/search.py "$DB_PATH" \
  "(reference OR blueprint) AND (scale OR resilience)" --json \
  | jq 'map(select((.images_text // "") != "")) | .[:10]'
```
