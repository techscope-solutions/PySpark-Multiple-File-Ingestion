# PySpark-Multiple-File-Ingestion
This repo outlines a framework we have used in the past to create a unified data ingestion/consumption strategy.


Project Overview:
This project aims to analyze customer purchasing patterns and sales data to optimize business strategies. The analysis covers data collection, processing, and insight generation, utilizing technologies like SQL, Python, Apache Spark, and GCP BigQuery.

Key Objectives:

Aggregate diverse data sources.
Perform exploratory data analysis and advanced analytics.
Generate actionable business insights.

Data Sources:
  CSV File: Sample customer purchase data.
  Mock API: Simulated customer feedback data.
  SQL Tables: Sales records and inventory data.
  Data Ingestion and Processing Workflow:

Data Ingestion:
  Sqoop: Used for importing data from SQL tables.
  Python Scripts: For API data ingestion and CSV file processing.
  SharePoint Directory: Storing and retrieving the flat files.


Data Staging:
  Schema Standardization: Aligning data from all sources to a common schema.
  PySpark: Employed for complex data transformations, joins, and filters.

Data Loading:
  GCP BigQuery: Final transformed data is loaded into a BigQuery table for analysis and reporting.

Script Descriptions:
  sqoop_import.sh: Script to import data from SQL databases using Sqoop.
  api_ingestion.py: Python script for retrieving data from a mock API.
  csv_processor.py: Script for processing CSV files from SharePoint.
  data_staging.py: PySpark script for data transformation and staging.
  bigquery_loader.py: Script to load the data into GCP BigQuery.

Example DataSet:
  example_dataset.csv: A sample CSV file containing mock customer purchase data.

Mock API Details:
  Endpoint: https://example.com/api/customer_feedback
  Method: GET
  Data Format: JSON

SQL Table Structure:
  Sales Table: Columns include SaleID, ProductID, Quantity, SaleDate, etc.
  Inventory Table: Columns include ProductID, StockLevel, ReorderLevel, etc.

Usage Instructions:
  Set up the environment and install dependencies.
  Run the ingestion scripts to load data into the staging area.
  Execute the PySpark script for data transformation.
  Load the transformed data into BigQuery using the provided script.


Contribution Guidelines:
  Fork the repository.
  Make changes or additions.
  Submit a pull request with a clear description of the modifications.
