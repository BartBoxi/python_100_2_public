import requests

##kiwi_search_api
kiwi_search_url = "https://api.tequila.kiwi.com/v2/search"

headers = {
    "apikey" : "QLYELueajtR5B7uG9le9s4MZ93Gj1w54"
}

parameters = {
    "fly_from" : "JFK",
    "fly_to" : "LON",
    "date_from" : "20/03/2024",
    "date_to" : "01/05/2024"
}

flights = requests.get(url=kiwi_search_url, headers=headers, params=parameters)
flights_data = flights.json()
print("response.status_code = ", flights.status_code)
print("response.text= ", flights.text)
print(flights_data)