import os
from dotenv import load_dotenv
from twilio.rest import Client
import requests
from datetime import datetime

load_dotenv()
"""
TWILIO CREDENTIALS
"""
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone = os.getenv('TWILIO_ACCOUNT_PHONE')
destinatary_phone = "+524422737383"
"""
TWILIO SMS CONFIGURATION 
"""
client = Client(account_sid, auth_token)

def send_sms(sms_body: str,remitent: str, destinatary: str):
    message = client.messages \
                    .create(
                        body=sms_body,
                        from_=remitent,
                        to=destinatary
                    )
    return (message.sid)

"""
NEWS API CONFIGURATION
"""
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
# DATETIME FOR TODAYS NEWS
today = datetime.today()
today_date = today.strftime("%Y-%m-%d")
# FUNCTION THAT EXTRACTS THE NEWS OF THE API AND RETURNS A DICTIONARY WITH THE NEWS
def get_news(company: str, date = today_date, quantity = 3):
    list_of_news = []
    url = ('https://newsapi.org/v2/everything?'
       f'q={company}&'
       f'from={date}&'
       'sortBy=popularity&'
       f'apiKey={NEWS_API_KEY}')
    
    res = requests.get(url=url)
    res.raise_for_status()
    for i in range(0,quantity):
        news_title = res.json()["articles"][i]["title"]
        news_content = res.json()["articles"][i]["content"]
        news_url = res.json()["articles"][i]["url"]
        news_dict = {
            "title":news_title,
            "content":news_content,
            "url":news_url
        }
        list_of_news.append(news_dict)
    return list_of_news



"""
POLYGON API KEY CONFIGURATION (STOCK MARKET)
"""
POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')
APPLE_STOCK = "AAPL"
def get_closing_price(stock = APPLE_STOCK,api_key= POLYGON_API_KEY,):
    url = (f'https://api.polygon.io/v2/aggs/ticker/{stock}/prev?'
        'adjusted=true&'
        f'apiKey={api_key}')
    res = requests.get(url=url)
    res.raise_for_status()
    closing_price = res.json()["results"][0]["c"]
    closing_price_str = "$" + str(closing_price)
    return closing_price_str

"""
SMS FORMAT 
"""
closing_price = get_closing_price(stock=APPLE_STOCK)
list_of_news = get_news("Apple")

stock_alert_message = (
    f'{APPLE_STOCK}: {closing_price}\n' 
    f'{list_of_news[0]["title"]}...{list_of_news[0]["url"]}\n'
    f'{list_of_news[1]["title"]}...{list_of_news[1]["url"]}\n'
    f'{list_of_news[2]["title"]}...{list_of_news[2]["url"]}\n'
)

send_message = False

send_sms(sms_body=stock_alert_message,remitent=twilio_phone,destinatary=destinatary_phone)
       





