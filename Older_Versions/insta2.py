from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
from urllib import request
import re
import time

driver = webdriver.Chrome('C:\\Users\\zachm\\Documents\\chromedriver_win32\\chromedriver')
url = "https://www.instagram.com/hannah.lutz/"

driver.get(url)

def scrollToBottom(secs):

    while (secs > 0):
        secs -= 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", "")
        time.sleep(1)

scrollToBottom(60)

links = driver.find_elements_by_tag_name("a")

for linkObject in links:
    link = linkObject.get_attribute("href")

    # print(link)

    if re.match(r'(.*)/p/(.*)', link):
        print(link)

        driver2 = webdriver.Chrome('C:\\Users\\zachm\\Documents\\chromedriver_win32\\chromedriver')
        url2 = link
        driver2.get(url2)

        pics = driver2.find_elements_by_tag_name("img")

        i = 0
        for pic in pics:
            src = pic.get_attribute('src')
            print(src)
            # request.urlretrieve(src, "%s.jpg" % i)
            i = i + 1

        driver2.close()

driver.close()