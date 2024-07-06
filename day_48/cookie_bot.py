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
cursor_text = cursor.text
cursor_split = cursor_text.split()
cursor_price = cursor_split[2]

grandma = driver.find_element(By.ID, "buyGrandma")
grandma_text = grandma.text
grandma_split = grandma_text.split()
grandma_price = grandma_split[2]

factory = driver.find_element(By.ID, "buyFactory")

mine = driver.find_element(By.ID, "buyMine")

shipment = driver.find_element(By.ID, "buyShipment")

lab = driver.find_element(By.ID, "buyAlchemy lab")
portal = driver.find_element(By.ID, "buyPortal")
machine = driver.find_element(By.ID, "buyTime machine")

list = [cookie, money, cursor. grandma, factory, mine, shipment, lab, portal, machine]

last_execution_time = time.time()

while True:
    cookie.click()
    current_time = time.time()
    if current_time - last_execution_time > 5:
        money = money.text

        if money > cursor_price:
            cursor.click()
        else:
            pass








