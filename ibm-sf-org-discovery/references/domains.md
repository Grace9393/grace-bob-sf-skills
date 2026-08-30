# Discovery Domains — Question Bank

12 domains. Each has **core questions** (always asked) and **probe questions**
(asked only when answers reveal risk, ambiguity, or data gaps).

---

## Domain 1 — Licensing & Edition

**Core questions**
1. Which Salesforce edition is deployed — Professional, Enterprise, Unlimited, or Developer?
2. How many licences are purchased, assigned, and actively used (logged in within the last 30 days)?
3. What add-on products are in the contract (Marketing Cloud, Service Cloud, CPQ, Einstein, Data Cloud, etc.)?
4. Are there any permission set licences (PSLs), and how many are allocated versus consumed?
5. Are there known edition limitations currently blocking any business requirements?

**Probe questions**
- When was the edition last reviewed against business requirements?
- How many licences are unassigned or have had no login in 90+ days, and what is the reclamation process?
- What is the average daily API call consumption, and how does this compare to the per-edition limit?
- Are there seasonal or temporary licence spikes, and has flex licensing been explored?
- Has a cost-benefit analysis for edition upgrade been conducted in the last 12 months?
- What Platform, Community, or Experience Cloud licences exist, and what is the monthly active user count?
- Are there add-on products that were purchased but never fully implemented?
- What is the contract renewal date, and is edition re-evaluation planned?

---

## Domain 2 — Data & Storage

**Core questions**
1. What percentage of data storage and file storage is currently consumed?
2. Which objects hold the largest record volumes?
3. Are there recurring governor limit warnings in logs or email alerts?
4. What data retention and archiving policies are in place, and are they actively enforced?

**Probe questions**
- What is the month-over-month storage growth trend for the past 12–24 months?
- What are the top 10 objects by record count and by storage consumed?
- Are there large file attachments or Chatter files consuming disproportionate file storage?
- Are any batch jobs or integrations consistently approaching heap size, SOQL row, or DML limits?
- What archiving or purging tools are in use (OwnBackup Archive, Salesforce Archiving, custom)?
- At current growth rate, when will data storage reach 80% capacity?
- Have any API limit exhaustion events occurred, and what was the business impact?

---

## Domain 3 — Customisation & Schema

**Core questions**
1. How many custom objects and custom fields exist in the org?
2. Are any objects approaching the 500 custom field limit?
3. What percentage of standard Salesforce functionality is unused while custom solutions replicate it?
4. How many formula fields and roll-up summary fields exist?

**Probe questions**
- How many custom fields have less than 5% population rate across records?
- Are any objects at or near the two-parent master-detail limit?
- Are there lookup relationship chains creating cross-object query performance concerns?
- How many picklist fields have overlapping or redundant value sets?
- Which custom objects have had no activity in the last 90 days?
- Has a schema review or field audit been performed in the past 12 months?

---

## Domain 4 — Technical Debt

**Core questions**
1. What API versions are in use across Apex classes, triggers, and integrations?
2. Are Workflow Rules or Process Builders still in use that should be migrated to Flow?
3. What managed and unmanaged packages are installed, and are any versions outdated or unsupported?
4. Are there Visualforce pages, JavaScript buttons, or s-controls still in use?

**Probe questions**
- How many API calls use deprecated versions older than the three most recent Salesforce releases?
- Are there Apex classes or triggers with hardcoded IDs, record type names, URLs, or credentials?
- Are there Flash-based components or features on Salesforce's retirement roadmap?
- Is there custom code that bypasses platform features (e.g. non-bulkified triggers, direct SOQL in loops)?
- What is the estimated remediation effort in story points or days for identified technical debt?
- Are there unmanaged packages from inactive vendors or with no available updates?

---

## Domain 5 — Security Model

**Core questions**
1. What are the Organisation-Wide Default (OWD) settings for key standard and custom objects?
2. How many profiles and permission sets exist, and is there significant permission overlap?
3. What percentage of users hold View All Data, Modify All Data, or full System Administrator permissions?
4. When was the last comprehensive security audit, and are there unresolved findings?

**Probe questions**
- How many sharing rules exist and what is the business justification for each?
- Are field-level security settings consistently applied across profiles and permission sets?
- How many users have View All or Modify All permissions on objects containing sensitive data?
- Are public groups, queues, and territories actively maintained and audited?
- Are there manual sharing records that should be automated through sharing rules or Apex sharing?
- Can current access levels be traced back to documented business requirements?

---

## Domain 6 — Integrations

**Core questions**
1. What is the complete inventory of systems integrated with Salesforce, inbound and outbound?
2. What authentication methods are in use — OAuth, Named Credentials, basic auth, session IDs, API tokens?
3. What middleware or integration platforms are deployed (MuleSoft, Dell Boomi, Informatica, Azure Logic Apps, custom)?
4. What error handling and retry logic exists at each integration point?

**Probe questions**
- Are any integrations still using basic authentication or username/session-based tokens?
- Which integrations consume the most API calls daily, and are any approaching limit thresholds?
- Where are integration credentials stored — Named Credentials, Protected Custom Settings, or hardcoded?
- What logging and monitoring covers integration success and failure rates?
- Is there a change management process for when external system APIs are updated or deprecated?
- Are there point-to-point integrations that would benefit from being routed through an integration hub?
- How is data field mapping documented between Salesforce and connected systems?

---

## Domain 7 — Apex & Test Quality

