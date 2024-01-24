import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


# MY_LAT = 28.507351 # Your latitude
# MY_LONG = -99.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
time_now = time_now.strftime('%H')

# print(sunrise)
# print(sunset)
# print(time_now)
#If the ISS is close to my current position

message = f"Look up! ISS is above you with latitude {iss_latitude} and longitude {iss_longitude}"
def send_email():
    my_email = "pythonbarttest@gmail.com"
    password = "udyd dkwa cost ydqy"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="bartoszpudlo07@gmail.com",
                            msg=f'Subject:ISS is above\n\n{message}.')

while True:
#The ISS position is within +5 or -5 degrees of the iss position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG-5:
        if sunset <= time_now <= sunrise:
            send_email()
    else:
        print("nah")
    time.sleep(60)



# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



