"""
CRM Customer Data Ingestion Script
----------------------------------
Ingests customer master data from CRM source files
and writes it to the Data Lake bronze layer.

Environment:
- PySpark / Databricks compatible
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

def create_spark_session():
    return SparkSession.builder \
        .appName("CRMIngestion") \
        .getOrCreate()

def get_crm_schema():
    return StructType([
        StructField("customer_id", StringType(), True),
        StructField("email", StringType(), True),
        StructField("first_name", StringType(), True),
        StructField("last_name", StringType(), True),
        StructField("phone", StringType(), True)
    ])

def ingest_crm_data(spark):
    input_path = "/mnt/raw/crm/customers.csv"
    output_path = "/mnt/bronze/crm"

    schema = get_crm_schema()

    df = spark.read \
        .option("header", True) \
        .schema(schema) \
        .csv(input_path)

    if df.count() == 0:
        raise Exception("CRM source file is empty")

    df.write \
        .mode("overwrite") \
        .parquet(output_path)

    print("CRM data ingestion completed successfully")

if __name__ == "__main__":
    spark = create_spark_session()
    ingest_crm_data(spark)
