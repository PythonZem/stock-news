from api import get_last_news, get_stockdata, STOCK
from SMS import send_sms
import math

img = {"up": "🔺",
       "down": "🔻"}

price = get_stockdata()
start_price = float(price[1])+500
finish_price = float(price[0])
different = (finish_price - start_price) / start_price * 100
last_news = get_last_news()
if different >= 0:
    sign = img["up"]
else:
    sign = img["down"]

if not -5 <= different <= 5:
    text = f"""
{STOCK}: {sign}{round(different) }%
{last_news["Headline"]}

{last_news["Brief"]}
"""
    send_sms(text=text)