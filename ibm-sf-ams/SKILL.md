---
name: ibm-sf-ams
description: Estimate IBM Application Management Services (AMS) for Salesforce implementations using ticket-based or user-based models. Use when creating AMS proposals, sizing support teams, calculating FTE requirements, or scoping managed services for Salesforce Service Cloud, Sales Cloud, Marketing Cloud, CRM Analytics, FSL, Service Cloud Voice, or Agentforce implementations. Handles incident/service request estimation, complexity assessment, minor enhancement capacity, non-ticketing activities, IBM GenAI accelerators, and multi-year staffing projections.
metadata:
  skills-required:
    - ibm-sf-solution-architect
---

# IBM AMS Salesforce Estimation

Estimate Application Management Services for Salesforce platforms using industry-standard IBM methodologies.

## Context Management

Write output to `./tmp/ibm-sf-ams-estimation.md` only when the user asks for persisted artifacts or when chaining skills needs a handoff file. This remains the canonical AMS filename across bid skills. Keep responses inline by default, and copy final deliverables to `./outputs` at completion.

## Estimation Workflow

Execute steps sequentially. Override defaults only with documented justification.

### Step 0: Determine Contract Duration

**Default: 5 years** (Years 1-5 projection)

Adjust based on:
- Client contract length (typical: 3-5 years)
- Regulatory requirements (some industries require 7+ year projections)
- Platform lifecycle (migrations, decommissions)

All subsequent calculations scale to selected duration.

### Step 1: Determine Input Method

**Ticket-based** (preferred):
- Historical L2/L3 incident count/month
- Historical service request count/month

**User-based**:
- Licensed users × 30% incident rate = monthly L1 incidents
- L1 resolves 60% (default, validate with client)
- Remaining 40% flows to IBM L2/L3
- Service requests estimated separately

### Step 2: Calculate Ticket Distribution

Apply default splits (from IBM historical data):

**Incidents** (L2/L3 total):
- L1.5: 20%
- L2: 50%
- L3: 20%
- Remaining 10% absorbed in rounding

**Service Requests** (monthly total):
- Basic: 30%
- Moderate: 60%
- Complex: 10%

Document overrides with client-specific rationale.

### Step 3: Assess Complexity

Calculate weighted score from four factors:

**Instances**: Count Salesforce orgs
- 1 = 100 points
- 2 = 200 points
- 3 = 300 points
- 4 = 400 points
- 5 = 500 points
- >5 = 600 points

**Customisation Level**:
- Low (mostly standard, <20% custom) = 100 points
- Medium (balanced mix, 20-50% custom) = 200 points
- High (heavily customised, >50% custom) = 300 points

**Regulated Industry**:
- No = 0 points
- Yes (finance, healthcare, government) = 200 points

**Solution Manager Assessment**:
- Low complexity = 200 points
- Medium complexity = 400 points
- High complexity = 800 points

**Total Score Interpretation**:
- <800: Low complexity → 0.75× effort multiplier
- 800-1149: Medium → 1.0× multiplier
- 1150-1600: Medium-High → 1.2× multiplier
- >1600: High → 1.5× multiplier

Apply multiplier to incident resolution hours only (not SRs, enhancements, or non-ticketing).

### Step 4: Calculate Resolution Effort

**Base hours per ticket** (before complexity multiplier):

Incidents:
- L1.5: 0.75h × complexity multiplier
- L2: 3h × complexity multiplier
- L3: 9.75h × complexity multiplier

Service Requests (no complexity adjustment):
- Basic: 1.5h
- Moderate: 2.5h
- Complex: 4h

**Monthly incident effort** = (L1.5_count × L1.5_hours) + (L2_count × L2_hours) + (L3_count × L3_hours)

**Monthly SR effort** = (Basic_count × 1.5h) + (Moderate_count × 2.5h) + (Complex_count × 4h)

### Step 5: Add Non-Ticketing Activities

**Baseline: 150h/month** for single-org, 10-15 integrations. Scale for:

