from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

def create_spark_session():
    return SparkSession.builder \
        .appName("MarketingIngestion") \
        .getOrCreate()

def get_marketing_schema():
    return StructType([
        StructField("customer_id", StringType(), True),
        StructField("email", StringType(), True),
        StructField("campaign", StringType(), True),
        StructField("clicks", IntegerType(), True),
        StructField("source", StringType(), True)
    ])

def ingest_marketing_data(spark):
    input_path = "/mnt/raw/marketing/marketing.csv"
    output_path = "/mnt/bronze/marketing"

    schema = get_marketing_schema()

    df = spark.read \
        .option("header", True) \
        .schema(schema) \
        .csv(input_path)

    if df.count() == 0:
        raise Exception("Marketing source file is empty")

    df.write \
        .mode("overwrite") \
        .parquet(output_path)

    print("Marketing data ingestion completed successfully")

if __name__ == "__main__":
    spark = create_spark_session()
    ingest_marketing_data(spark)
