# AMS Calculation Examples

Worked examples demonstrating the IBM AMS estimation methodology.

## Example 1: Small Single-Org Implementation

**Client Profile**:
- 46 Salesforce users (Sales Cloud + Service Cloud)
- Single production org
- 10 integrations (ERP, marketing automation, BI)
- No regulated industry
- Medium customisation level
- Historical data unavailable (new implementation)

### Step 1: Input Calculation (User-Based)

Licensed users: 46
Incident rate: 30% of users/month (industry standard)
Monthly L1 incidents: 46 × 0.30 = 13.8 ≈ 14 incidents

L1 resolution rate: 60%
L1 resolves: 14 × 0.60 = 8.4 incidents
Flow to IBM (L2/L3): 14 - 8.4 = 5.6 ≈ 6 incidents

Service requests: Estimated 5/month (validated with client)

**Override**: Client provided estimate of 12 L2/L3 incidents/month based on beta testing → use 12

### Step 2: Ticket Distribution

L2/L3 incidents (12 total):
- L1.5 (20%): 12 × 0.20 = 2.4 incidents
- L2 (50%): 12 × 0.50 = 6.0 incidents
- L3 (20%): 12 × 0.20 = 2.4 incidents
- Absorbed (10%): 1.2 incidents

Service requests (5 total):
- Basic (30%): 5 × 0.30 = 1.5 SRs
- Moderate (60%): 5 × 0.60 = 3.0 SRs
- Complex (10%): 5 × 0.10 = 0.5 SRs

### Step 3: Complexity Assessment

**Instances**: 1 org = 100 points
**Customisation**: Medium = 200 points
**Regulated**: No = 0 points
**Manager Assessment**: Medium = 400 points

**Total**: 100 + 200 + 0 + 400 = 700 points
**Category**: Low (<800)
**Multiplier**: 0.75×

### Step 4: Resolution Effort

Incidents (with 0.75× complexity multiplier):
- L1.5: 2.4 × (0.75h × 0.75) = 2.4 × 0.5625 = 1.35h
- L2: 6.0 × (3h × 0.75) = 6.0 × 2.25 = 13.5h
- L3: 2.4 × (9.75h × 0.75) = 2.4 × 7.3125 = 17.55h

**Total incident effort**: 1.35 + 13.5 + 17.55 = 32.4h/month

Service requests (no complexity adjustment):
- Basic: 1.5 × 1.5h = 2.25h
- Moderate: 3.0 × 2.5h = 7.5h
- Complex: 0.5 × 4h = 2.0h

**Total SR effort**: 2.25 + 7.5 + 2.0 = 11.75h/month

### Step 5: Non-Ticketing Activities

Baseline: 150h/month

Adjustments:
- Single org: +0h
- 10 integrations: +0h (within 10-15 baseline)
- Not regulated: +0h
- <200 users: +0h

**Total non-ticketing**: 150h/month

### Step 6: Minor Enhancements

Standard capacity: 50h/month (Years 1-3)

### Step 7: Monthly Effort Total

| Category              | Hours  |
|-----------------------|--------|
| Incident resolution   | 32.4   |
| Service requests      | 11.75  |
| Minor enhancements    | 50.0   |
| Non-ticketing         | 150.0  |
| **Total**             | **244.15** |

### Step 8: FTE Calculation

**Perform FTE**: 244.15h ÷ 172.5h = 1.42 FTE

**Adjusted FTE** (India, 0.85 factor): 1.42 ÷ 0.85 = 1.67 FTE

Shift coverage:
- Business hours only: +0 FTE
- 24×7 on-call (P1/P2): +0.15 FTE

**Total required**: 1.67 + 0.15 = 1.82 FTE → **2.0 FTE** (rounded for staffing)

### Step 9: JRSS Mapping

2.0 FTE breakdown:
- Application Developer (7B): 1.0 FTE (core delivery)
- Package Consultant (7A): 0.5 FTE (senior troubleshooting)
- Delivery Executive (7A): 0.5 FTE (coordination, metrics, client interaction)

