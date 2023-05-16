from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv(".env")

class TwitterBot:
    
    def internet_speed(self):
        self.driver = webdriver.Firefox(executable_path = r"C:\Users\obada\Downloads\firefox_driver")
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a").click()
        sleep(60)
        self.download_speed = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.upload_speed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
        self.driver.quit()
        
    def twitter_login(self):
        self.driver = webdriver.Firefox(executable_path = r"C:\Users\obada\Downloads\firefox_driver")
        self.driver.get("https://www.twitter.com")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, """.r-1ydw1k6 > div:nth-child(1) > div:nth-child(1) >
        div:nth-child(1) > a:nth-child(1)""").click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".r-30o5oe").send_keys(os.environ["TWITTER_EMAIL"])
        self.driver.find_element(By.CSS_SELECTOR, "div.css-18t94o4:nth-child(6)").click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".r-homxoj").send_keys(os.environ["PHONE_NO"])
        self.driver.find_element(By.CSS_SELECTOR, "div.r-19yznuf").click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".r-homxoj").send_keys(os.environ["TWITTER_PASS"])
        self.driver.find_element(By.CSS_SELECTOR, ".r-1sw30gj > div:nth-child(1)").click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".r-30o5oe").send_keys(os.environ["PHONE_NO"])
        self.driver.find_element(By.CSS_SELECTOR, ".r-1sw30gj > div:nth-child(1)").click()
        
    def tweet(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "a.r-l5o3uw").click()
        sleep(1)
        self.driver.find_element(By.XPATH, """/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/
        div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/
        div/div/div/div[2]/div""").send_keys(f"""yooo @TurkTelekom my internet download speed is {self.download_speed} and
        upload speed is {self.upload_speed} and i pay only 110 tl monthly for a better company than you""")
        self.driver.find_element(By.CSS_SELECTOR, "div.r-l5o3uw:nth-child(4)").click()
        self.driver.quit()
        
        