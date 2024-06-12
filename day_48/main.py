from selenium import webdriver
from selenium.webdriver.common.by import By


#day2
# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
#
# driver.get("https://www.amazon.pl/Anker-SoundCore-przetwornikami-akumulator-bezprzewodowy/dp/B01MTB55WH/ref=sr_1_4?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dib=eyJ2IjoiMSJ9.Ue79Zu9BY1pIDRnHzHUbqCxK2RE1zzPoIIQ2MB0ee8PwMkT0mqrEdCE2QfsWAvvrE2xezDPLTcvnLlzZNpAb0ZuwAZjWhj2zy-zZk1Unbhg-w6mg7VstV9kxbo4LqrfDASNfxngsaN4LutAseBmkr05cQ3EQu50qKzGDpH8x4OQ.qNVCjrAaRaKZg2sCsfhPkDzHeWeyV0kcSjH78pKrfCo&dib_tag=se&keywords=apple%2Bhome%2Bpod&qid=1718137681&s=electronics&sr=1-4&th=1")
#
# price_pln = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_pln}.{price_cents}")



driver.close() #closing single tab
driver.quit() #quit the entier browser not just a tab