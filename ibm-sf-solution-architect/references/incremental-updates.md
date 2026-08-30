# Incremental Solution Document Updates

Workflow for updating existing solution architecture documents when user stories change.

## Update Scenarios

**Scenario 1: New Requirements Added**
- New user stories added to spreadsheet
- Existing requirements unchanged
- Need to extend solution document

**Scenario 2: Requirements Modified**
- Existing user stories updated with new acceptance criteria
- May require reworking solution design
- Maintain version history

**Scenario 3: Requirements Deprecated**
- User stories marked as out of scope
- Remove or archive related solution components
- Document rationale

## Step-by-Step Update Process

### Step 1: Load and Compare

**Load Previous Document:**
```bash
# If previous document is markdown
cat previous_solution.md > ../tmp/previous_content.txt

# If previous document is Word
python3 << 'EOF'
from docx import Document
doc = Document('previous_solution.docx')
for para in doc.paragraphs:
    print(para.text)
EOF
```

**Extract Previous Requirements:**
Parse requirements table from section 2 (Input User Stories) to create baseline.

**Compare with New User Stories:**
```python3
import openpyxl

# Load new user stories
wb = openpyxl.load_workbook('new_user_stories.xlsx')
ws = wb.active

new_requirements = []
for row in ws.iter_rows(min_row=2, values_only=True):
    new_requirements.append({
        'id': row[0],
        'story': row[2],
        'acceptance': row[3]
    })

# Compare against previous requirements
# Flag: NEW, MODIFIED, UNCHANGED, DEPRECATED
```

### Step 2: Identify Impact

**Impact Analysis Matrix:**

| Change Type | Sections to Update | Action Required |
|-------------|-------------------|-----------------|
| New persona | Context Diagram (§6), Security Model (§12) | Add persona to diagrams, define permissions |
| New data object | Solution Design (§5), ERD (§7), Volume (§8) | Define object schema, update ERD, estimate volumes |
| New integration | Integration Architecture (§9), Security (§12) | Document integration, define authentication |
| Modified flow | System Flow (§4), Solution Design (§5) | Update flowcharts, revise Apex/Flow specs |
| New report | Analytics (§10) | Add report specification |
| Deprecated requirement | All sections | Remove references, document in version history |

**Impact Analysis Logic:**
```
Change Detection Rules:

New Persona ("As a [persona]"):
→ Impacts: Context Diagram, Security Model, Permission Sets

New Data Object/Field:
→ Impacts: ERD, Solution Design, Volume Analysis

Integration Keywords (integrate, sync, connect):
→ Impacts: Integration Architecture, Security

Reporting Keywords (report, dashboard, analytics):
→ Impacts: Analytics section

Workflow Changes:
→ Impacts: System Flow Diagrams, Solution Design automation
```

### Step 3: Update Document Structure

**Version Control:**
- Increment version number (major.minor.patch)
  - Major: Significant scope change or new capability
  - Minor: Requirements added or modified
  - Patch: Corrections or clarifications
- Update document date
- Add entry to version history table

**Example:**
```
Previous: Version 1.2.0 (2026-01-15)
Current: Version 1.3.0 (2026-01-22)
Changes: Added SSO authentication requirements (REQ-015 to REQ-018)
```

### Step 4: Update Content by Section

**Section 2: Input User Stories**
- Add new requirements to table
- Mark deprecated requirements with strikethrough
- Update persona mapping table if new personas
- Recalculate requirements summary statistics

**Section 3: Document Purpose**
- Update scope if new capabilities added
- Revise success criteria if KPIs changed
- Add new assumptions or constraints

**Section 4: System Flow Diagrams**
- Redraw affected flowcharts
- Add new flows for new capabilities
- Maintain existing flows unless requirements changed

**Section 5: Solution Design**
- Add new Salesforce objects, fields, classes
- Update existing component specs if modified
- Mark deprecated components with note

**Section 6: Architecture Diagrams**
- Update C4 Context if new external systems or personas
- Update Component Diagram if new components
- Maintain diagram consistency

**Section 7: ERD**
- Add new objects and relationships
- Update cardinality if changed
- Remove deprecated objects

