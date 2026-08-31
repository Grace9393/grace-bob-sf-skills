---
name: ibm-sf-solution-architect
description: Generate comprehensive Salesforce solution architecture documents from user stories and requirements. Use when asked to create solution design documents, architecture documentation, or technical specifications for Salesforce implementations. Supports incremental updates where user stories change and the solution document needs revision. Integrate with $ibm-sf-help and $ibm-sf-architect skills for Salesforce best practices.
metadata:
  skills-suggested:
    - ibm-sf-help
    - ibm-sf-architect
---

# Salesforce Solution Architecture Document Generator

Generate a production-quality Salesforce architecture document using a strict one-section-at-a-time workflow.

## Context Management

Use these paths:
- State: `./tmp/ibm-sf-solution/state.json`
- Section outputs: `./tmp/ibm-sf-solution/sections/`
- Memory summary: `./tmp/ibm-sf-solution/section-memory.md`
- Final assembled doc: `./tmp/ibm-sf-solution/complete_solution.md`

Persist after every section. Copy final artifact to `./outputs` only when complete.

## Required Generation Mode

Always run in **sectional mode**. Do not draft all sections in a single response.

## Skill Integration (Mandatory)

Before generating Salesforce design-heavy sections (05, 06, 08, 09, 12):
- Use `ibm-sf-architect` for pattern validation.
- Use `ibm-sf-help` for feature and platform constraint checks.

## Load Strategy (Progressive Disclosure)

1. Load this file for workflow rules.
2. Load `$SKILL_DIR/references/section-contracts.md` for section scope/dependencies.
3. Load `$SKILL_DIR/references/style-rules.md` for style constraints.
4. Load `$SKILL_DIR/references/workflow-state.md` for state protocol.
5. Load only requirement excerpts relevant to the current section.
6. Load compact prior section summaries from `section-memory.md`.

Hard limits:
- Context pack target: <= 2000 words
- Never load all previously generated sections unless user requests full revision

## Workflow

### Step 1: Initialize and Validate Inputs
- Validate user story source includes requirement ID, story text, acceptance criteria.
- Initialize state and section directories if missing.
- Extract personas, domains, integrations, and compliance needs.

### Step 2: Choose Next Section
- Pick the next dependency-ready section from `section-contracts.md`.
- Default sequence: 01 -> 16 with dependency checks.
- If user requests a specific section, verify dependencies first.

### Step 3: Build Context Pack for Current Section
Include only:
- Current section contract
- Relevant requirement excerpts
- Summary lines from dependency sections
- Applicable style rules
- Targeted Salesforce guidance from `ibm-sf-help`/`ibm-sf-architect`

### Step 4: Generate Single Section
- Write one section file at `sections/NN-<name>.md`.
- Include decisions, rationale, Salesforce mapping, risks, and traceability.
- Target 450-1000 words unless requested otherwise.

### Step 5: Update State and Memory
- Append 5-10 line summary to `section-memory.md`.
- Mark section complete in `state.json`.
- Capture changed requirements if discovered.

### Step 6: Incremental Update Flow
When requirements change:
1. Map changed requirements to impacted sections.
2. Regenerate only impacted section files.
3. Refresh section-memory entries for impacted sections.
4. Reassemble final document.

### Step 7: Assemble Final Output
Assemble files in this order:
1. Document Control
2. Input User Stories
3. Document Purpose
4. System Flow Diagrams
5. Solution Design
6. Architecture Diagrams
7. Entity Relationship Diagram
8. Data Volume and Performance
9. Integration Architecture
10. Analytics and Reporting
11. Data Migration
12. Security Architecture
13. Governance Framework
14. Risk Assessment
15. Implementation Roadmap
16. Appendices

## Quality Gate

Before finalizing:
- Every requirement appears in at least one section mapping
- Diagram narratives align with ERD and integration model
- Security and compliance controls are explicit
- LDV/performance assumptions are stated and testable
- Risks and roadmap entries are consistent with architecture decisions