### Step 10: Multi-Year Projection

Productivity improvements: 8% YoY (5% automation + 3% process)

| Year | Scope                          | Hours | Perform FTE | Adjusted FTE |
|------|--------------------------------|-------|-------------|--------------|
| 1    | Full (incidents, SRs, enhancements, non-ticketing) | 244.15 | 1.42 | 2.0 |
| 2    | Full, 8% productivity gain     | 224.62 | 1.30 | 1.9 |
| 3    | Full, cumulative 15.4% gain    | 206.65 | 1.20 | 1.8 |
| 4    | Enhancements excluded          | 156.65 | 0.91 | 1.5 |
| 5    | Enhancements excluded, cumulative 22.3% gain | 144.12 | 0.84 | 1.4 |

---

## Example 2: Multi-Org Regulated Implementation

**Client Profile**:
- 450 Salesforce users across Sales Cloud, Service Cloud, FSL
- 3 production orgs (EMEA, APAC, Americas)
- 28 integrations (ERP, CRM, warehouse management, BI, telephony)
- Regulated (financial services - FCA compliance)
- High customisation
- Historical data: 85 L2/L3 incidents/month, 25 SRs/month

### Step 1: Input Calculation (Ticket-Based)

Historical data available → use directly:
- L2/L3 incidents: 85/month
- Service requests: 25/month

### Step 2: Ticket Distribution

L2/L3 incidents (85 total):
- L1.5 (20%): 85 × 0.20 = 17 incidents
- L2 (50%): 85 × 0.50 = 42.5 ≈ 43 incidents
- L3 (20%): 85 × 0.20 = 17 incidents
- Absorbed: 8 incidents

Service requests (25 total):
- Basic (30%): 25 × 0.30 = 7.5 ≈ 8 SRs
- Moderate (60%): 25 × 0.60 = 15 SRs
- Complex (10%): 25 × 0.10 = 2.5 ≈ 2 SRs

### Step 3: Complexity Assessment

**Instances**: 3 orgs = 300 points
**Customisation**: High = 300 points
**Regulated**: Yes = 200 points
**Manager Assessment**: High = 800 points

**Total**: 300 + 300 + 200 + 800 = 1600 points
**Category**: Medium-High (1150-1600)
**Multiplier**: 1.2×

### Step 4: Resolution Effort

Incidents (with 1.2× complexity multiplier):
- L1.5: 17 × (0.75h × 1.2) = 17 × 0.9 = 15.3h
- L2: 43 × (3h × 1.2) = 43 × 3.6 = 154.8h
- L3: 17 × (9.75h × 1.2) = 17 × 11.7 = 198.9h

**Total incident effort**: 15.3 + 154.8 + 198.9 = 369h/month

Service requests (no complexity adjustment):
- Basic: 8 × 1.5h = 12h
- Moderate: 15 × 2.5h = 37.5h
- Complex: 2 × 4h = 8h

**Total SR effort**: 12 + 37.5 + 8 = 57.5h/month

### Step 5: Non-Ticketing Activities

Baseline: 150h

Adjustments:
- Additional 2 orgs: +40h (20h each)
- 28 integrations (13 beyond baseline 15): +39h (3h each)
- Regulated industry: +30h (compliance, audit support)
- >200 users: +20h (admin overhead)

**Total non-ticketing**: 150 + 40 + 39 + 30 + 20 = 279h/month

### Step 6: Minor Enhancements

Increased capacity (multi-org): 75h/month

### Step 7: Monthly Effort Total

| Category              | Hours  |
|-----------------------|--------|
| Incident resolution   | 369.0  |
| Service requests      | 57.5   |
| Minor enhancements    | 75.0   |
| Non-ticketing         | 279.0  |
| **Total**             | **780.5** |

### Step 8: FTE Calculation

**Perform FTE**: 780.5h ÷ 172.5h = 4.52 FTE

