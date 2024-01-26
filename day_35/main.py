<<<<<<< HEAD
import requests

endpoint = "http://api.openweathermap.org/data/2.5/forecast"
weather_param = {
    "appid": "fe4710a7303b544c44b9c3041b99d647",
    "q": "Warsaw",
}
response = requests.get(endpoint, params=weather_param)

print(response.status_code)

data = response.json()
print(data)
=======
api_keu = "8f1ba3f2663b7bf0011d4ab86989fa29"

>>>>>>> origin/main