**Core questions**
1. What is the overall Apex test coverage percentage for the org?
2. How many Apex classes and triggers have individual coverage below 75%?
3. Are there any Apex classes or triggers with zero coverage?
4. What error handling patterns exist in production code?

**Probe questions**
- What proportion of test methods use real assertions versus simply executing code for coverage metrics?
- Are any test classes using @SeeAllData=true, creating dependencies on live org data?
- Are test data factories or utility classes in use, or is test data created ad hoc?
- How many Apex classes rely on System.debug for logging rather than a proper framework?
- Are there slow-running test classes that extend deployment windows?
- Do Apex classes include exception handling for governor limit breach scenarios?

---

## Domain 8 — Release Management

**Core questions**
1. What deployment methodology is in use — change sets, SFDX, a DevOps platform (Copado, Gearset, AutoRABIT)?
2. How many sandboxes exist and what is the purpose of each?
3. What is the typical deployment frequency and are release windows formally defined?
4. Are rollback procedures documented and have they been tested in the last 12 months?

**Probe questions**
- When were sandboxes last refreshed from production, and what is the refresh schedule?
- Is version control in use, and if so what branching strategy is followed?
- What pre-deployment validation steps and automated tests run before a production release?
- What stakeholder approval gates exist — CAB review, business owner sign-off?
- How are emergency hotfixes handled differently from the standard release track?
- How is deployment success defined and validated post-release?

---

## Domain 9 — Monitoring & Alerting

**Core questions**
1. What monitoring tools are in use — Event Monitoring, third-party APM, custom dashboards?
2. Are automated alerts configured for governor limit warnings or critical errors?
3. How are batch job and integration failures detected and communicated to technical teams?
4. What SLAs exist for system availability and response times?

**Probe questions**
- Is API consumption tracked in real time or near-real time?
- Are there login forensics or security monitoring tools detecting unusual access patterns?
- Are synthetic health checks running against critical business processes?
- How are bulk data load failures detected and remediated?
- What is the log retention period, and where are logs stored?
- How is system performance tracked over time — page load times, SOQL execution, transaction durations?

---

## Domain 10 — Documentation

**Core questions**
1. Does a comprehensive data dictionary exist covering all custom objects and fields?
2. Are process flow diagrams maintained for critical business processes?
3. When was documentation last updated, and who owns it?
4. Where is documentation stored and how discoverable is it for new team members?

**Probe questions**
- Do integration architecture diagrams exist covering all system connections and data flows?
- Are technical runbooks available for common administrative tasks — user provisioning, data loads, deployments?
- Does API documentation exist for any custom REST or SOAP services exposed by Salesforce?
- Are configuration changes logged with business justification and change request references?
- What knowledge management system or wiki is in use?
- Are troubleshooting guides available for common error scenarios?

---

## Domain 11 — Compliance & Regulatory

**Core questions**
1. What regulatory frameworks apply — GDPR / UK GDPR, HIPAA, SOX, CCPA, PCI-DSS, NHS DSP Toolkit, Cyber Essentials?
2. What PII or sensitive data is stored in Salesforce, and is it classified or field-tagged?
3. What data encryption is deployed — Platform Encryption, Shield Platform Encryption, encryption at rest?
4. When was the last compliance audit and what findings remain unresolved?

**Probe questions**
- Are data subject rights implemented — access, rectification, erasure, portability?
- Are audit trails configured to satisfy regulatory requirements for data access and modification tracking?
- Do data retention policies align with regulatory minimisation requirements?
- Are there automated processes to fulfil data deletion requests within required timeframes?
- What cross-border data transfer mechanisms are in place — Standard Contractual Clauses, data localisation?
- How are third-party apps and integrations assessed for compliance with applicable regulations?
- What is the remediation timeline for any compliance gaps identified in the most recent audit?

---

## Domain 12 — Disaster Recovery & Business Continuity

**Core questions**
1. Which business processes would immediately cease if Salesforce became unavailable?
2. What are the defined Recovery Time Objective (RTO) and Recovery Point Objective (RPO)?
3. What backup solutions are in use — native Salesforce weekly export, OwnBackup, Veeam, Spanning?
4. When was the disaster recovery plan last tested — tabletop exercise or live drill?

**Probe questions**
- Is a documented DR plan specific to Salesforce in place, and who owns it?
- What is the process for restoring deleted records, and what is the recovery window?
- Are there alternative processes or systems that can handle critical functions during an outage?
- What is the stakeholder and customer communication plan for a service disruption?
- Are dependencies between Salesforce and other business-critical systems formally mapped?
- What are the contractual SLA terms with Salesforce, and what is the escalation process for P1 outages?

---

## Domain 13 — Innovation & AI Readiness

**Core questions**
1. What Einstein or AI features are currently enabled — Einstein Analytics, Prediction Builder, Einstein GPT, Agentforce?
2. What manual or repetitive processes exist that could be automated through Flow, AI, or Agentforce agents?
3. Is the organisation's data quality sufficient to support AI-driven features — completeness, consistency, accuracy?
4. What is the leadership appetite for AI adoption, and are there specific business outcomes being targeted?

**Probe questions**
- Has Data Cloud been evaluated or deployed for unified customer data?
- Are there use cases where autonomous agents (Agentforce) could reduce operational cost or improve service?
- What Einstein Copilot or generative AI features have been trialled?
- Are there self-service or Experience Cloud portal opportunities that could deflect volume from human teams?
- What competitor or industry peer AI deployments have been observed?
- What IBM AI or watsonx capabilities could complement Salesforce's native AI?
- What data governance controls would need to be in place before AI features can be safely deployed?
