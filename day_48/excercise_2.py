from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# #article_number = driver.find_element(By.XPATH, "//a[@href='/wiki/Special:Statistics']").text
# article_number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# #article_number.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# #all_portals.click()
#
# # Find the "Search" <input> by Name
#
# search = driver.find_element(By.NAME, value="search")
#
# #Sending key to the search
# search.send_keys("Python",Keys.ENTER)


driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Bartosz", Keys.TAB)
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Pudlo", Keys.TAB)
email = driver.find_element(By.NAME, "email")
email.send_keys("bartoszpudlo07@gmail.com", Keys.TAB)

button = driver.find_element(By.CLASS_NAME,"btn-primary")
#print(button.text)
button.click()
