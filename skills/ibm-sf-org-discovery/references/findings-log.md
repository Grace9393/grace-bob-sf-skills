# Findings Log — Schema & Usage

Maintain this log throughout the discovery session. Add an entry for every
risk, gap, or data gap identified. This log feeds directly into the final report.

---

## Entry Schema

```
ID:          [R01, R02, ...] — sequential, prefixed R
Domain:      [Domain name]
Type:        Risk | Data Gap | Quick Win | Innovation Opportunity
Finding:     [One sentence — what is wrong or missing]
Evidence:    [What the client said or failed to say that confirms this]
Impact:      [Business consequence if unaddressed]
Severity:    Critical | High | Medium | Low
Effort:      Low (<1 week) | Medium (1–4 weeks) | High (>1 month)
Action:      [Specific recommended action]
Owner:       [IBM | Client | Joint | TBC]
Priority:    Immediate | Short-term (30–90 days) | Strategic (90+ days)
```

---

## Example Entries

```
ID:       R01
Domain:   Licensing & Edition
Type:     Risk
Finding:  120 of 400 assigned licences have not been accessed in over 90 days
Evidence: Client confirmed no process exists to review or reclaim dormant licences
Impact:   Estimated £48,000 annual spend on unused licences
Severity: High
Effort:   Low
Action:   Run licence usage report; deactivate dormant users; implement 90-day review cycle
Owner:    Joint
Priority: Immediate

---

ID:       R02
Domain:   Disaster Recovery
Type:     Data Gap
Finding:  No Recovery Time Objective or Recovery Point Objective defined
Evidence: Client unable to answer when asked; no DR plan document shared
Impact:   In a P1 outage, no target for recovery exists — business impact duration unknown
Severity: Critical
Effort:   Medium
Action:   Facilitate DR requirements workshop with business and IT; document RTO/RPO; test annually
Owner:    Joint
Priority: Short-term

---

ID:       R03
Domain:   Innovation & AI Readiness
Type:     Innovation Opportunity
Finding:  High-volume manual case triage process is a strong Agentforce candidate
Evidence: Client described 3 FTE dedicated to routing 800+ cases/week using fixed criteria
Impact:   Potential 60–70% reduction in manual triage effort; faster SLA response
Severity: N/A
Effort:   Medium
Action:   Scope Agentforce pilot for case triage; present IBM Client Zero reference story
Owner:    IBM
Priority: Strategic
```

---

## Data Gap Convention

When a client cannot answer a question, log it as a Data Gap — do not leave it
blank or skip it. The inability to answer is itself a risk indicator.

Example:
```
ID:       R07
Domain:   Release Management
Type:     Data Gap
Finding:  Client unable to confirm whether rollback procedures have been tested
Evidence: "I think we have something documented but I'd need to check with the team"
Impact:   Untested rollback procedures may fail at the moment of need
Severity: High
Effort:   Low
Action:   Request procedure document; schedule a dry-run exercise
Owner:    Client
Priority: Short-term
```
