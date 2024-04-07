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
#article_tag = soup.find(name="span", class_="storylink")

article_tag = soup.find("span", class_="titleline")
article_text = article_tag.getText()
article_link = article_tag.find('a')
article_link = article_link.get("href")

print(article_tag)
print(article_text)
print(article_link)