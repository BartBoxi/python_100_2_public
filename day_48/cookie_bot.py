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
grandma = driver.find_element(By.ID, "buyGrandma")
grandma_text = grandma.text

factory = driver.find_element(By.ID, "buyFactory")
factory_text = factory.text

mine = driver.find_element(By.ID, "buyMine")
mine_text = mine.text

shipment = driver.find_element(By.ID, "buyShipment")
shipment_text = shipment.text

lab = driver.find_element(By.ID, "buyAlchemy lab")
lab_text = lab.text

portal = driver.find_element(By.ID, "buyPortal")
portal_text = portal.text

machine = driver.find_element(By.ID, "buyTime machine")
machine_text = machine.text

upgrade_elements = [cursor, grandma, factory, mine, shipment, lab, portal, machine]

upgrade_prices = {}
for name, element in upgrade_elements.items():
    text = element.text
    price = int(text.split()[-1].replace(",",""))
    upgrade_prices[name] = price



last_execution_time = time.time()





