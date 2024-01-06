from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def create_spark_session():
    return SparkSession.builder \
        .appName("Data Staging") \
        .getOrCreate()

def main():
    spark = create_spark_session()

    # Load and process data
    df = spark.read.csv('data/processed_dataset.csv', header=True, inferSchema=True)
    # Perform joins, filters, and transformations
    # Example: df = df.filter(df['column_name'] > value)

    # Save the staged data
    df.write.format("parquet").save("data/staged_data")

if __name__ == "__main__":
    main()
