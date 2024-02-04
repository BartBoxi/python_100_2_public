
import requests

endpoint = "http://api.openweathermap.org/data/2.5/forecast"
weather_param = {
    "appid": "fe4710a7303b544c44b9c3041b99d647",
    "q": "Warsaw",
    "cnt": 4
}
response = requests.get(endpoint, params=weather_param)

print(response.status_code)
print(response.raise_for_status())
data = response.json()
print(data)


