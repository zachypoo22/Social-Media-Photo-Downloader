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
url = "https://vsco.co/allyrichwine/images/1"
driver.get(url)


# click to next page, collect all links to pics, get actual source links
linksList = []
nextPage = driver.find_element_by_xpath("//a[@title='Next']")
nextLink = nextPage.get_attribute('href')
print(nextLink)
driver.get(nextLink)
time.sleep(3)
while True:
    if re.match("(.*)/images/1", driver.current_url):
        break


    # get all the links to pix
    linksObject = driver.find_elements_by_tag_name("a")
    for link in linksObject:
        l = link.get_attribute('href')
        if re.match("(.*)/media/(.*)", l):
            linksList.append(l)



    nextPage = driver.find_element_by_xpath("//a[@title='Next']")
    nextLink = nextPage.get_attribute('href')

    driver.get(nextLink)
    time.sleep(3)

for link in linksList:
    driver.get(link)
    linkObj = driver.find_elements_by_tag_name('img')
    for l in linkObj:
        source = l.get_attribute('src')
        print(source)
# ---------