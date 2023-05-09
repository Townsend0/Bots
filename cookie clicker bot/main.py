from selenium import webdriver
from selenium.webdriver.common.by import By
import time

a = webdriver.Firefox(executable_path = r"C:\Users\obada\Downloads\firefox_driver")
a.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(2)

a.find_element(By.XPATH, '//*[@id="langSelect-EN"]').click()
time.sleep(2)

while True:
    a.find_element(By.ID, 'bigCookie').click()
    
    try:
        for b in range(19):
            a.find_element(By.ID, f"product{b}").click()
    except:
        continue
        