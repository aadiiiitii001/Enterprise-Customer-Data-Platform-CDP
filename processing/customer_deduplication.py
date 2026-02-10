from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window

crm_df = spark.read.parquet("/mnt/bronze/crm")
mkt_df = spark.read.parquet("/mnt/bronze/marketing")

combined = crm_df.unionByName(mkt_df, allowMissingColumns=True)

windowSpec = Window.partitionBy("email").orderBy(col("customer_id"))

deduped = combined.withColumn(
    "row_num", row_number().over(windowSpec)
).filter(col("row_num") == 1).drop("row_num")

deduped.write.mode("overwrite").parquet("/mnt/silver/customer_master")
