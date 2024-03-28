import os

import requests
from datetime import datetime
import json
import os


APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
# APP_ID = "" #please update if u want  to use it
# API_KEY = "" #please update if u want  to use it
USER = os.environ["USER"]
PASS = os.environ["PASS"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

GENDER = "male"
WEIGHT_KG = 60
HEIGHT = 180
AGE = 27

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

excercise = input("Enter the excercise you did - input should be excercies and duration 1 h or 1 m ")

parameters = {
    "query": excercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

excercise_put = requests.post(url=excercise_endpoint, json=parameters, headers=headers)
result = excercise_put.json()
print(result)

# docs used for this api https://docx.syndigo.com/developers/docs/natural-language-for-exercise?highlight=nutritionix%20excercies

sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/bart/arkusz1"



###STEP 4###

today = datetime.today()
today = today.strftime("%d/%m/%Y")
time = datetime.now()
time = time.strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "arkusz1": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    basic = {
        "user": USER, #please update if u want  to use it
        "pass": PASS #please update if u want  to use it add as local variable 
    }
    #headers for authorization
    #added just a header
    headers_sheety = {"Authorization":"Basic YmFydDpNZW5hY29yKiExOTk2"}

    response = requests.post(url=sheety_url, json=sheet_inputs, headers=headers_sheety)

    if response.status_code == 200:
        json_response = response.json()
        print(json_response['arkusz1'])
    else:
        print("Error", response.status_code)
    print(response.text)



