from keys import *
import requests
import  json
from datetime import date,timedelta
from twilio.rest import Client
import time 

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


def percentage_func(a,b):
        
        percentage  = abs(a - b) / ((a + b) / 2) * 100
        percentage =  float(percentage)
        return percentage 

# print(percentage_func(a=900,b= 1000))



def date_find(today_date):
        yesterday =  today_date - timedelta(days=1)
        day_bf_yesterday = today_date - timedelta(days = 2)
        return yesterday,day_bf_yesterday
        

#date extraction 

today  =  date.today()

yesterday,day_bf_yesterday =date_find(today) 


print(f"Today : {today} Yesterday : {yesterday} Day_bf_yesterday : {day_bf_yesterday}")

news_url = ("https://newsapi.org/v2/everything")

news_params = {
       "q":COMPANY_NAME,
       "from":yesterday,
       "sortBy":"relevancy",
       "apiKey":news_apikey 
}
    

params = {
    "function" :"TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "interval" : "60min",
    "apikey": api_key
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response  = requests.get(url=STOCK_ENDPOINT,params=params)
data_dict = response.json()
time_data =  data_dict["Time Series (Daily)"]
yesterday_close = time_data[str(yesterday)]['4. close']
day_bf_yesterday_close = time_data[str(day_bf_yesterday)]['4. close']

percentage_diff =  percentage_func(a=float(yesterday_close),b = float(day_bf_yesterday_close))
print(percentage_diff)

Title = ""

if float(yesterday_close)> float(day_bf_yesterday_close):
      Title += f"🔺 {percentage_diff}/n"
else:
      Title += f"🔻 {percentage_diff}/n"

if percentage_diff > 5:
               
    news_response = requests.get(url = news_url, params=news_params)
    articles = news_response.json()['articles']

    for article in articles:
       Title  += article['title']
       Description =  article['description']
    #    print(f"Title : {Title} and \n Description : {Description}")
       
       time.sleep(10)
       client = Client(account_sid, auth_token)
       message = client.messages.create(
            from_=from_number,
            body=f"Title : {Title} \n Decription : {Description}",
            to=to_number)
       print(message.status)
else:
        print("No news")

