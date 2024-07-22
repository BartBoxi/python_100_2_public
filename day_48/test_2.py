from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
item_prices = []


for price in all_prices:
    price_text = price.text
    if price_text:
        final_price = price_text.split(" - ")
        final_price = final_price[1].replace(",","")
        final_price = int(final_price)
        item_prices.append(final_price)
        print(item_prices)

###method 1 of combining two lists into one dictionary

#item_dict = dict(zip(item_ids, item_prices))
#print(item_dict)
# item_dict = {}
# for i in range(len(item_ids)):
#     item_dict[item_ids[i]] = item_prices[i]
# print(item_dict)

while True:
    cookie.click()