import requests
from datetime import datetime
import json

APP_ID = "024a7bf0"
API_KEY = "cd9678b13f4b908b97e0c13f75672ccc"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

GENDER = "male"
WEIGHT_KG = 60
HEIGHT = 180
AGE = 27

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

excercise = input("Enter the excercise you did ")

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


    response = requests.post(url=sheety_url, json=sheet_inputs)

    if response.status_code == 200:
        json_response = response.json()
        print(json_response['arkusz1'])
    else:
        print("Error", response.status_code)
    print(response.text)