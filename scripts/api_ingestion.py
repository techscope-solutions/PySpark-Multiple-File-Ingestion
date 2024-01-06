import requests
import pandas as pd

def fetch_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

def main():
    api_url = "https://example.com/api/customer_feedback"
    data = fetch_api_data(api_url)
    df = pd.DataFrame(data)
    df.to_csv('data/api_data.csv', index=False)

if __name__ == "__main__":
    main()
