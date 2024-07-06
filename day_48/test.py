from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")
money = money.text
print(money)
#right panel
cursor = driver.find_element(By.ID, "buyCursor")
cursor = cursor.text
cursor = cursor.split()
cursor_price = cursor[2]
print(cursor_price)


