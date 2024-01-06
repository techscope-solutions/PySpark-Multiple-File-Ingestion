import pandas as pd

def process_csv(file_path):
    df = pd.read_csv(file_path)
    # Perform your processing here
    return df

def main():
    file_path = 'data/example_dataset.csv'
    processed_df = process_csv(file_path)
    processed_df.to_csv('data/processed_dataset.csv', index=False)

if __name__ == "__main__":
    main()
