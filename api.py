import os
from dotenv import find_dotenv, load_dotenv
import requests
load_dotenv(find_dotenv())


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MAIN_PRODUCT = "TESLA"

URL_STOCK = 'https://www.alphavantage.co/query?'
parameters_stock = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK,
            "apikey": os.getenv("apikey_stock"),
        }

URL_NEWS = 'https://newsapi.org/v2/everything?'
parameters_news = {
            "q": f"{MAIN_PRODUCT}",
            "language": "en",
            "apiKey": os.getenv("apikey_news"),
        }


def get_stockdata():
    r = requests.get(URL_STOCK, params=parameters_stock)
    raw_data = r.json()
    daily_data = raw_data["Time Series (Daily)"]
    last_tree_days = list({date: price["4. close"] for date, price in list(daily_data.items())[:2]}.values())
    return last_tree_days


def get_last_news():
    r = requests.get(URL_NEWS, params=parameters_news)
    raw_data = r.json()
    last_news = {
        "Headline": raw_data["articles"][0]["title"],
        "Brief": raw_data["articles"][0]["description"]
                 }
    return last_news


