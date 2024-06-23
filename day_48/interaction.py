from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://en.wikipedia.org/wiki/Main_Page")
#article_number = driver.find_element(By.XPATH, "//a[@href='/wiki/Special:Statistics']").text
article_number = driver.find_element(By.CSS_SELECTOR, value = "#articlecount a").text
print(article_number)
