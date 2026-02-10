-- =========================================================
-- Customer 360 Analytical View
-- =========================================================
-- Purpose:
-- Provides a unified, analytics-ready customer profile
-- combining identity and engagement metrics.
--
-- Layer: Gold
-- Consumers: Marketing, Business, Leadership
-- =========================================================

CREATE OR REPLACE VIEW customer_360 AS
SELECT
    customer_id,
    email,

    -- Engagement metrics
    COUNT(DISTINCT campaign)       AS active_campaigns,
    SUM(clicks)                    AS total_clicks,

    -- Activity tracking
    MAX(event_date)                AS last_engagement_date,

    -- Data lineage
    source_system                  AS source

FROM parquet.`/mnt/silver/customer_master`

GROUP BY
    customer_id,
    email,
    source_system;