**Agentforce Considerations**:
- Add 30h/month for Agentforce agent monitoring and tuning
- Add 20h/month for knowledge article curation for agents
- Add 15h/month for agent performance analytics and optimization
- Total Agentforce overhead: +65h/month if deployed

Platform activities (∼60h):
- Salesforce org monitoring (health checks, limits, storage)
- User access reviews, licence management
- Data quality monitoring
- Backup/recovery validation

Integration monitoring (∼40h):
- Interface health checks (10-15 integrations assumed)
- Error log reviews
- Data flow validation
- API consumption tracking

Compliance/governance (∼30h):
- RCA documentation for major incidents
- Audit log reviews (if regulated)
- Security posture monitoring
- Change advisory board participation

DevOps (∼20h):
- Sandbox refresh management
- Deployment pipeline maintenance
- Environment synchronisation
- Release coordination support

**Adjustments**:
- Add 20h per additional org beyond first
- Add 3h per integration beyond 15
- Add 30h if regulated industry (SOC2, GDPR, HIPAA audits)
- Add 20h if >200 users (increased admin overhead)

### Step 6: Minor Enhancements

**Default capacity: 50h/month**

Scope:
- Configuration changes (workflows, page layouts, validation rules)
- Report/dashboard creation
- Simple automations (Process Builder, Flow)
- Data loads/updates

Out of scope (require separate estimation):
- Custom Apex development
- Integration builds
- Major process redesigns
- New module implementations

**Deadband**: ±10% variation over rolling 3-month period. Beyond deadband triggers PCR.

### Step 7: Calculate FTE

**Monthly hours** = Incident effort + SR effort + Enhancement effort + Non-ticketing effort

**Perform FTE** = Monthly hours ÷ 172.5h (standard monthly capacity at 100% utilisation)

**Adjusted FTE** = Perform FTE ÷ labour factor

Labour factors by location:
- India: 0.85 (accounts for training, leave, overhead)
- UK: 0.80
- Multi-location: weighted average

Add shift premiums separately:
- Extended coverage (>8h/day): +0.3 FTE per shift
- Weekend coverage: +0.2 FTE
- 24×7 on-call: +0.15 FTE for rotation pool

### Step 8: IBM Accelerators & GenAI Tools

**Salesforce Accelerator (SFA)** - GenAI-based assets:
- **Ticket resolution efficiency**: 1.5-3% YoY effort reduction
- **Knowledge base auto-generation**: Converts resolved tickets to KB articles
- **Automated code suggestions**: Context-aware fixes for common issues
- **Dependencies**: Client infrastructure readiness, GenAI solution adoption, data access permissions

**IBM Consulting Assistant** - GenAI DevOps automation:
- **Deployment automation**: 1% YoY effort reduction
- **Code review automation**: Accelerated PR reviews with AI-assisted analysis
- **Test case generation**: Automated test scenario creation
- **Integration**: Works with Azure DevOps (ADO) pipelines

**GenAI Test Automation**:
- **Regression testing reduction**: 1% YoY
- **Quality improvement**: Fewer production defects through intelligent test coverage
- **Adaptive testing**: Self-healing test scripts that adjust to UI changes

**Native Salesforce Tools**:
- **Einstein Bots**: L1 ticket deflection (3% incident reduction Y1-Y2)
- **Einstein Next Best Action**: Proactive issue prevention
- **Flow Orchestration**: Multi-step automation without code
- **Agentforce**: Autonomous AI agents for case resolution, knowledge retrieval, and workflow automation
  - **Case deflection**: 5-10% L1/L1.5 ticket reduction through autonomous agent resolution
  - **Knowledge curation**: Requires ongoing agent tuning and knowledge base maintenance
  - **Support overhead**: +65h/month for monitoring, tuning, and optimization (see Step 5)
  - **Prerequisites**: Salesforce Data Cloud, Service Cloud, robust knowledge base

**Implementation Costs**:
- **Automation SME**: 0.2 FTE (Y1-Y2) for tool implementation and optimization
- **One-time costs (OTC)**: Tool setup, integration, training (typically $8,000-$24,000)
- **Monthly recurring costs (MRC)**: Platform fees, API consumption charges

