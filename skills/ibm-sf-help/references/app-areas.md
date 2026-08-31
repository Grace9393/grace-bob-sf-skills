# Salesforce Help App Areas Reference

Unique `app_area` values from `entries_fts` table. The database stores semicolon-delimited values; this list shows individual app areas after splitting.

## Usage

## App Areas (104 unique values)

### Core Clouds
| App Area | Description |
|----------|-------------|
| `Sales_Cloud` | Sales automation and CRM |
| `Service_Cloud` | Customer service and support |
| `Experience_Cloud` | Digital experiences and portals |
| `Marketing_Cloud` | Marketing automation |
| `Commerce` | Commerce Cloud |
| `B2B_Commerce` | Business-to-business commerce |
| `B2B2C_Commerce` | Hybrid commerce model |
| `B2C_Commerce` | Business-to-consumer commerce |
| `Revenue_Cloud` | CPQ and billing |

### Industry Clouds
| App Area | Description |
|----------|-------------|
| `Financial_Services_Cloud` | Banking, insurance, wealth management |
| `Financial_Services` | FSC features |
| `Healthcare` | Health Cloud |
| `Health1` | Health Cloud variant |
| `Manufacturing_Cloud` | Manufacturing operations |
| `Manufacturing` | Manufacturing variant |
| `Consumer_Goods_Cloud` | Consumer goods industry |
| `Consumer` | Consumer goods variant |
| `Goods` | Consumer goods variant |
| `Automotive_Cloud` | Automotive industry |
| `Education_Cloud` | Education sector |
| `Nonprofit_Cloud` | Nonprofit organisations |
| `Public_Sector_Cloud` | Government sector |
| `Public_Sector_Solutions` | Government solutions |
| `Net_Zero_Cloud` | Sustainability tracking |
| `Sustainability_Cloud` | Environmental sustainability |
| `Wealth1` | Wealth management |

### Einstein & AI
| App Area | Description |
|----------|-------------|
| `Einstein` | AI and machine learning features |
| `einstein` | Einstein (lowercase variant) |
| `Einstein_CC` | Einstein for Commerce Cloud |
| `Sales_Cloud_Einstein` | Einstein for Sales |
| `Industries_Einstein` | Einstein for Industry Clouds |

### Analytics & Reporting
| App Area | Description |
|----------|-------------|
| `Analytics` | Salesforce analytics |
| `Analytics_CC` | Analytics for Commerce Cloud |
| `CRM_Analytics` | CRM Analytics (formerly Tableau CRM) |
| `Tableau` | Tableau integration |
| `Reports` | Standard reporting |
| `Wave_Build_Dashboards` | Analytics dashboard builder |
| `Wave_Setup_Security` | Analytics security |

### Platform & Development
| App Area | Description |
|----------|-------------|
| `Salesforce_Platform` | Core platform features |
| `Apex` | Apex programming language |
| `Apex_Code_Development_Deployment` | Apex development |
| `API_Integration_Performance` | API and integrations |
| `SOAP_API` | SOAP API |
| `api` | API (lowercase variant) |
| `Application_Development` | App development |
| `Developer_Tools` | Developer tools |
| `Lightning_App_Builder` | Lightning app builder |

### Service & Field
| App Area | Description |
|----------|-------------|
| `Service_Support` | Service support features |
| `Field_Service` | Field Service Lightning |
| `Knowledge` | Knowledge base |
| `Knowledge_Management` | Knowledge management |
| `Articles` | Knowledge articles |

### Collaboration & Mobile
| App Area | Description |
|----------|-------------|
| `Slack` | Slack integration |
| `Slack_Apps` | Slack applications |
| `Apps` | Applications |
| `Mobile` | Salesforce Mobile |
| `Salesforce_Mobile_App` | Mobile app |
| `Communities` | Communities (legacy Experience Cloud) |
| `Portal_Sites` | Portal sites |

