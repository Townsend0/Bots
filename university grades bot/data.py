from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
from email.mime.text import MIMEText

class UniBot:
    
    def set_mail(self):
        self.mail = smtplib.SMTP("smtp.gmail.com", 587)
        self.mail.starttls()
        self.mail.login("obadahpy@gmail.com", "zittlnfvrlwutenl")
        
    def uni_login(self):
        self.uni = webdriver.Firefox(executable_path = r"C:\Users\obada\Downloads")
        self.uni.get("https://online.deu.edu.tr/")
        self.uni.find_element(By.ID, "eid").send_keys("2022280026@ogr.deu.edu.tr")
        self.uni.find_element(By.ID, "pw").send_keys("Ksfaq137")
        self.uni.find_element(By.ID, "submit").click()
        
    def uni_scrape(self):
        self.uni.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/nav/div[2]/ul/li[4]/a[3]").click()
        self.uni.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[2]/nav/div[2]/ul/li[4]/ul/li[8]/a").click()
        self.grade = self.uni.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[2]/main/div/div/div/form/div[4]/div[2]/div/table/tbody/tr[1]/td[3]/span").text

    def grade_exist(self):
        if self.grade != "yok":
            return True
        
    def send_grade(self):
        self.msg = MIMEText(self.grade, "plain", "utf-8")
        self.msg["Subject"] = "Technical english"
        self.msg["From"] = "obadahpy@gmail.com"
        self.msg["To"] = "obadah2109@gmail.com"
        self.mail.send_message(self.msg)