**Critical Validation**:
- Confirm client infrastructure supports GenAI tools (network access, security clearances)
- Verify data residency and compliance requirements (GDPR, HIPAA, SOC2)
- Validate budget approval for OTC/MRC costs
- Assess client's risk appetite for GenAI adoption

**Important**: All accelerator benefits are subjective to:
- Client GenAI solution adoption maturity
- Security/compliance clearances
- Infrastructure and network readiness
- Change management capability

### Step 9: Apply Productivity Improvements

Combine **manual process improvements** with **IBM accelerators** (from Step 8) for year-over-year FTE reduction.

**Process Maturity** (typical: 2-4% YoY):
- **Problem management**: KPI monitoring, RCA documentation for repetitive incidents (1.5%)
- **Knowledge gain/efficiency**: Knowledge base growth, runbook standardization (3-3.5% Y1-Y2)
- **Preventive maintenance**: Proactive monitoring reduces reactive tickets

**IBM Accelerators** (from Step 8):
- **SFA native tools**: GenAI ticket resolution, Einstein Bots (1.5-3% YoY)
- **GenAI DevOps + Test automation**: IBM Consulting Assistant, automated testing (1-2% YoY)
- **Infrastructure-dependent**: Actual benefit varies based on client readiness

**Total Productivity Range**: 5-10% YoY cumulative
- **Conservative (5%)**: Mature platforms, limited automation adoption, regulated industries
- **Moderate (7-8%)**: Balanced mix of process and tooling improvements
- **Aggressive (10%)**: New engagement with high automation potential, client committed to GenAI

**Breakdown by Category**:
- **Ticket Reduction**: Problem management, Einstein Bots, proactive monitoring (2-3%)
- **Team Efficiency**: Knowledge tools, SFA accelerators, process optimization (2-4%)
- **Automation**: GenAI DevOps, test automation, deployment pipelines (1-2%)
- **Quality**: Fewer production defects, reduced rework (1%)

**Important Constraints**:
- Accelerator benefits are subjective to client GenAI solution adoption
- Infrastructure readiness impacts actual realization
- Conservative estimates recommended for regulated industries
- Productivity gains require 2-3 months ramp-up post-implementation

**Cumulative application**: Year 2 = Year 1 × (100% - improvement%), Year 3 = Year 2 × (100% - improvement%)

### Step 10: JRSS Role Mapping

Map FTE to IBM job classifications:

**Premium bands** (typical 70% of team):
- Application Developer-Salesforce (Band 7B): Core delivery, 50-60% of FTE
- Package Consultant-Salesforce (Band 7A/8A): Senior troubleshooting, 20-30%
- Solution/Technical Architect (Band 8A/8B): Complex issues, architecture, 10-15%

**Standard bands** (typical 30%):
- Business Sales & Delivery Executive (Band 7A): Coordination, reporting, metrics

All roles → BTS → Customer Transformation → Salesforce → DXX-Salesforce X6

Validate band distribution against skill requirements and shift coverage needs.

### Step 11: Multi-Year Projection

Project FTE across contract duration (from Step 0, typically 5 years).

**Years 1-3**: Full scope
- All ticket categories
- Minor enhancements (50h/month default)
- Full non-ticketing activities
- IBM accelerator implementation (Step 8)

**Years 4-5** (if applicable): Adjusted scope
- Tickets and non-ticketing continue
- Minor enhancements often excluded (review with client)
- Platform may expand (add clouds) or contract (retirements)
- Accelerator benefits fully realized

**Key Adjustments**:
- Apply cumulative productivity improvements from Step 9 each year
- Factor in accelerator ramp-up time (2-3 months for full benefit realization)
- Model scope change scenarios (platform expansion, cloud additions, retirements)
- Account for potential ticket volume growth (user base expansion, new integrations)

**Important**: For contracts shorter than 5 years, adjust projection table accordingly. For contracts longer than 5 years, extend productivity assumptions conservatively (diminishing returns after Year 5).

## Standard Assumptions

Validate these for each deal:

