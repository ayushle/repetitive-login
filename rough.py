'''import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Initiliaze Webdriver
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


def FacebookLogin():
    # Enter Your Email ID And Password
    user = input('Enter Email Id:')
    password = input('Enter Password:')

    # Opening Facebook.
    driver.get('https://www.facebook.com/')
    print("Facebook Opened")
    time.sleep(1)

    # Entering Email and Password
    username_box = driver.find_element_by_id('email')
    username_box.send_keys(user)
    print("Email Id entered")
    time.sleep(1)

    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(password)
    print("Password entered")

    # Pressing The Login Button
    login_box = driver.find_element_by_id('loginbutton')
    login_box.click()

    print("Done")
    input('Press anything to quit')
    driver.quit()
    print("Finished")


FacebookLogin()'''

'''
st=[]
wrd=str(input("words: "))
while wrd!='0':
    st.append(wrd)
    wrd = str(input("words: "))

date=[]
dat=input("dd/mm/yyyy: ")
while dat!='0':
    date.append(dat)
    dat=input("dd/mm/yyyy: ")

ph_num=[]
ph_no=input("ph no :")
while ph_no!='0':
    ph_num.append(ph_no)
    ph_no=input("ph no :")

symbol=['@','&']

number=[0,1,2,3,4,5,6,7,8,9]'''

import resources as rs

print(rs.st)

pr_1=[]

pr_1=rs.st
k=len(rs.st)
i=0
while (i<k):
    pr_1.append(rs.st[i].upper())
    pr_1.append(rs.st[i][0].upper()+rs.st[i][1:])
    i+=1
print(pr_1)



























