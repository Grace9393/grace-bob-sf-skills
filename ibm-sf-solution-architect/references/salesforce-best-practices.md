# Salesforce Architecture Best Practices

Quick reference for applying Salesforce best practices during solution architecture development.

## Apex Development Best Practices

**Bulkification:**
- Never perform DML operations inside loops
- Use collections (Lists, Sets, Maps) to batch operations
- Query records outside loops and process in bulk
- Example: `List<User> users = [SELECT Id FROM User WHERE ...]; insert users;`

**Trigger Framework:**
- One trigger per object
- Delegate logic to handler classes
- Use trigger context variables (Trigger.new, Trigger.old, etc.)
- Implement trigger bypass mechanisms via custom settings

**Exception Handling:**
- Try-catch blocks for external API calls
- Custom exception classes for business logic
- Log exceptions to custom object or Platform Events
- Provide user-friendly error messages

**Governor Limits:**
- 150 DML statements per transaction
- 100 SOQL queries per transaction
- 50,000 records retrieved by SOQL
- 10 callouts per transaction
- Use `@future` or Queueable Apex for async processing

## Security Best Practices

**Authentication:**
- Enforce MFA for all users
- Implement SSO where possible (SAML 2.0)
- Password policies: 12+ characters, complexity requirements, 90-day expiry
- Session timeout: 2 hours for community users, 4 hours for internal

**Authorisation:**
- Profile defines baseline permissions
- Permission sets for additional access
- Never modify standard profiles
- Use permission set groups for role-based access

**Data Security:**
- Organisation-Wide Defaults (OWD): Most restrictive setting
- Sharing rules for controlled opening
- Manual sharing for ad-hoc access
- Field-level security for sensitive data
- Never use `with sharing` keyword in trigger handlers (maintain system context)

**Encryption:**
- Platform Encryption for PII fields
- Shield Platform Encryption for HIPAA/GDPR compliance
- Encrypted fields cannot be used in filters, formulas, or unique constraints

## Integration Best Practices

**API Design:**
- REST APIs for modern integrations
- Named Credentials for authentication
- Implement retry logic with exponential backoff
- Use Bulk API for high-volume data (>2000 records)

**Asynchronous Processing:**
- Platform Events for event-driven architecture
- Change Data Capture for data synchronisation
- Queueable Apex for chained jobs
- Batch Apex for processing >50,000 records

**Error Handling:**
- Implement dead letter queue pattern
- Log integration errors to custom object
- Alert administrators on repeated failures
- Circuit breaker pattern for external system failures

## Performance Optimisation

**Query Optimisation:**
- Index frequently filtered fields
- Use selective queries (reduce records scanned)
- Avoid wildcard searches in production
- Use SOQL FOR loops for large datasets

**UI Performance:**
- Lightning Web Components over Aura
- Lazy loading for large datasets
- Client-side caching
- Minimise server-side calls

**Large Data Volumes (LDV):**
- Skinny tables for frequently accessed data
- Data archival strategy (>2 years old)
- BigObjects for historical data
- External objects for very large datasets

## Experience Cloud Best Practices

**Performance:**
- CDN for static resources
- Browser caching enabled
- Optimise image sizes (<200KB)
- Minimise custom CSS/JavaScript

**Security:**
- Guest user access restrictions
- Rate limiting enabled (1000 requests/hour/IP)
- Content Security Policy configured
- Regular security reviews

**Customisation:**
- Theme layouts for consistent branding
- Reusable components
- Navigation menu structure planning
- Mobile-responsive design

## Testing Best Practices

**Unit Testing:**
- Minimum 85% code coverage for production
- Test positive and negative scenarios
- Use Test.startTest() and Test.stopTest()
- Mock external callouts with HttpCalloutMock

**Integration Testing:**
- Test end-to-end workflows
- Verify error handling paths
- Test with realistic data volumes
- Include governor limit testing

## Data Management Best Practices

**Data Quality:**
- Validation rules for data integrity
- Duplicate management rules
- Required fields for core objects
- Picklist standardisation

**Data Migration:**
- Dry-run in sandbox environment
- Data cleansing before migration
- Maintain data lineage
- Rollback strategy

## Metadata Management

**Naming Conventions:**
- Custom Objects: PascalCase with __c suffix (Email_Verification__c)
- Custom Fields: Snake_case with __c suffix (verification_token__c)
- Apex Classes: PascalCase (EmailVerificationController)
- Apex Variables: camelCase (verificationToken)
- Flows: Descriptive with underscores (User_Registration_Flow)

**Change Management:**
- Version control for all metadata (Git)
- Sandbox progression: Dev → UAT → Full Copy → Production
- Automated deployments via CI/CD
- Release notes for each deployment

## Documentation Standards

**Code Documentation:**
- Class and method-level comments
- Inline comments for complex logic
- Parameter descriptions
- Return value documentation

**Architecture Documentation:**
- Keep diagrams current
- Document integration touchpoints
- Maintain data dictionary
- Update on each release