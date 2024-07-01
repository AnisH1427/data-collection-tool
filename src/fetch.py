import requests
import pandas as pd

def fetch_data(url):
    '''
    This function fetches data from a given URL and returns it as a DataFrame
    :param url:
    :return:
    '''
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")