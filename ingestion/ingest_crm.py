df = spark.read.option("header", True).csv("/mnt/raw/crm/customers.csv")

df.write.mode("overwrite").parquet("/mnt/bronze/crm")