**Section 9: Integration Architecture**
- Add new integration specifications
- Update existing integrations if modified
- Document migration path for deprecated integrations

**Section 10: Analytics**
- Add new reports/dashboards
- Update existing if requirements changed

**Section 12: Security Architecture**
- Update permission model if new personas
- Add new security controls if required
- Document new compliance requirements

**Section 14: Risk Assessment**
- Identify new risks from added requirements
- Update mitigation strategies

**Section 15: Implementation Roadmap**
- Revise timeline if scope changed significantly
- Add new phases or milestones
- Update dependencies

**Section 16: Appendices**
- Update version history
- Add new glossary terms
- Document assumptions for new requirements

### Step 5: Cross-Reference Validation

**Traceability Validation:**
- Review requirements table against solution document
- Ensure every user story ID appears in at least one solution section
- Document untraced stories for investigation
- Verify bi-directional traceability (requirement → component, component → requirement)

**Diagram Consistency:**
- All components in diagrams must be described in text
- All external systems in integration section must appear in Context Diagram
- All objects in ERD must be documented in Solution Design

**Link Validation:**
- Verify all Salesforce documentation links still valid
- Update links if documentation moved or deprecated

### Step 6: Generate Change Summary

**Change Log Format:**
```markdown
## Version 1.3.0 Change Summary (2026-01-22)

### Requirements Added
- REQ-015: SSO authentication via Okta (§12.1)
- REQ-016: Custom email templates (§5.2)
- REQ-017: Audit trail for user actions (§12.4)

### Requirements Modified
- REQ-003: Email verification expiry changed from 24h to 72h (§5.1)
- REQ-008: Additional fields required for registration (§5.1)

### Requirements Deprecated
- REQ-012: Manual user approval (replaced by automated workflow)

### Sections Updated
- §4: Added SSO authentication flow diagram
- §5: Added Apex classes for audit logging
- §6: Updated Context Diagram with Okta IdP
- §9: Added Okta integration specification
- §12: Updated security architecture for SSO

### Impact Assessment
- Implementation timeline extended by 2 weeks for SSO integration
- Additional Salesforce license required for Shield Platform Encryption
- New risk identified: IdP availability (documented in §14)
```

### Step 7: Review and Approval

**Review Checklist for Updates:**
- [ ] All new requirements appear in user stories table
- [ ] All modified requirements show updated acceptance criteria
- [ ] Deprecated requirements marked and justified
- [ ] Version history updated
- [ ] Change summary comprehensive
- [ ] Diagrams updated and consistent
- [ ] Cross-references validated
- [ ] Implementation roadmap revised if needed
- [ ] Risk assessment updated

**Approval Process:**
- Circulate change summary to stakeholders
- Highlight high-impact changes
- Obtain sign-off before proceeding to implementation

## Update Anti-Patterns to Avoid

**Don't:**
- Create entirely new document for minor changes (maintain version history instead)
- Update diagrams without updating text descriptions
- Remove deprecated requirements without documentation
- Skip cross-reference validation
- Ignore impact on implementation timeline

**Do:**
- Maintain clear version history
- Document rationale for all changes
- Keep diagrams and text in sync
- Validate traceability after updates
- Communicate changes to all stakeholders

## Automation Opportunities

**Automated Diff Generation:**
```bash
# Compare user stories spreadsheets
python3 << 'EOF'
import openpyxl

old_wb = openpyxl.load_workbook('v1.2_user_stories.xlsx')
new_wb = openpyxl.load_workbook('v1.3_user_stories.xlsx')

# Generate diff report
# Output: requirements_diff.json
EOF
```

**Template-Based Section Updates:**
Use section templates with placeholders for new requirements, reducing manual reformatting.

**Link Checker:**
```bash
# Validate Salesforce documentation links
python3 << 'EOF'
import requests
import re

with open('solution_document.md', 'r') as f:
    content = f.read()
    
links = re.findall(r'https://[^\s\)]+', content)
for link in links:
    response = requests.head(link)
    if response.status_code != 200:
        print(f'Broken link: {link}')
EOF
```