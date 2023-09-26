from api import get_last_news, get_stockdata, STOCK
from SMS import send_sms

img = {"up": "🔺",
       "down": "🔻"}

price = get_stockdata()
start_price = float(price[1])
finish_price = float(price[0])
different = (finish_price - start_price) / start_price * 100
last_news = get_last_news()
if different >= 0:
    sign = img["up"]
else:
    sign = img["down"]

if not -5 <= different <= 5:
    text = f"""
{STOCK}: {sign}{different}%
Headline: {last_news["Headline"]}
Brief: {last_news["Brief"]}
"""
    send_sms(text=text)
