from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

#elements of the page
cookie = driver.find_element(By.ID, "cookie")

#get list of the items to buy
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5


while True:
    cookie.click()
    if time.time() > timeout:

        all_prices = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#store b")))
        item_prices = []

        for price in WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#store b"))):
            try:
                element_text = price.text
                if element_text != "":
                    cost = int(element_text.split("-")[1].strip().replace(",", ""))
                    item_prices.append(cost)
            except StaleElementReferenceException:
                print("Stale element encountered. Retrying...")

        #print(len(item_prices))

    #next steps is to create a dictionary with item name and prices


        item_dict = dict(zip(item_ids, item_prices))

        #print(item_dict)

        ### method 2 for getting dict from two lists

        # item_dict = {}
        # for i in range(len(item_ids)):
        #     item_dict[item_ids[i]] = item_prices[i] #here issue is that two list got different len

        # print(item_dict)

    # next get the current cookie count

        cookie_count = driver.find_element(By.ID, value="money")
        cookie_count = cookie_count.text
        cookie_count = int(cookie_count)
        #print(cookie_count)

    # find upgrades that we can afford
        global highest_key
        def higher_values(dictionary, threshold):

            affordable_items = {}
            for item_id, cena in dictionary.items():  # Iterate through key-value pairs
                if cena < threshold:
                    affordable_items[item_id] = cena
            if affordable_items:
                highest_value = max(affordable_items.values())
                highest_key = max(affordable_items, key=affordable_items.get)
                button = driver.find_element(By.ID, f"{highest_key}")
                button.click()
            else:
                print("no affordable items")

            #print(affordable_items)


        higher_values(item_dict, cookie_count)
    elif time.time() > five_min:
        break














