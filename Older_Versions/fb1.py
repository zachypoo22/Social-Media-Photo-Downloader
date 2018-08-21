from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
from urllib import request
import re
import time
from selenium.webdriver.chrome.options import Options

ops = Options()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome('C:\\Users\\zachm\\Documents\\chromedriver_win32\\chromedriver', options=ops)
url = "https://www.facebook.com/michelle.richwine/photos?lst=1347936816%3A1176673711%3A1534799573"

def scrollToBottom(secs):

    while (secs > 0):
        secs -= 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", "")
        time.sleep(1)

#login
loginUrl = "https://www.facebook.com/"
driver.get(loginUrl)
myUsername = ""
myPassword = ""

usr = driver.find_element_by_name("email")
pwd = driver.find_element_by_name("pass")
usr.send_keys(myUsername)
pwd.send_keys(myPassword)
pwd.send_keys(keys.Keys.ENTER)
time.sleep(5)
driver.get(url)

# get other photos link
otherPhotosLink = ""
dummyLink = driver.find_elements_by_class_name("_3c_")
for l in dummyLink:
    link = l.get_attribute("href")
    # print(link)
    if re.match("(.*)/photos_all(.*)", link):
        otherPhotosLink = link

# scroll down
scrollToBottom(20)

# get all pic page links
listOfLinks = []
dummyLink = driver.find_elements_by_class_name("uiMediaThumb")
for link in dummyLink:
    picLink = link.get_attribute("href")
    listOfLinks.append(picLink)

for l in listOfLinks:
    # print(l)
    driver.get(l)
    time.sleep(2)
    pics = driver.find_elements_by_class_name("spotlight")
    for pic in pics:
        plink = pic.get_attribute("src")
        print(plink)

print("------going to other photos page -------")
driver.get(otherPhotosLink)
listOfLinks.clear()


# scroll down again
scrollToBottom(30)

dummyLink = driver.find_elements_by_class_name("uiMediaThumb")
for link in dummyLink:
    picLink = link.get_attribute("href")
    listOfLinks.append(picLink)

for l in listOfLinks:
    # print(l)
    driver.get(l)
    time.sleep(2)
    pics = driver.find_elements_by_class_name("spotlight")
    for pic in pics:
        plink = pic.get_attribute("src")
        print(plink)

driver.close()