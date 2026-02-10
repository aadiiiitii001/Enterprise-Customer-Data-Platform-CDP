from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def create_spark_session():
    return SparkSession.builder \
        .appName("CustomerDataQualityChecks") \
        .getOrCreate()

def load_customer_master(spark):
    input_path = "/mnt/silver/customer_master"
    return spark.read.parquet(input_path)

def identify_invalid_records(df):
    """
    Data quality rules:
    - Email must not be null
    - Email must contain '@'
    """
    invalid_df = df.filter(
        col("email").isNull() | ~col("email").contains("@")
    )
    return invalid_df

def quarantine_invalid_records(df):
    output_path = "/mnt/quarantine/invalid_customers"
    df.write \
        .mode("overwrite") \
        .parquet(output_path)

def run_quality_checks():
    spark = create_spark_session()
    customer_df = load_customer_master(spark)

    if customer_df.count() == 0:
        raise Exception("Customer master dataset is empty")

    invalid_df = identify_invalid_records(customer_df)

    if invalid_df.count() > 0:
        quarantine_invalid_records(invalid_df)
        print("Invalid records quarantined successfully")
    else:
        print("No data quality issues found")

if __name__ == "__main__":
    run_quality_checks()