**Adjusted FTE** (India 80%, UK 20%):
- India portion: 4.52 × 0.80 = 3.62 FTE, adjusted: 3.62 ÷ 0.85 = 4.26 FTE
- UK portion: 4.52 × 0.20 = 0.90 FTE, adjusted: 0.90 ÷ 0.80 = 1.13 FTE
- Combined: 4.26 + 1.13 = 5.39 FTE

Shift coverage:
- Extended hours (14h/day across timezones): +0.6 FTE
- Weekend on-call: +0.2 FTE
- 24×7 P1/P2: +0.15 FTE

**Total required**: 5.39 + 0.6 + 0.2 + 0.15 = 6.34 FTE → **6.5 FTE** (rounded)

### Step 9: JRSS Mapping

6.5 FTE breakdown:
- Application Developer (7B): 3.5 FTE (core delivery, split shifts)
- Package Consultant (7A): 1.5 FTE (senior support, complex troubleshooting)
- Solution Architect (8A): 0.5 FTE (architecture queries, integration issues)
- Technical Architect (8B): 0.25 FTE (high-complexity escalations)
- Delivery Executive (7A): 0.75 FTE (client management, reporting, governance)

### Step 10: Multi-Year Projection

Productivity improvements: 10% YoY (6% automation, 4% tooling/process)

| Year | Scope | Hours | Perform FTE | Adjusted FTE |
|------|-------|-------|-------------|--------------|
| 1    | Full  | 780.5 | 4.52        | 6.5          |
| 2    | Full, 10% productivity | 702.5 | 4.07 | 6.0 |
| 3    | Full, cumulative 19% gain | 632.2 | 3.66 | 5.5 |
| 4    | Enhancements excluded | 557.2 | 3.23 | 5.0 |
| 5    | Enhancements excluded, cumulative 27.1% gain | 501.5 | 2.91 | 4.5 |

### Key Assumptions

- EMEA and APAC require extended coverage (06:00-22:00 UK time)
- FCA audit support included in non-ticketing (quarterly cycles)
- Integration monitoring assumes 60% near-real-time, 40% batch
- 3 orgs have separate sandbox environments (UAT, staging)
- Client provides Salesforce Shield for compliance logging

### PCR Triggers

- Additional org beyond 3 (+100h/month baseline)
- Integration count exceeds 35 (+3h each)
- Ticket volume exceeds ±10% deadband over 3 months
- Scope addition: new Salesforce cloud (e.g., Commerce Cloud)
- Compliance regime change (e.g., DORA regulations)

---

## Example 3: Scaling Scenario (Year-Over-Year Growth)

**Client Profile**:
- Year 1: 150 users, 2 orgs, 35 L2/L3 incidents/month, 12 SRs/month
- Year 2: Platform expansion - add Marketing Cloud (+50 users, +1 org)
- Year 3: FSL implementation (+75 users, +1 org)

### Year 1 Baseline

Complexity: Medium (score 1000, multiplier 1.0×)

| Category              | Hours  |
|-----------------------|--------|
| Incident resolution   | 127.5  |
| Service requests      | 30.0   |
| Minor enhancements    | 50.0   |
| Non-ticketing         | 190.0  |
| **Total**             | **397.5** |

Perform FTE: 2.30 → Adjusted: 3.0 FTE

### Year 2 (Marketing Cloud Added)

Additional scope:
- +1 org: +20h non-ticketing
- +8 integrations: +24h non-ticketing
- Incident volume +15% (platform expansion): 35 → 40 incidents
- SR volume +20%: 12 → 14 SRs
- Complexity increases to Medium-High (score 1200, multiplier 1.1×)

Productivity improvement: -8%

| Category              | Hours (before productivity) | After 8% gain |
|-----------------------|-----------------------------|---------------|
| Incident resolution   | 167.4 (40 incidents × 1.1 multiplier) | 154.0 |
| Service requests      | 35.0 (14 SRs)              | 32.2          |
| Minor enhancements    | 50.0                       | 46.0          |
| Non-ticketing         | 234.0 (+44h)               | 215.3         |
| **Total**             | **486.4**                  | **447.5**     |

