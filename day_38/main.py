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
print(excercise_put)
excercise_put.raise_for_status()
result = excercise_put.json()
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']
result = result['exercises'][0]['user_input']
print(result)

# docs used for this api https://docx.syndigo.com/developers/docs/natural-language-for-exercise?highlight=nutritionix%20excercies

sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/myWorkouts/workouts"

today = datetime.today()
today = today.strftime("%Y-%m-%d")
time = datetime.now()
time = time.strftime("%H:%M:%S")

workouts = {
    "workouts": {
        "Date": today,
        "Time": time,
        "Exercise": result,
        "Duration": duration,
        "Calories": calories,
    }
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url=sheety_url, headers=headers, data=json.dumps(workouts))

if response.status_code == 200:
    json_response = response.json()
    print(json_response['workouts'])
else:
    print("Error", response.status_code)
