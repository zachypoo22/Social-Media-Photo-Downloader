from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout,\
    QPushButton, QInputDialog, QComboBox, QDockWidget, QFileDialog
from PyQt5.QtCore import Qt, pyqtSignal
import sys
import re
import time
from urllib import request
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options

class FacebookWindow(QWidget):

    addSig = pyqtSignal(list)

    def __init__(self, driver):
        super(FacebookWindow, self).__init__()

        self.height = 100
        self.width = 300
        self.top = 500
        self.left = 500

        self.list = []

        ops = Options()
        ops.add_argument("--disable-notifications")
        self.driver = driver

        self.initUi()
        self.main()

    def initUi(self):
        self.setWindowTitle("Facebook Pics")
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainLayout = QVBoxLayout()

        # labels
        urlLabel = QLabel("Enter URL:")

        # inputs
        self.urlInput = QLineEdit()

        # buttons
        self.submitButton = QPushButton("GO!")

        # setup layouts
        mainLayout.addWidget(urlLabel)
        mainLayout.addWidget(self.urlInput)
        mainLayout.addWidget(self.submitButton)

        self.setLayout(mainLayout)

    def main(self):
        self.submitButton.clicked.connect(self.click)

    def click(self):

        url = self.urlInput.text()

        # get login creds
        myUserName, good = QInputDialog.getText(self, "Username", "Input Username")

        if not good:
            print("oops")

        myPassword, good = QInputDialog.getText(self, "Password", "Input Password")

        if not good:
            print('oops')

        ops = Options()
        ops.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(self.driver,
                                       options=ops)

        def scrollToBottom(secs):
            # print('3')
            while (secs > 0):
                secs -= 1
                try:
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", "")
                except Exception as e:
                    print(e)
                # print('4')
                time.sleep(2)

        loginUrl = "https://www.facebook.com"
        self.driver.get(loginUrl)

        usr = self.driver.find_element_by_name("email")
        pwd = self.driver.find_element_by_name("pass")
        usr.send_keys(myUserName)
        pwd.send_keys(myPassword)
        pwd.send_keys(keys.Keys.ENTER)
        time.sleep(3)
        self.driver.get(url)

        # get other photos link
        otherPhotosLink = ""
        dummyLink = self.driver.find_elements_by_class_name("_3c_")
        for l in dummyLink:
            link = l.get_attribute("href")
            # print(link)
            if re.match("(.*)/photos_all(.*)", link):
                otherPhotosLink = link


        # scroll down
        scrollToBottom(20)

        # get all pic page links
        listOfLinks = []
        dummyLink = self.driver.find_elements_by_class_name("uiMediaThumb")
        for link in dummyLink:
            picLink = link.get_attribute("href")
            listOfLinks.append(picLink)

        for l in listOfLinks:
            # print(l)
            self.driver.get(l)
            time.sleep(2)
            pics = self.driver.find_elements_by_class_name("spotlight")
            for pic in pics:
                plink = pic.get_attribute("src")
                self.list.append(plink)  # would save here but....testing

        print("------going to other photos page -------")
        self.driver.get(otherPhotosLink)
        listOfLinks.clear()

        # scroll down again
        scrollToBottom(30)

        # get these photos
        dummyLink = self.driver.find_elements_by_class_name("uiMediaThumb")
        for link in dummyLink:
            picLink = link.get_attribute("href")
            listOfLinks.append(picLink)

        for l in listOfLinks:
            # print(l)
            self.driver.get(l)
            time.sleep(2)
            pics = self.driver.find_elements_by_class_name("spotlight")

            for pic in pics:
                try:
                    plink = pic.get_attribute("src")
                    self.list.append(plink)
                except Exception as e:
                    print(e)

        self.addSig.emit(self.list)
        self.driver.close()
        self.close()

