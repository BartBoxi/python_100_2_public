import requests



APP_ID = "024a7bf0"
API_KEY = "cd9678b13f4b908b97e0c13f75672ccc"

headers = {
    "Content-Type": "application/json",
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}
excercise = input("Enter the excercise you did ")
url = "https://trackapi.nutritionix.com/v2/natural/excercise"
endpoint = f"{url}/{excercise}"

excercise_put = requests.put(url=endpoint, headers=headers)
print(excercise_put.text)
print(excercise_put.json)

#docs used for this api https://docx.syndigo.com/developers/docs/natural-language-for-exercise?highlight=nutritionix%20excercies