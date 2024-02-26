import requests
from datetime import datetime, timedelta

USERNAME = "bartob"
TOKEN = "123312fasasdv"
TODAY = datetime.now()
TODAY = TODAY.strftime("%Y%m%d")


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Running",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN":TOKEN,
}


response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

#link to site https://pixe.la/v1/users/bartob/graphs/graph1.html
print(graph_config["id"])

graph = graph_config["id"]

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph}"
print(pixel_update_endpoint)

pixel_update = {
    "date":TODAY,
    "quantity":"50",
}

pixel = requests.post(url=pixel_update_endpoint, json=pixel_update, headers=headers)
print(pixel.text)

