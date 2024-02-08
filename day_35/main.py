from twilio.rest import Client
import requests

endpoint = "http://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC26f5e5d16942bb5e431ab1c151b54b58"
auth_token = "a231819d5f6ccf6a4b7a65a4f3d24193"
weather_param = {
    "appid": "fe4710a7303b544c44b9c3041b99d647",
    "q": "Warsaw",
    "cnt": 4
}
response = requests.get(endpoint, params=weather_param)

#print(response.status_code)
#print(response.raise_for_status())
data = response.json()
print(data)



first = data["list"][0]
weather_id = first["weather"][0]['id']
weather_desc =  first["weather"][0]['description']
second = data["list"][1]
weather_id_2 = second["weather"][0]['id']
third = data["list"][2]
weather_id_3 = third["weather"][0]['id']
#print(first)
fourth = data["list"][3]
weather_id_4 = fourth["weather"][0]['id']
# print(weather_id_2)
# print(weather_id_3)
# print(weather_id_4)
pogoda = [weather_id, weather_id_2, weather_id_3, weather_id_4]
print(pogoda)

will_rain = False

for i in pogoda:
    if i < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body='It is going to rain today. Remember to bring an ☂️ ',
        from_="+17867131656",
        to= "+48531305974"
    )
