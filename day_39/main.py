import requests
import os
import json



#APIs

##Sheety
sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/flightDeals/prices"
# USER = os.environ["USER"]
# PASS = os.environ["PASS"]
headers_sheety = {"Authorization":"Basic YmFydDpNZW5hY29yKiExOTk2"}
response = requests.get(url=sheety_url)
data = response.json()

print("response.status_code = ", response.status_code)
print("response.text= ", response.text)
print(data)


##kiwi_search_api
kiwi_search_url = "https://api.tequila.kiwi.com/v2"

parameters = {
    "apikey" : "QLYELueajtR5B7uG9le9s4MZ93Gj1w54",
    "fly_from" : "WAW",
    "fly_to" :
}