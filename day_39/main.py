#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from pprint import pprint
import os
import json



#APIs

##Sheety
sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/flightDeals/prices"
# USER = os.environ["USER"]
# PASS = os.environ["PASS"]
headers_sheety = {"Authorization":"Basic YmFydDpNZW5hY29yKiExOTk2"}
response = requests.get(url=sheety_url)
sheet_data = response.json()
sheet_data = sheet_data["prices"]
#print("response.status_code = ", response.status_code)
#print("response.text= ", response.text)
pprint(sheet_data)









# ##kiwi_search_api
# kiwi_search_url = "https://api.tequila.kiwi.com/v2"
#
# parameters = {
#     "apikey" : "QLYELueajtR5B7uG9le9s4MZ93Gj1w54",
#     "fly_from" : "WAW",
#     "fly_to" : "SFO",
#     "date_from" : "20/03/2024",
#     "date_to" : "01/05/2024"
# }
#
# flights = requests.get(url=kiwi_search_url, params=parameters)
# flights_data = flights.json()
# print("response.status_code = ", flights.status_code)
# print("response.text= ", flights.text)
# print(flights_data)