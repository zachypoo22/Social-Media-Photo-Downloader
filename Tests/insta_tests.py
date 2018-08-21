from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
from urllib import request
import re
import time

driver = webdriver.Chrome('C:\\Users\\zachm\\Documents\\chromedriver_win32\\chromedriver')
url = ""

driver.get(url)


# LOGIN
#--------------
# myUsername = ""
# myPassword = ""
# loginUrl = "https://www.instagram.com/accounts/login/?hl=en"
# driver.get(loginUrl)
# usr = driver.find_element_by_name("username")
# pwd = driver.find_element_by_name("password")
# usr.send_keys(myUsername)
# pwd.send_keys(myPassword)
# pwd.send_keys(keys.Keys.ENTER)
# time.sleep(5)
# driver.get(url)
#--------------

# SCROLL TO BOTTOM
#-------------------------------
# def scrollToBottom(secs):
#
#     while (secs > 0):
#         secs -= 1
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", "")
#         time.sleep(1)
#
# scrollToBottom(40)
#-------------------------------