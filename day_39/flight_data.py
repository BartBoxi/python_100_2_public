import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2"
TEQUILA_APIKEY = "QLYELueajtR5B7uG9le9s4MZ93Gj1w54"

class FlightData:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_APIKEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
    #This class is responsible for structuring the flight data.
