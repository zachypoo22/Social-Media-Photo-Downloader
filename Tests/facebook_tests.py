from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
from urllib import request
import re
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options

ops = Options()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome('C:\\Users\\zachm\\Documents\\chromedriver_win32\\chromedriver', options=ops)
url = "https://www.facebook.com/michelle.richwine/photos?lst=1347936816%3A1176673711%3A1534799573"
# driver.get(url)

# LOGIN
# ---------
loginUrl = "https://www.facebook.com/"
driver.get(loginUrl)
myUsername = "sensizachattack@aol.com"
myPassword = "H3llonub@"

usr = driver.find_element_by_name("email")
pwd = driver.find_element_by_name("pass")
usr.send_keys(myUsername)
pwd.send_keys(myPassword)
pwd.send_keys(keys.Keys.ENTER)
time.sleep(5)
driver.get(url)
# -----------

# get "whoever's photos"
# ----------------
# link2 = driver.find_elements_by_class_name("_3c_")
# for l in link2:
#     link = l.get_attribute("href")
#     # print(link)
#     if re.match("(.*)/photos_all(.*)", link):
#         print(link)
# ----------------

# get links to each pic
# ----------
# links = driver.find_elements_by_class_name("uiMediaThumb")
# for link in links:
#     picLink = link.get_attribute("href")
#     print(picLink)
# ----------

# make a list of links to each pic
# ----------
# listOfLinks = []
# links = driver.find_elements_by_class_name("uiMediaThumb")
# for link in links:
#     picLink = link.get_attribute("href")
#
#     listOfLinks.append(picLink)
#     print(listOfLinks)
# ----------


# get pic pink from theater
# --------------
# thisUrl = "https://www.facebook.com/photo.php?fbid=10213328871474405&set=t.1176673711&type=3&theater"
# # thisDriver = webdriver.Chrome('C:\\Users\\zachm\\Documents\\chromedriver_win32\\chromedriver')
# driver.get(thisUrl)
#
# pics = driver.find_elements_by_class_name("spotlight")
# for pic in pics:
#     plink = pic.get_attribute("src")
#     print(plink)
# --------------

# scroll down
# --------
# def scrollToBottom(secs):
#
#     while (secs > 0):
#         secs -= 1
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", "")
#         time.sleep(1)
#
# scrollToBottom(60)
# --------