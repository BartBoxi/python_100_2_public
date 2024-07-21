from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

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


