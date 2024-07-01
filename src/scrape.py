import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def scrape_data(url, target_element=None):

    ac = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"

    # Set the headers
    headers = {
        "Referer": "https://www.google.com",
        "Connection": "Keep-Alive",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": ac,
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1"
    }

    # Proxy information (replace with an actual proxy address and port)
    proxies = {
        "http": "http://<auto>:<apify_proxy_aWw1qSDGs5lz4CI5aDZI8QVJTp2w3A4eZEmY>@proxy.apify.com:8000"
    }

    # Load the webpage
    resp = requests.get(url, headers=headers, proxies=proxies)

    # To check if the page is blocked by the website captcha
    if ("Robot or human" in resp.text):
        print(True)
    else:
        print(False)
    soup = BeautifulSoup(resp.text, 'html.parser')
    l = []
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
    import json
    nextTag = soup.find("script", {"id": "__NEXT_DATA__"})
    jsonData = json.loads(nextTag.text)
    Detail = jsonData['props']['pageProps']['initialData']['data']['product']['shortDescription']
    try:
        obj["detail"] = Detail
    except:
        obj["detail"] = None
    l.append(obj)
    print(l)

    #convert into pandas dataframe and return
    return pd.DataFrame(l)