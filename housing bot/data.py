from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas

class SahibindenBot:
    
    def flats_data(self):
        self.driver = webdriver.Firefox(r'C:\Users\obada\AppData\Roaming\Mozilla\Firefox\Profiles\9x8d3523.default-release-1682615904672',
        executable_path = r"C:\Users\obada\Downloads\firefox_driver")
        self.driver.get("https://www.sahibinden.com/kiralik/izmir-buca?pagingSize=50&sorting=price_asc&a20=38472&a20=38473")
        self.csv = open("Github/sahibinden bot/data.csv", "a", encoding = "utf-8")
        for _ in range(1, 10):
            for a in range(1, 53):
                try:
                    price = self.driver.find_element(By.XPATH, f"/html/body/div[5]/div[4]/form/div[1]/div[3]/table/tbody/tr[{a}]/td[6]/div/span").text
                    district = self.driver.find_element(By.XPATH, f"/html/body/div[5]/div[4]/form/div[1]/div[3]/table/tbody/tr[{a}]/td[8]").text.split("\n")[1].split(" ")[0]
                    rooms_no = self.driver.find_element(By.XPATH, f"/html/body/div[5]/div[4]/form/div[1]/div[3]/table/tbody/tr[{a}]/td[5]").text
                    area = self.driver.find_element(By.XPATH, f"/html/body/div[5]/div[4]/form/div[1]/div[3]/table/tbody/tr[{a}]/td[4]").text
                    self.csv.write(f"{rooms_no},{area},{price},{district}\n")
                except:
                    continue
            self.driver.find_element(By.LINK_TEXT, "Sonraki").click()
            sleep(1)
        self.csv.close()
        self.driver.quit()
    
    
    def google_fomrs(self):
        self.driver = webdriver.Firefox(executable_path = r"C:\Users\obada\Downloads\firefox_driver")
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdEXuvB8LVtB-0yyEbscIYD1tfvRVAkK7A0ZhU9stbH-q64XQ/viewform")
        self.csv = pandas.read_csv("Github/sahibinden bot/data.csv", encoding = "latin-1").iterrows()
        sleep(3)
        for a in self.csv:
            sleep(1)
            self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(a[1][0])
            self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(a[1][1])
            self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(a[1][2])
            self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(a[1][3])
            sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, ".Y5sE8d > span:nth-child(3)").click()
            sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, ".c2gzEf > a:nth-child(1)").click()
        self.driver.quit()
    
        