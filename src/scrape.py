import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import json

def scrape_data(urls, target_element=None):
    '''
    This function scrapes data from a list of URLs and returns a DataFrame
    :param urls:
    :param target_element:
    :return:
    '''
    results = []
    for url in urls:
        # existing code...
        ac = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        headers = {
            "Referer": "https://www.google.com",
            "Connection": "Keep-Alive",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": ac,
            "User-Agent": "Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1"
        }
        payload = {
            'api_key':'41eda62231ec7c7f3f9e32455547a9ce',
            'url':url,
            'render':'true'
        }
        # Load the webpage
        html = requests.get("http://api.scraperapi.com", params=payload)
        if ("Robot or human" in html.text):
            print(True)
        else:
            print(False)
        product_info = {}
        soup = BeautifulSoup(html.text,'html.parser')
        obj = {}
        try:
            obj["price"] = soup.find("span", {"itemprop": "price"}).text.replace("Now ", "")
        except:
            obj["price"] = None
        try:
            obj["name"] = soup.find("h1", {"itemprop": "name"}).text
        except:
            obj["name"] = None
        try:
            obj["rating"] = soup.find("span", {"class": "rating-number"}).text.replace("(", "").replace(")", "")
        except:
            obj["rating"] = None
        nextTag = soup.find("script", {"id": "__NEXT_DATA__"})
        if nextTag is not None:
            jsonData = json.loads(nextTag.text)
            Detail = jsonData.get('props', {}).get('pageProps', {}).get('initialData', {}).get('data', {}).get('product', {}).get('shortDescription', None)
            obj["detail"] = Detail
        else:
            obj["detail"] = None
        results.append(obj)
    return pd.DataFrame(results)