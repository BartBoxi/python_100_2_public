from bs4 import BeautifulSoup
# import lxml
#
# with open("website2.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# print(soup.title)
# print(soup.prettify())

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)
#article_tag = soup.find(name="span", class_="titleline")
article_tag = soup.find("span", class_="titleline")
print(article_tag)