import requests
from bs4 import BeautifulSoup

# date = input("Please provide date in YYYY-MM-DD")
# print(date)

URL = 'https://www.billboard.com/charts/hot-100/2000-08-12'

response = requests.get(URL)
response = response.text

soup = BeautifulSoup(response, "html.parser")
songs = soup.select("li ul li h3")
print(songs)

#all_movies = soup.find_all(name="h3", class_="title")
