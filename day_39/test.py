import requests
import json
#
# #kiwi_search_api
# kiwi_search_url = "https://api.tequila.kiwi.com/v2/search"
#
# headers = {
#     "apikey" : "" #please update if u want  to use it
# }
#
# parameters = {
#     "fly_from" : "JFK",
#     "fly_to" : "LON",
#     "date_from" : "20/03/2024",
#     "date_to" : "01/05/2024"
# }
#
# flights = requests.get(url=kiwi_search_url, headers=headers, params=parameters)
# flights_data = flights.json()
# print("response.status_code = ", flights.status_code)
# print("response.text= ", flights.text)
# print(flights_data)


global sheety_url
sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/flightDeals/prices/"
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





city_id_list = [(item['city'], item['id']) for item in data['prices']]

for city_tuple in city_id_list:
    city = city_tuple[0]
    id = city_tuple[1]
    url = "https://api.tequila.kiwi.com/locations/query"
    headers = {
        "apikey" : "" #please update if u want  to use it
    }
    parameters = {
        "term":city}
    IATA = requests.get(url=url, headers=headers, params=parameters)
    data = IATA.json()
    self.desitation_data = data
    print(IATA.status_code)
    print(IATA.text)
    print(IATA.json())









###Testing reading one row (cell) in google sheet
#
# sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/flightDeals/prices/"
#
# response = requests.get(url=sheety_url)
# data = response.json()
# print(data)
#
# city_id_list = [(item['city'], item['id']) for item in data['prices']]
#
# # for i in city_id_list:
# #     city_name = city_id_list[0]
# # print(city_id_list)
#
# # city = data['prices'][0]['city']
# # id = data['prices'][0]['id']
# # print(city)
#
# cities = {
#     "Warsaw":"WAW",
#     "Berlin":"BER",
#     "Tokyo":"TYO",
#     "Sydney":"SYD",
#     "Istanbul": "IST",
#     "Kuala Lumpur": "KUL",
#     "New York": "NYC",
#     "San Francisco": "SFO",
#     "Cape Town": "CPT",
#     "Frankfurt":"FRK"
# }
# global city
# for city_tuple in city_id_list:
#     city = city_tuple[0]
#     id = city_tuple[1]
#     if city in cities:
#         sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/flightDeals/prices/"
#         data = {
#             "price": {
#                 "iataCode": cities[city]
#         }
#         }
#         headers_sheety = {"Authorization": "Basic YmFydDpNZW5hY29yKiExOTk2"}
#         endpoint = f"{sheety_url}/{id}"
#         response = requests.put(url=endpoint, json=data, headers=headers_sheety)
#     else:
#         print("error")
#
#


# headers_sheety = {"Authorization": "Basic YmFydDpNZW5hY29yKiExOTk2"}
# endpoint = f"{sheety_url}/{id}"
# response = requests.put(url=endpoint, json=data, headers=headers_sheety)
# print("response.status_code =", response.status_code)
# print("response.text= ", response.text)