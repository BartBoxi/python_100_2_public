import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    iata_dict = {
        ""
    }
    sheety_url = "https://api.sheety.co/c5294e1cd882deb45fb05bdb1c1640b8/flightDeals/prices/"
    id = 2
    data = {
        "price": {
            "iataCode": "PL"
        }
    }
    headers_sheety = {"Authorization": "Basic YmFydDpNZW5hY29yKiExOTk2"}
    endpoint = f"{sheety_url}/{id}"
    response = requests.put(url=endpoint, json = data, headers=headers_sheety)
    print("response.status_code =", response.status_code)
    print("response.text= ", response.text)

DataManager()



#
# import requests
# SHEETY_ENDPOINT = f'https://api.sheety.co/xxxxxxxxxxxxxxxx/sheetyTest/sheet1/'
#
# id = 2
# data = {
#     "sheet1": {
#         "a": "C",
#         "b": "D",
#     }
# }
# endpoint = f"{SHEETY_ENDPOINT}/{id}"
#
# response = requests.put(url=endpoint, json=data)
# print("response.status_code =", response.status_code)
# print("response.text= ", response.text)