Perform FTE: 2.59 → Adjusted: 3.2 FTE

**PCR required**: +1 org, +8 integrations, +15% ticket volume exceeds deadband

### Year 3 (FSL Added)

Additional scope:
- +1 org: +20h non-ticketing
- +5 integrations (warehouse, telematics): +15h non-ticketing
- FSL mobile complexity: +10h non-ticketing (offline sync monitoring)
- Incident volume +10%: 40 → 44 incidents
- SR volume +15%: 14 → 16 SRs
- Complexity remains Medium-High (1.1×)

Cumulative productivity: Year 1 → Year 2 (8%) → Year 3 (additional 8%) = 15.4% total

| Category              | Hours (before productivity) | After 15.4% cumulative gain |
|-----------------------|-----------------------------|------------------------------|
| Incident resolution   | 184.1 (44 incidents)       | 155.8                        |
| Service requests      | 40.0 (16 SRs)              | 33.8                         |
| Minor enhancements    | 50.0                       | 42.3                         |
| Non-ticketing         | 279.0 (+45h)               | 236.0                        |
| **Total**             | **553.1**                  | **467.9**                    |

Perform FTE: 2.71 → Adjusted: 3.5 FTE

**PCR required**: +1 org, +5 integrations, FSL complexity addition

### 3-Year Trajectory

| Year | Orgs | Clouds | L2/L3 Incidents | Adjusted FTE | Δ vs Prior Year |
|------|------|--------|-----------------|--------------|-----------------|
| 1    | 2    | Sales, Service | 35           | 3.0          | Baseline        |
| 2    | 3    | +Marketing     | 40           | 3.2          | +0.2 (PCR)      |
| 3    | 4    | +FSL           | 44           | 3.5          | +0.3 (PCR)      |

Despite 25% incident growth and 2× org count, productivity improvements contained FTE growth to 17% total.

---

## Calculation Reference Tables

### Standard Resolution Hours (Pre-Multiplier)

| Ticket Type        | Base Hours |
|--------------------|------------|
| L1.5 Incident      | 0.75       |
| L2 Incident        | 3.00       |
| L3 Incident        | 9.75       |
| Basic SR           | 1.50       |
| Moderate SR        | 2.50       |
| Complex SR         | 4.00       |

### Complexity Scoring Matrix

| Factor              | Low   | Medium | High  |
|---------------------|-------|--------|-------|
| Instances           | 100   | 200    | 300+  |
| Customisation       | 100   | 200    | 300   |
| Regulated (Y/N)     | 0/200 | -      | -     |
| Manager Assessment  | 200   | 400    | 800   |

**Score bands**:
- <800: Low (0.75×)
- 800-1149: Medium (1.0×)
- 1150-1600: Medium-High (1.2×)
- >1600: High (1.5×)

### Non-Ticketing Baselines

| Activity Category      | Base Hours/Month | Scaling Factor |
|------------------------|------------------|----------------|
| Platform monitoring    | 60               | +20h per additional org |
| Integration monitoring | 40               | +3h per integration beyond 15 |
| Compliance/governance  | 30               | +30h if regulated |
| DevOps                 | 20               | +10h per additional org |
| Admin overhead         | -                | +20h if >200 users |

### Labour Factors

| Location        | Factor | Rationale |
|-----------------|--------|-----------|
| India           | 0.85   | Training, leave, meetings |
| UK              | 0.80   | Meetings, admin, knowledge sharing |
| Multi-location  | Weighted average | Based on split % |

### Shift Premium FTE

| Coverage Type           | Additional FTE |
|-------------------------|----------------|
| Extended hours (>8h/day)| +0.3 per shift |
| Weekend coverage        | +0.2           |
| 24×7 on-call (P1/P2)    | +0.15          |