### Marketing & Engagement
| App Area | Description |
|----------|-------------|
| `Pardot_Marketing` | Pardot marketing automation |
| `Account_Engagement` | Account Engagement (Pardot) |
| `Engagement` | Marketing engagement |
| `Referral_Marketing` | Referral marketing |
| `Email_Templates` | Email templates |

### Loyalty & Rebates
| App Area | Description |
|----------|-------------|
| `Loyalty_Management` | Loyalty programmes |
| `Loyalty_Mangement` | Loyalty (typo in source) |
| `Rebate_Management` | Rebate management |
| `Rebate_Mangement_Cloud` | Rebate (typo in source) |
| `Rebate` | Rebate features |
| `Management` | Management variant |

### Data & Processing
| App Area | Description |
|----------|-------------|
| `Data_Management` | Data management |
| `Data_Processing_Engine` | Data processing |
| `Customer_Data_Cloud` | CDP |
| `Batch_Management` | Batch processing |
| `Batch` | Batch processing variant |

### Customer 360
| App Area | Description |
|----------|-------------|
| `c360` | Customer 360 |
| `c360_aud` | Customer 360 Audiences |
| `activation_c360_aud` | C360 activation |
| `experiences_c360` | C360 experiences |
| `segments_c360_aud` | C360 segments |

### Security & Admin
| App Area | Description |
|----------|-------------|
| `Security` | Security features |
| `Setup_Security` | Setup and security |
| `Sharing_Visibility` | Sharing and visibility rules |
| `Feature_Activation` | Feature activation |

### UI & Content
| App Area | Description |
|----------|-------------|
| `UI_Customization` | UI customisation |
| `Salesforce_CMS` | Content management |
| `Salesforce_Maps` | Mapping features |
| `Tasks_Calendars_Activities` | Productivity features |

### Editions
| App Area | Description |
|----------|-------------|
| `Essentials` | Essentials edition |
| `ME` | Micro edition |
| `GE` | Group edition |
| `PE` | Professional edition |
| `EE` | Enterprise edition |
| `PXE` | Performance edition |
| `UE` | Unlimited edition |
| `DE` | Developer edition |

### Other
| App Area | Description |
|----------|-------------|
| `Cross_Cloud` | Cross-cloud features |
| `Cross_Cloud_Packages_Solutions` | Cross-cloud packages |
| `Cross_Cloud_Products` | Cross-cloud products |
| `Industries` | Industry clouds general |
| `General_Salesforce_Functionality` | Core functionality |
| `Salesforce_Pricing` | Pricing information |
| `Product_Catalog_Management` | Product catalogue |
| `Cloud` | Generic cloud reference |
| `None` | No specific area |

## Common Filter Patterns

### By Cloud Product
```bash
# Sales Cloud
WHERE app_area LIKE '%Sales_Cloud%'

# Service Cloud
WHERE app_area LIKE '%Service_Cloud%'

# Experience Cloud (includes legacy Communities)
WHERE app_area LIKE '%Experience_Cloud%' OR app_area LIKE '%Communities%'

# Marketing Cloud
WHERE app_area LIKE '%Marketing_Cloud%' OR app_area LIKE '%Pardot%' OR app_area LIKE '%Account_Engagement%'
```

### By Industry Cloud
```bash
# Financial Services
WHERE app_area LIKE '%Financial_Services%'

# Healthcare
WHERE app_area LIKE '%Health%'

# Manufacturing
WHERE app_area LIKE '%Manufacturing%'

# Public Sector
WHERE app_area LIKE '%Public_Sector%'
```

### By Feature Area
```bash
# Einstein/AI (case-insensitive matching)
WHERE app_area LIKE '%Einstein%' OR app_area LIKE '%einstein%'

# Slack
WHERE app_area LIKE '%Slack%'

# Analytics
WHERE app_area LIKE '%Analytics%' OR app_area LIKE '%CRM_Analytics%' OR app_area LIKE '%Tableau%'

# Development/API
WHERE app_area LIKE '%API%' OR app_area LIKE '%Apex%' OR app_area LIKE '%Developer%'
```

---
*Generated from `docs.sqlite` on 2026-01-30*
