from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
print("NOTE: Group ID is the part of group link which comes after https://meetup.com/ and next / : /n")
def modifyforfile(data):
    return data + '\n'
f =  open("config.txt" , "r")
groupids =f.readlines()
f.close()
temp = input("Please enter a group ID or n to exit: ")
if temp != "n":
    groupids.append(temp)
f = open("config.txt" , "w")
for i in groupids:
    f.write(modifyforfile(i))
f.close()
email = input("Please enter your email address: ")
password = input("Please enter your password: ")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://meetup.com/login")

signup = driver.find_element(By.ID,"email")
signup.send_keys(email)
time.sleep(1)
signup = driver.find_element(By.ID,"current-password")
signup.send_keys(password + Keys.ENTER)
n = 0
while n < len(groupids):
    if groupids[n] != "":
        driver.get("https://meetup.com/"+groupids[n]+"/events/")
        k = 1
        while True:
            try:
                eventname = "event-card-e-" + k
                signup = driver.find_element(By.ID,eventname)
                signup.click()
                k += 1
            except:
                break
                                     
    n += 1
driver.quit() 



              
            