# Data Model Considerations

Comprehensive analysis framework for mapping user stories to Salesforce data models.

## Core Questions

### Entity Identification

**Standard vs Custom Objects:**
- What primary business entities exist in user stories?
- Which map to standard objects (Account, Contact, Case, Lead, Opportunity)?
- Which require custom objects?
- Can standard objects be extended with custom fields?

**Object Selection Criteria:**
| Scenario | Standard Object | Custom Object |
|----------|----------------|---------------|
| Core CRM entity | Account, Contact, Lead | N/A |
| Sales process | Opportunity, Quote | N/A |
| Service process | Case, Entitlement | N/A |
| Industry-specific | Check AppExchange | Consider custom |
| Unique business entity | Extend standard if close fit | Create custom |

### Relationship Cardinality

**One-to-Many:**
- Master-Detail: Parent controls child lifecycle, roll-up summaries needed
- Lookup: Independent child records, more flexible

**Many-to-Many:**
- Junction objects required
- Example: Contact-to-Multiple-Accounts via AccountContactRelation

**Considerations:**
- Does parent deletion require child deletion? → Master-Detail
- Are roll-up summaries needed? → Master-Detail (max 2 levels)
- Do children need independent sharing? → Lookup
- Does relationship cross org boundaries? → External Lookup

### Field Types and Validation

**Field Type Selection:**
```
Text → Short text (255), Long text (131,072), Rich text
Number → Number, Currency, Percent
Date/Time → Date, DateTime, Time
Relationship → Lookup, Master-Detail, External Lookup
Picklist → Standard, Multi-select, Global value sets
Boolean → Checkbox
Complex → Formula, Roll-up Summary, Geolocation
```

**Validation Rules:**
- Email format: RFC 5322 validation
- Phone format: Country-specific patterns
- Date ranges: Start date < End date
- Required field combinations: IF conditions
- Business logic: Cross-field validation

**Picklist Values:**
- Standard values for common fields (Status, Priority, Category)
- Global value sets for reused picklists across objects
- Controlling/dependent picklists for dynamic options
- Inactive values for legacy data

### Data Volume Planning

**Current Volumes:**
- Records per object
- Storage consumption (data + file)
- Transaction volumes (creates, updates, queries per day)

**Growth Projections:**
```
Year 1: Baseline + X% growth
Year 3: 3-year projection
Year 5: Strategic planning horizon

LDV Threshold: 1M records per object
```

**Impact Analysis:**
| Volume Range | Considerations | Solutions |
|--------------|----------------|-----------|
| <100K | Standard approach | N/A |
| 100K-1M | Monitor query performance | Add custom indexes |
| 1M-10M | LDV strategies | Skinny tables, archival |
| >10M | External data | BigObjects, external objects |

### Record Types and Page Layouts

**When to Use Record Types:**
- Multiple business processes on same object
- Different picklist values per process
- Different page layouts per user segment
- Different validation rules per process

**Page Layout Strategy:**
| Persona | Fields Visible | Field Order | Sections |
|---------|---------------|-------------|----------|
| Sales Rep | Core + Sales | Sales-focused | Opportunity details |
| Service Agent | Core + Service | Service-focused | Case management |
| Manager | All | Strategic view | Analytics |

**Considerations:**
- Limit record types to avoid complexity (<10 per object)
- Use field-level security over hidden fields on layouts
- Consider Lightning page assignments over record type layouts

### Sharing Model

**Organisation-Wide Defaults (OWD):**
```
Private → Most restrictive, explicit sharing required
Public Read Only → View access, edit requires sharing
Public Read/Write → Open access, use with caution
Controlled by Parent → Master-detail relationship
```

**Sharing Rules:**
- Criteria-based: Share records matching criteria
- Ownership-based: Share records owned by role/group

**Manual Sharing:**
- Apex Managed Sharing: Programmatic sharing logic
- Manual sharing buttons: Ad-hoc user sharing

**Decision Framework:**
1. Start with most restrictive OWD
2. Open access via sharing rules
3. Use manual sharing for exceptions
4. Monitor sharing calculation performance

### Data Quality and Integrity

**Duplicate Management:**
- Standard duplicate rules: Account, Contact, Lead
- Custom duplicate rules: Custom objects
- Matching rules: Fuzzy matching, exact matching

**Data Retention:**
- Legal hold requirements
- Archival strategy for old data (>2 years)
- Hard delete vs soft delete (IsDeleted flag)

**Data Migration Considerations:**
- Source system data quality audit
- Transformation rules
- Lookup ID mapping
- Data validation scripts
- Rollback plan

### Object Relationships Best Practices

**Relationship Limits:**
- Max 40 Master-Detail relationships per object
- Max 2 Master-Detail relationships per child
- No Master-Detail on custom objects in managed packages

**Performance Considerations:**
- Deep relationship queries (5+ levels) impact performance
- Polymorphic lookups (WhatId, WhoId) limit reporting
- Self-referential relationships require careful design

**Relationship Patterns:**
```
Account → Contact (Standard 1:M Lookup)
Opportunity → Product (M:M via OpportunityLineItem)
Case → Account (1:M Lookup)
Custom Object → User (Lookup for ownership, not Master-Detail)
```

### External Objects and Integration

**When to Use External Objects:**
- Very large datasets (>50M records)
- Data resides in external system
- Real-time data access without storage
- Infrequent access patterns

**External Object Limitations:**
- No triggers
- Limited query capabilities
- No roll-up summaries
- Requires Salesforce Connect

**Integration Data Model:**
- External IDs for matching records
- Upsert operations require external ID
- Composite keys via formula fields

### Custom Metadata Types

**Use Cases:**
- Configuration data accessible across environments
- Application settings and feature flags
- Mapping tables for integration
- Business rule configuration

**Advantages:**
- Deployable via metadata API (included in change sets)
- No SOQL query governor limits
- Packageable for AppExchange
- Protected custom settings alternative

**Example Use Case:**
```
Custom Metadata Type: Integration_Endpoint__mdt

Purpose: Store integration configuration per environment
Fields: Endpoint_URL__c, Auth_Type__c, Timeout__c, Retry_Count__c
Benefit: Update endpoints without code deployment, different values per sandbox/production
```

## Data Model Documentation Template

```markdown
### Object: [Object_API_Name__c]

**Purpose:** [Business entity description]

**Deployment:** Custom / Standard Extended

**Sharing Model:** Private / Public Read / Public Read/Write

**Record Types:** [List record types if applicable]

#### Fields

| Field API Name | Type | Length | Required | Description |
|----------------|------|--------|----------|-------------|
| Field1__c | Text | 255 | Yes | [Description] |
| Field2__c | Lookup(Account) | - | No | [Description] |

#### Relationships

| Relationship | Type | Related Object | Cascade Delete | Description |
|--------------|------|----------------|----------------|-------------|
| Parent__c | Master-Detail | Parent__c | Yes | [Description] |

#### Validation Rules

| Rule Name | Formula | Error Message |
|-----------|---------|---------------|
| VR_Required_Fields | ISBLANK(Field1__c) | Field 1 is required |

#### Security

- OWD: Private
- Criteria-based sharing: Share with Support team where Status='Open'
- Profile access: System Admin (Full), Service Agent (Read/Edit)
```