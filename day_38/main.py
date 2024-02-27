import requests

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
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT,
    "age":AGE,
}

excercise_put = requests.post(url=excercise_endpoint, json= parameters,  headers=headers)
print(excercise_put)
excercise_put.raise_for_status()
result = excercise_put.json()
print(result)

#docs used for this api https://docx.syndigo.com/developers/docs/natural-language-for-exercise?highlight=nutritionix%20excercies