**Support model**:
- Client provides L1 helpdesk (KDI assumed)
- IBM delivers L1.5, L2, L3
- L1 resolves 60-65% of total incidents
- ITSM tool: ServiceNow

**Coverage**:
- Business hours: 06:00-18:00 Irish time
- Primary delivery: India offshore
- 24×7 on-call for P1/P2 incidents
- Shift coverage calculated separately

**Transition**:
- 4 weeks IBM-to-IBM knowledge transfer
- Steady state commences after transition
- Assumes incumbent documentation exists

**Technology stack** (typical):
- Service Cloud
- Sales Cloud
- Marketing Cloud
- CRM Analytics (Tableau CRM)
- Field Service Lightning
- Service Cloud Voice
- Agentforce (autonomous AI agents)
- Integrations: Amazon Connect, ERP, data warehouses

**Contractual**:
- Deadband: ±10% over 3-month rolling window
- PCR triggers: beyond deadband, scope additions, major platform changes
- Client provides all licences (Salesforce, integrations, tools)
- IBM team licences charged to client

## Validation Checklist

Before finalising:

- [ ] Contract duration confirmed (Step 0)
- [ ] Complexity assessment reviewed with Solution Manager
- [ ] Ticket distribution validated against client history (if available)
- [ ] Non-ticketing hours scaled to actual org/integration count
- [ ] All default overrides documented with remarks
- [ ] Location effort split totals 100%
- [ ] Shift coverage FTE calculated separately from perform FTE
- [ ] IBM accelerators validated with client (infrastructure, approvals, costs)
- [ ] Productivity assumptions separated: manual vs accelerator-driven
- [ ] JRSS bands aligned with skill requirements
- [ ] Multi-year productivity assumptions validated
- [ ] PCR triggers identified and documented
- [ ] Assumptions log created for client review

## Output Format

Provide structured summary:

**Volumetrics**:
- Monthly L2/L3 incidents: [count]
- Monthly service requests: [count]
- Complexity score: [score] ([category], [multiplier]×)

**Monthly Effort (Year 1)**:
- Incident resolution: [hours]
- Service requests: [hours]
- Minor enhancements: [hours]
- Non-ticketing: [hours]
- **Total**: [hours]

**Staffing (Year 1)**:
- Perform FTE: [count]
- Adjusted FTE: [count] ([location], [labour factor])
- Shift coverage: +[count] FTE
- **Total**: [count] FTE

**JRSS Breakdown**:
- Application Developer-Salesforce (7B): [count] FTE
- Package Consultant-Salesforce (7A): [count] FTE
- Solution Architect (8A): [count] FTE
- Delivery Executive (7A): [count] FTE

**5-Year Projection**:
| Year | Total Hours | Perform FTE | Productivity Δ | Notes |
|------|-------------|-------------|----------------|-------|
| 1    | [hours]     | [fte]       | Baseline       | [scope notes] |
| 2    | [hours]     | [fte]       | [%]            | [scope notes] |
| 3    | [hours]     | [fte]       | [%]            | [scope notes] |
| 4    | [hours]     | [fte]       | [%]            | [scope notes] |
| 5    | [hours]     | [fte]       | [%]            | [scope notes] |

**IBM Accelerators Included**:
- Salesforce Accelerator (SFA): [Yes/No] - GenAI ticket resolution ([X]% productivity impact)
- IBM Consulting Assistant: [Yes/No] - DevOps automation ([X]% productivity impact)
- GenAI Test Automation: [Yes/No] - Automated testing ([X]% productivity impact)
- Einstein Bots: [Yes/No] - L1 ticket deflection ([X]% ticket reduction)
- **Implementation costs**: OTC: [amount], MRC: [amount/month], SME effort: [0.2 FTE Y1-Y2]
- **Dependencies**: [List infrastructure requirements, client approvals, security clearances]
- **Ramp-up period**: [2-3 months for full benefit realization]

**Key Assumptions**:
- [List critical assumptions]

**PCR Triggers**:
- [List scenarios requiring price change]

## References

See `references/calculation_examples.md` for worked examples with actual client scenarios.
