from google.cloud import bigquery

def load_to_bigquery(source_file, dataset_id, table_id):
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.PARQUET
    job_config.autodetect = True

    with open(source_file, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

    job.result()  # Waits for the job to complete

def main():
    source_file = "data/staged_data"
    dataset_id = 'your_dataset_id'
    table_id = 'your_table_id'
    load_to_bigquery(source_file, dataset_id, table_id)

if __name__ == "__main__":
    main()
