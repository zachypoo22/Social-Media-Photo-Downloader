from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome('C:\\Users\\zachm\\Documents\\chromedriver_win32\\chromedriver')
usr = "zach"
pw = "swag420"

driver.get('http://www.instagram.com')

element = driver.find_element_by_id('email')
element.send_keys(usr)

element =  driver.find_element_by_id('pass')
element.send_keys("pw")

element.send_keys(Keys.RETURN)

driver.close()