import smtplib
import random,os

my_email = "raghavandev12@gmail.com"
my_password = "ughj wxdq ccfm vgyk" 

subject  = "HAPPY BIRTHDAY!"

file_location  = ["letter_1.txt","letter_2.txt","letter_3.txt"]  


import datetime as dt 
import pandas as pd 

now = dt.datetime.now()

month = now.month
day =  now.day

csv_content  =  pd.read_csv("birthdays.csv")
filtered_content = csv_content[csv_content['month']== month ]

for index,row in filtered_content.iterrows():
    receiver_name  = row['name']
    redceiver_email =  row['email']


file  =  random.choice(file_location)


with open(f"letter_templates/{file}") as file :
     file_content  = file.read()

new_content  =  file_content.replace("[NAME]",receiver_name)
new_content  =  new_content.replace("Angela","Raghavan")

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=redceiver_email, msg= f"Subject:{subject}\n\n{new_content}" )  
     








# HINT 2: Use pandas to read the birthdays.csv

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



