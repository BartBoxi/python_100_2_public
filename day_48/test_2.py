from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")




timeout = time.time() + 60 * 0.1 #5 min from the start

while True:
    test = 0
    cookie.click()
    money = driver.find_element(By.ID, "money")
    money = money.text

    items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")

    item_ids = [item.get_attribute("id") for item in items]




    if test == 5 or time.time() > timeout:
        break
    test = test - 1