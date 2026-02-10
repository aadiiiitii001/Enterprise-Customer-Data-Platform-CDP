from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MarketingIngestion").getOrCreate()

df = spark.read.option("header", True).csv("/mnt/raw/marketing/marketing.csv")

df.write.mode("overwrite").parquet("/mnt/bronze/marketing")
