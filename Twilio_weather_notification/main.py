import requests
import json
from twilio.rest import Client
from keys import *




#constants

long = 80.073268
lat = 12.873253


values = {"lat":lat,"lon":long,"appid":api_key,'cnt':4}


response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast",params=values)

json_response =  response.json()

with open ("weather_data.json","w") as file:
    json_response_formatted  =  json.dumps(json_response,indent=4)
    file.write(json_response_formatted)

weather_list = json_response['list']

will_rain = False
for data in weather_list:
     value = data['weather']
     for items in value:
          code  =  items['id']
          if code < 700:
              will_rain  = True
        

if will_rain:
    print("It will rain")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            from_='+12562696598',
            body='it is going to rain bring an umbrealla',
            to='+919514980684')
    

    print(message.status)