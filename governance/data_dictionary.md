# Enterprise Customer Data Platform – Data Dictionary

This document defines the standardized data elements used across the
Enterprise Customer Data Platform (CDP).  
It ensures **data consistency, shared understanding, and governance compliance**
across ingestion, processing, analytics, and reporting layers.

---

## Customer Master Dataset

### Table: `customer_master`
**Layer:** Silver  
**Description:**  
Consolidated and deduplicated customer profile created by integrating CRM
and marketing data sources.

| Column Name   | Data Type | Description |
|--------------|----------|-------------|
| customer_id  | String   | Unique customer identifier sourced from CRM or generated during ingestion |
| email        | String   | Primary customer email address used for identity resolution |
| first_name   | String   | Customer first name (if available) |
| last_name    | String   | Customer last name (if available) |
| source_system| String   | Originating system (CRM or Marketing) |
| created_date | Date     | Record creation date |

---

## Marketing Engagement Dataset

### Table: `marketing_engagement`
**Layer:** Bronze / Silver  
**Description:**  
Raw and cleaned marketing interaction data captured from campaign platforms.

| Column Name | Data Type | Description |
|------------|----------|-------------|
| campaign   | String   | Marketing campaign name or identifier |
| clicks     | Integer  | Number of user interactions (clicks) |
| email      | String   | Customer email associated with the campaign |
| event_date | Date     | Date of marketing interaction |

---

## Analytics & Aggregated Metrics

### Table: `customer_360_metrics`
**Layer:** Gold  
**Description:**  
Aggregated dataset used for dashboards and business reporting.

| Column Name     | Data Type | Description |
|----------------|----------|-------------|
| customer_id    | String   | Unique customer identifier |
| total_clicks   | Integer  | Total marketing clicks across all campaigns |
| active_campaigns | Integer | Count of campaigns the customer interacted with |
| last_activity_date | Date | Most recent engagement date |

---

## Data Governance Notes

- **Email** is treated as a sensitive identifier and protected via role-based access.
- Customer identifiers are standardized across all datasets.
- Aggregated datasets do not expose PII to business users.
- Invalid or malformed records are quarantined before reaching Silver layer.

---

## Ownership & Maintenance

- **Data Owner:** Marketing & CRM Teams
- **Data Steward:** Data Engineering Team
- **Review Cycle:** Quarterly

---

**Last Updated:** 2026
