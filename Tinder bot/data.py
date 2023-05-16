from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv(".env")

class TinderBot:
    
    def set_driver(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("geo.prompt.testing", True)
        self.profile.set_preference("geo.prompt.testing.allow", True)
        self.driver = webdriver.Firefox(self.profile, executable_path = r"C:\Users\obada\Downloads\firefox_driver")
        self.driver.get("https://tinder.com")
        
        
    def facebook_login(self):
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button").click()
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)
        self.driver.find_element(By.ID, "email").send_keys(os.getenv("FACEBOOK_EMAIL")) 
        self.driver.find_element(By.ID, "pass").send_keys(os.getenv("FACEBOOK_PASS"))
        self.driver.find_element(By.NAME, "login").click()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]").click()
        sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]").click()
        sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[3]/button[2]").click()
        
    def swipe_right(self):
        self.like_button = ".Bgi\(\$g-ds-background-like\)\:a"
        while True:
            sleep(1)
            try:
                self.driver.find_element(By.CSS_SELECTOR, self.like_button).click()
            except:
                self.driver.quit()