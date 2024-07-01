import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def scrape_data(url='https://www.walmart.com/ip/Pennington-Rejuvenate-Organic-and-Natural-All-Purpose-Plant-Food-Fertilizer-Feeds-4-Months-4-lb/1435190801'):
    # List of user-agents
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    ]

    # Choose a random user-agent
    user_agent = random.choice(user_agents)

    # Set the headers
    headers = {'User-Agent': user_agent}

    # Proxy information (replace with an actual proxy address and port)
    proxies = {
        "http": "http://<auto>:<apify_proxy_aWw1qSDGs5lz4CI5aDZI8QVJTp2w3A4eZEmY>@proxy.apify.com:8000"
    }

    # Load the webpage
    resp = requests.get(url, proxies=proxies)

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
    # Add your scraping code here...
    l.append(obj)
    print(l)

scrape_data()