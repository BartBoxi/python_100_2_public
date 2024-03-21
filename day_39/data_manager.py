import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/flightDeals/prices/"

    response = requests.get(url=sheety_url)
    data = response.json()
    print(data)

    city_id_list = [(item['city'], item['id']) for item in data['prices']]

    cities = {
        "Warsaw": "WAW",
        "Berlin": "BER",
        "Tokyo": "TYO",
        "Sydney": "SYD",
        "Istanbul": "IST",
        "Kuala Lumpur": "KUL",
        "New York": "NYC",
        "San Francisco": "SFO",
        "Cape Town": "CPT",
        "Frankfurt": "FRK",
        "Krakow": "KRK",
        "Amsterdam":"AMS",
        "New York City": "JFK"
    }
    global city
    for city_tuple in city_id_list:
        city = city_tuple[0]
        id = city_tuple[1]
        if city in cities:
            sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/flightDeals/prices/"
            data = {
                "price": {
                    "iataCode": cities[city]
                }
            }
            headers_sheety = {"Authorization": "Basic YmFydDpNZW5hY29yKiExOTk2"}
            endpoint = f"{sheety_url}/{id}"
            response = requests.put(url=endpoint, json=data, headers=headers_sheety)
            print(response.status_code)
            print(response.text)
        else:
            print("error")
DataManager()

