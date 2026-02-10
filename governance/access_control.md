# Access Control & Data Governance Strategy

This document outlines the role-based access control (RBAC) model implemented as part of the Enterprise Customer Data Platform (CDP).  
The objective is to ensure **data security, compliance, and least-privilege access** while enabling analytics and business insights.

---

## Access Control Principles

The CDP follows these governance principles:

- **Least Privilege**: Users are granted only the minimum access required.
- **Separation of Duties**: Data engineering, analytics, and business access are isolated.
- **Data Sensitivity Awareness**: Raw and curated layers have different access levels.
- **Auditability**: Access policies are clearly defined and reviewable.

---

## Role-Based Access Model

### 1. Marketing Team
**Access Level:** Read-only  
**Scope:** Curated analytics views

- Can query **Silver/Gold layer views** for campaign analysis
- No access to raw (Bronze) or personally sensitive datasets
- Cannot modify schemas or data

**Use Case:**
- Campaign performance analysis
- Customer segmentation insights

---

### 2. Data Engineering Team
**Access Level:** Full access  
**Scope:** All data layers and workflows

- Full read/write access to **Bronze, Silver, and Gold layers**
- Permission to manage ingestion pipelines, workflows, and schemas
- Responsible for data quality, deduplication, and pipeline reliability

**Use Case:**
- Data ingestion and transformation
- Master data management
- Governance enforcement

---

### 3. Business Users
**Access Level:** Restricted read-only  
**Scope:** Aggregated dashboards and reports

- Access limited to **pre-aggregated dashboards**
- No direct access to underlying tables or customer-level data
- Data is anonymized and aggregated where required

**Use Case:**
- Executive reporting
- KPI monitoring
- Strategic decision-making

---

## Data Layer Access Summary

| Data Layer | Marketing Team | Data Team | Business Users |
|-----------|---------------|-----------|----------------|
| Bronze (Raw) | ❌ No Access | ✅ Full Access | ❌ No Access |
| Silver (Cleaned) | ✅ Read | ✅ Full Access | ❌ No Access |
| Gold (Aggregated) | ✅ Read | ✅ Full Access | ✅ Read (Dashboards Only) |

---

## Governance Enforcement (Conceptual)

- Role-based permissions mapped to teams
- Sensitive attributes (PII) restricted to Data Team
- Invalid or non-compliant records quarantined
- Access policies reviewed periodically

---

## Future Enhancements

- Column-level security for PII fields
- Attribute-based access control (ABAC)
- Integration with enterprise IAM tools
- Automated access audits and alerts

---

**Owner:** Data Engineering Team  
**Last Updated:** 2026
