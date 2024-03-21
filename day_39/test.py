import requests

##kiwi_search_api
# kiwi_search_url = "https://api.tequila.kiwi.com/v2/search"
#
# headers = {
#     "apikey" : "QLYELueajtR5B7uG9le9s4MZ93Gj1w54"
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

###Testing reading one row (cell) in google sheet

sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/flightDeals/prices/"

response = requests.get(url=sheety_url)
data = response.json()
print(data)

city_id_list = [(item['city'], item['id']) for item in data['prices']]
print(city_id_list)

# city = data['prices'][0]['city']
# id = data['prices'][0]['id']
# print(city)

cities = {
    "Warsaw":"WAW",
    "Berlin":"BER",
    "Tokyo":"TYO",
    "Sydney":"SYD",
    "Istanbul": "IST",
    "Kuala Lumpur": "KUL",
    "New York": "NYC",
    "San Francisco": "SFO",
    "Cape Town": "CPT"
}


city = 'Warsaw'
if city in cities:
    sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/flightDeals/prices/"
    id = id
    data = {
        "price": {
            "iataCode": cities[city]
    }
    }
    headers_sheety = {"Authorization": "Basic YmFydDpNZW5hY29yKiExOTk2"}
    endpoint = f"{sheety_url}/{id}"
    response = requests.put(url=endpoint, json=data, headers=headers_sheety)
else:
    print("error")




# headers_sheety = {"Authorization": "Basic YmFydDpNZW5hY29yKiExOTk2"}
# endpoint = f"{sheety_url}/{id}"
# response = requests.put(url=endpoint, json=data, headers=headers_sheety)
# print("response.status_code =", response.status_code)
# print("response.text= ", response.text)