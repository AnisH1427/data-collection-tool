# Agritech Data Collection Tool

## Project Description

This project is a data collection tool designed to fetch and scrape data from various sources, such as APIs and web pages. The collected data is then saved to json and CSV files for further analysis. The tool is built using Python, leveraging the `requests` and `beautifulsoup4` libraries for data retrieval and parsing.

## Data 

### Data1: USDA's Corn Production of Vergenia
  - **Source**: USDA's Quick Stats API
  - **Description**: This data source fetches the corn production data for the state of Virginia from the USDA's Quick Stats API. The data includes information such as the year, state, and corn production in bushels.
  - **Data Fields**:
    - `year`: The year of the data
    - `state`: The state for which the data is reported
    - `corn_production`: The corn production in bushels
    - `Sales`
    - `Value`
    - and many other unstructured fields so that it is stored in a json file.
    
### Data2: Fertilizers from Walmart
    - **Source**: Walmart Product Page
    - **Description**: This data source scrapes the product details of a fertilizer product from Walmart's website. The data includes information such as the product name, price, rating, and detailed product information.
    - **Data Fields**:
        - `name`: The name of the product
        - `price`: The price of the product
        - `rating`: The rating of the product
        - `detail`: Detailed product information
## Features

- Fetch data from APIs
- Scrape data from web pages
- Save collected API data to json and webpage data to CSV files
- Configurable data sources via a YAML configuration file

## Project Structure
```
data_collection_tool/
├── config/
│   └── config.yaml
├── data/
│   ├── csv/
│   └── json/
├── logging_info/
|   └── app.log
├── src/
│   ├── __init__.py
│   ├── fetch.py
│   ├── scrape.py
|   |── test.py
│   └── utils.py
├── main.py
├── README.md
└── requirements.txt
```

## Setup Instructions

### Prerequisites

- Python 3.x
- `pip` (Python package installer)
- `Proxies API` It might not always necessary but very useful to have a proxy API to avoid getting blocked by the website.
- `BeautifulSoup4` and `requests` libraries
- `PyYAML` library for parsing the configuration file

### Creating a Virtual Environment

1. **Navigate to your project directory**:
    ```bash
    cd path/to/your/project
    ```

2. **Create the virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS and Linux**:
     ```bash
     source venv/bin/activate
     ```

### Installing Required Libraries

With the virtual environment activated, install the necessary libraries:

```bash
pip install -r requirements.txt
```

## Configuration

The data sources are configured in the `config/config.yaml` file. Here is an example configuration:

```yaml
data_sources:
  - name: USDA's Corn Production of Vergenia
    type: fetch
    url: 'https://quickstats.nass.usda.gov/api/api_GET/?key=AF79DE52-A47B-3E15-A35F-03C211866A21&commodity_desc=CORN&year__GE=2020&state_alpha=VA'
    
  - name: Fertilizers from Walmart
    type: scrape
    url: 'https://www.walmart.com/ip/Pennington-Rejuvenate-Organic-and-Natural-All-Purpose-Plant-Food-Fertilizer-Feeds-4-Months-4-lb/1435190801'
    target_element:
      price: 'span[itemprop="price"]'
      name: 'h1[itemprop="name"]'
      rating: 'span[class="rating-number"]'
      detail: 'script[id="__NEXT_DATA__"]'
```

## Usage

### Running the Data Collection Tool

With the virtual environment activated, run the main script:

```bash
python main.py
```

The script will load the configuration, fetch and scrape data from the specified sources, and save the data to the `data/` directory as CSV files.

### Example Output

After running the script, the `data/` directory will contain json file for API and CSV files for web, named after the data sources:

```
data/
├── data/json/example_api.csv
└── data/csv/example_website.csv
```

## Contributions

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries or questions, please contact [Anish Khatiwada] at [anishkhatioda@outlook.com].
