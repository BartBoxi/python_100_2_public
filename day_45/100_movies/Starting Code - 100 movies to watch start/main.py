import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
top_movies = response.text
#print(top_movies)

soup = BeautifulSoup(top_movies, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
print(movies)

with open('movie_titles.txt', 'w') as file:
    for movie in movies:
        file.write(movie + '\n')
print("File created succesfully")