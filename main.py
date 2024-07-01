import logging
from src.fetch import fetch_data
from src.scrape import scrape_data
from src.utils import load_config
import os
import pandas as pd
logging.basicConfig(filename='logging_info/app.log',filemode='a',level=logging.INFO)

import traceback

def main():
    # Load config
    config = load_config()

    #iterate over the data sources
    for data_source in config['data_sources']:
        try:
            url = data_source.get('url') or data_source.get('api_url')
            if not url:
                logging.error(f"Data source does not contain a 'url' or 'api_url' key: {data_source}")
                continue

            if data_source['type'] == 'fetch':
                logging.info(f"Fetching data from {url}")
                data = fetch_data(url)

                # Convert the data to a DataFrame
                data = pd.DataFrame(data)

                # Ensure the directory exists before saving the file
                os.makedirs(os.path.dirname(f"data/json/{data_source['name'].replace(' ', '_').lower()}.json"), exist_ok=True)

                # Save the data to a JSON file
                data.to_json(f"data/json/{data_source['name'].replace(' ', '_').lower()}.json", orient='records')
                logging.info(f"Successfully collected data for {data_source['name']}")

            elif data_source['type'] == 'scrape':
                logging.info(f"Scraping data from {url}")
                data = scrape_data(url, data_source['target_element'])

                # Ensure the directory exists before saving the file
                os.makedirs(os.path.dirname(f"data/csv/{data_source['name'].replace(' ', '_').lower()}.csv"), exist_ok=True)

                # Save the data to a CSV file
                data.to_csv(f"data/csv/{data_source['name'].replace(' ', '_').lower()}.csv", index=False)
                logging.info(f"Successfully collected data for {data_source['name']}")

            else:
                logging.error(f"Data source type {data_source['type']} not supported")

        except Exception as e:
            logging.error(f"Error processing data source {url}: {type(e).__name__} - {str(e)}\n{traceback.format_exc()}")

if __name__ == '__main__':
    main()