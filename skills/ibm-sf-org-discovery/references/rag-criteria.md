# RAG Status Criteria

Apply one RAG status to each domain after completing its questions.
Use the criteria below. When in doubt, err towards the more severe rating.

---

## 🔴 Red — Critical Risk

Assign Red when **any** of the following are true:

**Licensing & Edition**
- Licences within 10% of cap with no procurement process initiated
- Add-on products purchased but with near-zero utilisation and renewal imminent
- Edition limitations actively blocking a live business requirement

**Data & Storage**
- Data or file storage above 85% with no archiving plan
- Governor limit exhaustion events have occurred in the last 90 days
- No data retention policy exists for a regulated org

**Technical Debt**
- Apex classes or triggers in active use with zero test coverage
- Hardcoded credentials in production code
- Features on Salesforce's active retirement list with no migration plan

**Security Model**
- More than 10% of users hold System Administrator or Modify All Data
- No security audit in the last 24 months
- OWDs set to Public Read/Write on objects containing sensitive data

**Integrations**
- Basic authentication or hardcoded session IDs in active integrations
- No error handling or retry logic on a business-critical integration
- Credentials stored in plaintext custom fields or code

**Apex & Test Quality**
- Overall org test coverage below 75% (Salesforce deployment threshold)
- Production deployments failing due to test failures in the last 30 days

**Release Management**
- No sandbox strategy — all development done directly in production
- No rollback procedure documented or tested

**Compliance & Regulatory**
- PII stored without encryption in a regulated org
- Data subject rights (GDPR erasure/access) not implemented
- Unresolved high findings from a compliance audit older than 6 months

**Disaster Recovery**
- No DR plan exists
- No backup solution beyond Salesforce weekly export
- RTO / RPO undefined for a business-critical org

---

## 🟡 Amber — Elevated Risk

Assign Amber when risks are present but not immediately critical:

- Known gaps with a remediation plan and owner identified
- Storage between 60–85% with a monitoring process in place
- Test coverage between 75–85% with improvement work in progress
- Technical debt present but not in active deployment paths
- Security model functional but not formally audited in 12–24 months
- Integration authentication adequate but not best practice (e.g. API tokens instead of OAuth)
- Documentation exists but is out of date or incomplete
- DR plan exists but has not been tested in the last 12 months
- Compliance gaps identified with a tracked remediation timeline

---

## 🟢 Green — Low Risk / Well Managed

Assign Green when:

- Controls are in place, documented, and recently reviewed
- No active governor limit warnings or exhaustion events
- Test coverage above 85% with meaningful assertions
- Security audit completed within 12 months with findings resolved
- DR plan tested within 12 months
- Compliance requirements fully implemented with audit evidence
- Documentation current and accessible to the team

---

## Scoring Summary

After all domains, count Red / Amber / Green.

| Profile | Interpretation |
|---------|---------------|
| 3+ Red | High-risk org — immediate remediation required before new project work |
| 1–2 Red, 3+ Amber | Significant debt — risk register and remediation plan must precede delivery |
| All Amber, 0 Red | Manageable debt — address in parallel with delivery |
| Mostly Green | Healthy org — focus on innovation and optimisation |
