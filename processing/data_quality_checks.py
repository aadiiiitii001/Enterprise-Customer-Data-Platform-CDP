from pyspark.sql.functions import col

df = spark.read.parquet("/mnt/silver/customer_master")

invalid_records = df.filter(
    col("email").isNull() | ~col("email").contains("@")
)

if invalid_records.count() > 0:
    invalid_records.write.mode("overwrite").parquet("/mnt/quarantine/invalid_customers")
