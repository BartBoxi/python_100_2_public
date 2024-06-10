from selenium import webdriver
#day2
# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://amazon.com")

driver.close() #closing single tab
driver.quit() #quit the entier browser not just a tab