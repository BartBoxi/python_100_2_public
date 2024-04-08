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

articles = article_tag = soup.find_all("span", class_="titleline") ###with find all we are scraping for
# all 30 articles that are avaiable on the page
texts = []
links = []
for article_tag in articles:
    article_text = article_tag.getText()
    texts.append(article_text)
    article_link = article_tag.find('a')
    article_link = article_link.get("href")
    links.append(article_link)

#print(article_tag)
print(article_text)
print(article_link)
print(texts)
print(links)