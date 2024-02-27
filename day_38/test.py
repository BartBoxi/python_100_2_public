import requests

APP_ID = "024a7bf0"
API_KEY = "cd9678b13f4b908b97e0c13f75672ccc"

headers = {
"x-app-id": APP_ID,
"x-app-key": API_KEY,
}

GENDER = "male"
WEIGHT = 70.6
HEIGHT = 176.5
AGE = 20

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_json = {
"query": input("Tell me which exercise you did. "),
"gender": GENDER,
"weight_kg": WEIGHT,
"height_cm": HEIGHT,
"age": AGE,
}

response = requests.post(url=exercise_endpoint, json=exercise_json, headers=headers)
result = response.json()
print(result)