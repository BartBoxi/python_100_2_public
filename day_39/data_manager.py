import requests
from pprint import pprint

global sheety_url
sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/flightDeals/prices/"

class DataManager:

    def __init__(self):
        self.destination_data = {}
    def get_destination_data(self):
        response = requests.get(url=sheety_url)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for city in self.desitation_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_url}/{city['id']}",
                json = new_data
            )
            print(response.text)




