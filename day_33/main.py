import requests
from datetime import datetime
MY_LAT = 52.242130
MY_LONG = 20.912830

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_positon = (longitude, latitude)
# print(iss_positon)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()


print(sunrise.split("T")[1].split(":")[0], sunset.split("T")[1].split(":")[0])

print(time_now.hour)