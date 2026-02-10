"""
Customer Deduplication & Master Data Creation
---------------------------------------------
This script merges CRM and Digital Marketing customer data,
applies deduplication logic using email as a business key,
and creates a standardized customer master dataset (silver layer).

Environment:
- PySpark / Databricks compatible
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window

def create_spark_session():
    return SparkSession.builder \
        .appName("CustomerDeduplication") \
        .getOrCreate()

def load_source_data(spark):
    crm_path = "/mnt/bronze/crm"
    marketing_path = "/mnt/bronze/marketing"

    crm_df = spark.read.parquet(crm_path)
    marketing_df = spark.read.parquet(marketing_path)

    return crm_df, marketing_df

def deduplicate_customers(crm_df, marketing_df):
    # Combine CRM and marketing datasets
    combined_df = crm_df.unionByName(
        marketing_df,
        allowMissingColumns=True
    )

    # Window specification for deduplication
    window_spec = Window.partitionBy("email").orderBy(col("customer_id"))

    deduped_df = combined_df.withColumn(
        "row_num", row_number().over(window_spec)
    ).filter(col("row_num") == 1).drop("row_num")

    return deduped_df

def write_customer_master(df):
    output_path = "/mnt/silver/customer_master"

    if df.count() == 0:
        raise Exception("Customer master dataset is empty after deduplication")

    df.write \
        .mode("overwrite") \
        .parquet(output_path)

    print("Customer master dataset created successfully")

if __name__ == "__main__":
    spark = create_spark_session()

    crm_df, marketing_df = load_source_data(spark)
    customer_master_df = deduplicate_customers(crm_df, marketing_df)
    write_customer_master(customer_master_df)
