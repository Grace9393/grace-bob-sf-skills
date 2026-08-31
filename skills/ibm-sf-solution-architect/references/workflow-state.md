# Workflow State File Contract

Use `../tmp/ibm-sf-solution/state.json` during generation.

Required shape:
```json
{
  "mode": "sectional",
  "current_section": "02-input-user-stories",
  "completed_sections": [],
  "pending_sections": [],
  "changed_requirements": [],
  "dependencies_satisfied": {},
  "last_updated": "ISO-8601"
}
```

Also maintain:
- `../tmp/ibm-sf-solution/section-memory.md`
- `../tmp/ibm-sf-solution/sections/NN-<section-name>.md`
- `../tmp/ibm-sf-solution/complete_solution.md`
