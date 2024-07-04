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
cursor = driver.find_element(By.ID, "buyCursor")


last_execution_time = time.time()

while True:
    cookie.click()

    current_time = time.time()

    if current_time - last_execution_time >= 5:
        if
        cursor.click()
    else:
        cookie.click()




