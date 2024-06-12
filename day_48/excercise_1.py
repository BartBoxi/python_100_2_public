from selenium import webdriver
from selenium.webdriver.common.by import By



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://python.org")

events_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
for time in events_times:
    print(time.text)
events_name = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")

for name in events_name:
    print(name.text)

events = {}

for n in range(len(events_times)):
    events[n] = {
        "time": events_times[n].text,
        "name": events_name[n].text,
    }

print(events)

driver.close()
driver.quit()