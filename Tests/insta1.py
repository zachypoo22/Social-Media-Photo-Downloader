from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
from urllib import request

driver = webdriver.Chrome('C:\\Users\\zachm\\Documents\\chromedriver_win32\\chromedriver')
url = "https://www.instagram.com/p/BmoMYKPH2PF/?taken-by=hannah.lutz"

driver.get(url)

pics = driver.find_elements_by_tag_name("img")

i = 0
for pic in pics:
    src = pic.get_attribute('src')
    # print(src)
    request.urlretrieve(src, "%s.jpg" % i)
    i = i + 1
