from keys import *
import requests
from datetime import date,datetime

now  = datetime.now().strftime("%H:%M")
today =  date.today().strftime("%d-%m-%Y")

excercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
add_data_url = sheets_url

header_params = {
    'Content-Type': 'application/json',
    'x-app-id': app_id,
    'x-app-key': api_key
}

# query_params = {
#     "query": "swam for 1 hour"
# }

user_input  =  input("Enter the excercise you have done today: ")

query_params = {
    "query": user_input,
    "weight_kg"  : 65,
    "height_cm"  : 167,
    "age" : 25
}

response  = requests.post(url = excercise_url , json =query_params , headers=header_params)

# print(response.json())

json_response =  response.json()

for exercise in json_response["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response =  requests.post(url=add_data_url, json = sheet_inputs)
    print(sheet_response.json())

