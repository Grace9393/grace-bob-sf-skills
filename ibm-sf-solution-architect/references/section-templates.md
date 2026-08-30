# Solution Architecture Section Templates

High-level architecture templates for Salesforce solution documentation.

## Template Usage

Each template provides structure and guidance at **architecture level** - focused on WHAT the solution does, not HOW it's implemented. Suitable for architects, business stakeholders, and technical leads.

**Abstraction Principles:**
- No code snippets or implementation details
- Component purpose and logical flow, not syntax
- Configuration strategy, not specific settings
- Data architecture, not field-level specifications
- Integration patterns, not API code

## 1. Document Control Section

Standard document metadata and governance structure.

**Key Elements:**
- Version history table
- Review and approval tables
- Table of contents with section numbering

**Example Structure:**
```
Version: 0.1
Date: 2026-01-15
Author: Solution Team
Status: Draft

Document History:
Version | Date | Author | Changes
0.1 | 2026-01-15 | Team | Initial draft

Review Table:
Reviewer | Role | Review Date | Status
[Name] | Architect | TBD | Pending

Approval Table:
Approver | Role | Approval Date | Status
[Name] | Director | TBD | Pending
```

## 2. Input User Stories Section

Structured presentation of all requirements and user stories with traceability.

**Key Elements:**
- Requirements summary statistics
- Complete user story table with acceptance criteria
- Persona-to-Salesforce role mapping
- Priority classification

**Table Format:**
```
Req ID | User Story | Acceptance Criteria | Priority | Section Ref
REQ-001 | As [persona], I want [action] so that [benefit] | • Criterion 1 • Criterion 2 | High | §4.1
```

## 3. Document Purpose Section

Three subsections: System Overview, Problem Definition, Scope and Vision.

**System Overview:** 2-3 paragraph executive summary covering primary business objective, key stakeholders, core capabilities, technical foundation (Salesforce products), integration landscape.

**Problem Definition:** Current state challenges, business impact (quantified where possible), specific pain points being addressed.

**Scope and Vision:** 
- In-scope capabilities (bulleted list)
- Out-of-scope items with justification
- Assumptions and constraints
- Success criteria with measurable KPIs

## 4-7. Technical Design Sections

These sections contain Mermaid diagrams:
- System Flow Diagrams (flowcharts showing business process flow)
- Component Architecture (C4 diagrams showing system context and components)
- Entity Relationship Diagrams (ERD showing data model)

Refer to main SKILL.md for specific Mermaid syntax examples.

**Focus:** Logical architecture and data flow, not implementation details.

## 5. Solution Design Section

High-level architecture describing solution components.

**Data Architecture:**
```markdown
### Standard Objects Utilised
- **Account:** Customer organisations, customised with Industry_Segment__c and Annual_Contract_Value__c fields
- **Contact:** Associated with Accounts, extended with Preferred_Communication_Channel__c
- **User:** Platform users, extended with Email_Verified__c and verification tracking

### Custom Objects
- **Email_Verification__c:** Tracks verification lifecycle, Master-Detail to User, stores token and expiry
- **Support_Request__c:** Custom support ticketing, alternative to Case with industry-specific fields

### Data Model Approach
- Master-Detail relationships for parent-child lifecycle control
- Lookup relationships for flexible associations
- Junction objects for many-to-many (e.g., Account-to-Product via Account_Product__c)
```

**Process Automation Strategy:**
```markdown
### Declarative Automation
- **Validation Rules:** Email format, required field combinations, date range logic
- **Flows:** 
  - User registration (Screen Flow with multi-step form)
  - Email verification process (Auto-launched triggered by user action)
  - Case escalation (Record-triggered Flow on priority change)
- **Approval Processes:** User account approval for high-risk segments

### Programmatic Automation Required
- **Triggers:** Complex duplicate detection, cross-object data synchronisation
- **Batch Jobs:** Daily token cleanup, weekly reporting aggregation
- **Scheduled Apex:** Nightly data archival, monthly compliance reports

### Automation Rationale
Maximise declarative to reduce maintenance overhead. Custom code only where:
- Complex multi-object logic required
- Governor limits necessitate bulk processing
- External system integration requires error handling
```

**User Interface Architecture:**
```markdown
### Experience Cloud Portal
**Template Selected:** Customer Service (Aura)
**Justification:** Provides out-of-box authentication, case management, knowledge base

**Page Strategy:**
- Home: Landing page with dynamic content based on user segment
- Registration: Multi-step form with inline validation
- User Dashboard: Personalised view of recent activity and cases
- Knowledge Base: Self-service support articles with search

**Mobile Considerations:**
- Responsive design for 30% mobile user base
- Key workflows optimised for mobile (case creation, profile updates)
- Progressive Web App capabilities for offline access
```

**Security and Access Control:**
```markdown
### Profile Strategy
- Minimise custom profiles (maintenance overhead)
- Use standard profiles as base: System Administrator, Standard User
- Custom profiles only where license type differs: Community User Profile

### Permission Sets
- Modular access via permission sets for flexibility
- Examples: Advanced_Reporting, Bulk_Data_Operations, External_Integration_Access

### Sharing Model
**Organisation-Wide Defaults:**
- Account: Private (controlled access via hierarchy and sharing rules)
- Contact: Controlled by Parent
- Case: Public Read/Write (internal), Private (community users see own only)

**Sharing Rules:**
- Criteria-based: Share open Cases with Support Team (Status = 'Open')
- Ownership-based: Share Accounts from inactive users to Sales Management

### Authentication
- **Current:** Username/password with email verification
- **Roadmap:** SSO via SAML 2.0 (Q2), MFA required for all users (Q3)
```

## 8. Data Volume and Performance Section

**Current Volumes Table:**
```
Data Category | Volume | Growth Rate
User Records | 50,000 | 20% annually
Daily Registrations | 150 | Seasonal peaks
```

**Performance Requirements:**
- Page load targets (<2s)
- API response targets (<500ms)
- Batch processing throughput

**LDV Considerations:** Only if object volumes approach 1M records

## 9. Integration Architecture Section

For each integration system:

**Integration Profile:**
- System name and purpose
- Integration type (REST, SOAP, Platform Events, etc.)
- Data direction and frequency
- Authentication method
- Endpoint details
- Error handling strategy
- Monitoring approach

**Sequence Diagram:** Mermaid sequence diagram showing integration flow

## 10. Analytics and Reporting Section

**Standard Reports:** List of required reports with columns, filters, groupings

**Dashboards:** Dashboard specifications with components:
- Metrics
- Charts (line, bar, donut, etc.)
- Gauges
- Tables

**Einstein Analytics:** Optional section if using CRM Analytics, includes datasets and predictive models

## 11-16. Supporting Sections

**Data Migration:** Strategy, phases, tools, scripts
**Security Architecture:** Authentication, authorisation, encryption, compliance
**Governance Framework:** Change management, metadata standards, compliance monitoring
**Risk Assessment:** Risk description, impact, probability, mitigation, contingency
**Implementation Roadmap:** Phased timeline with deliverables per phase
**Appendices:** Glossary, assumptions, references, version history