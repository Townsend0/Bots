import time
from data import *

a = UniBot()
while True:
    a.uni_login()
    a.uni_scrape()
    if a.grade_exist():
        a.set_mail()
        a.send_grade()
        a.uni.quit()
        break
    a.uni.quit()
    time.sleep(300)
    