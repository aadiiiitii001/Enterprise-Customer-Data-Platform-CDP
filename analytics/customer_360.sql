CREATE OR REPLACE VIEW customer_360 AS
SELECT
    customer_id,
    email,
    campaign,
    clicks,
    source
FROM parquet.`/mnt/silver/customer_master`;
