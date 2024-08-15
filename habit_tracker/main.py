import requests
from keys import *
from datetime import date

today_date  = date.today().strftime("%Y%m%d")

pixela_url =  "https://pixe.la/v1/users"

user_params = {
    "token" : user_creation_password ,
    "username" : user_name,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response  =  requests.post(url=pixela_url,json=user_params)

graph_url = f"{pixela_url}/{user_name}/graphs"

graph_params = {
    "id" : "cycling1",
    "name": "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "momiji",
    "timezone" : "Asia/Kolkata"
}

header_params = {
    "X-USER-TOKEN" : user_creation_password
}

# response =  requests.post(url =graph_url, json = graph_params , headers=header_params)

# print(response.text)
post_pixel_url = f"{graph_url}/cycling1"



def post_pixel(distance):

    post_pixel_params = {
    "date" : today_date,
    "quantity": distance
}
    response = requests.post(url =post_pixel_url  , json =post_pixel_params , headers = header_params )
    print(response.text)


def update_pixel(distance,date):

    update_url = f"{post_pixel_url}/{date}"

    update_params = {
    "quantity" : distance,
}
    response = requests.put(url = update_url , json = update_params,headers=header_params)
    print(response.text)

def delete_data(date):
    delete_url = f"{post_pixel_url}/{date}"
    response  =  requests.delete(url =delete_url, headers=header_params)
    print(response.text)

user_choice  =input("What operation you wan to perform?\n")

if user_choice.lower() == "post":
    user_input = input("How many KM you have cycled today : ")
    post_pixel(user_input)

elif user_choice.lower() == "update":
    update_date = input("When you want to update(YYYYMMdd) date format: ")
    update_distance = input("Distance you want to update(Km): ")
    update_pixel(update_distance,update_date)

elif user_choice.lower() == "delete":
    delete_date = input("Input the date when you want to delete the record: ")
    delete_data(delete_date)

