from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep 
from dotenv import load_dotenv
import os

load_dotenv(".env")

class InstagramBot:
    
    def instagram_login(self):
        self.driver = webdriver.Firefox(executable_path = r"C:\Users\obada\Downloads\firefox_driver")
        self.driver.get("https://www.instagram.com")
        sleep(1)
        self.driver.find_element(By.NAME, "username").send_keys(os.environ["INSTAGRAM_EMAIL"])
        self.driver.find_element(By.NAME, "password").send_keys(os.environ["INSTAGRAM_PASS"])
        self.driver.find_element(By.CSS_SELECTOR, "._acap").click()
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "div.x1i10hfl").click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button._a9--:nth-child(2)").click()
        
    def search_page(self):
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".x1xgvd2v > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "._aauy").send_keys(os.environ["PAGE_NAME"])
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "._abn_ > a:nth-child(1)").click()
        
    def follow_followers(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "li.xl565be:nth-child(2) > a:nth-child(1)").click()
        sleep(3)
        for a in range(1,174000):
            self.driver.find_element(By.CSS_SELECTOR, f"div.x1i10hfl:nth-child({a}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)").click()
        self.driver.quit()
        
        