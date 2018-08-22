from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout,\
    QPushButton, QInputDialog, QComboBox, QDockWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
import sys
import re
import time
from urllib import request
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options

class InstagramWindow(QWidget):

    addSig = pyqtSignal(list)

    def __init__(self, driver):
        super(InstagramWindow, self).__init__()

        ops = Options()
        ops.add_argument("--disable-notifications")
        self.driver = driver

        self.list = []

        self.height = 100
        self.width = 300
        self.top = 500
        self.left = 500

        self.initUi()
        self.main()

    def initUi(self):
        self.setWindowTitle("Instagram Pics")
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
        # wantToLogin, ok = QInputDialog.getItem(self, "Login", "do you want to login?", ("yes", "no"))
        #
        # if not ok:
        #     print("oops")

        wantToLogin = QMessageBox.question(self, 'Login?', 'Do you want to log in to Instagram?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)


        url = self.urlInput.text()

        # if wantToLogin == "yes":
        if wantToLogin == QMessageBox.Yes:
            myUsername, ok = QInputDialog.getText(self, "Username", "Enter Username:")
            if not ok:
                print('oops')
            myPassword, ok = QInputDialog.getText(self, "Password", "Enter Password:", QLineEdit.Password)
            if not ok:
                print('oops')

            driver = webdriver.Chrome(self.driver)
            loginUrl = "https://www.instagram.com/accounts/login/?hl=en"
            driver.get(loginUrl)
            usr = driver.find_element_by_name("username")
            pwd = driver.find_element_by_name("password")
            usr.send_keys(myUsername)
            pwd.send_keys(myPassword)
            pwd.send_keys(keys.Keys.ENTER)
            time.sleep(5)

        else:
            driver = webdriver.Chrome(self.driver)

        driver.get(url)

        def scrollToBottom(secs):

            while (secs > 0):
                secs -= 1
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", "")
                time.sleep(1)

        scrollToBottom(60)
        links = driver.find_elements_by_tag_name("a")

        picsList = []

        for linkObject in links:
            link = linkObject.get_attribute("href")

            # print(link)

            if re.match(r'(.*)/p/(.*)', link):
                # print(link)

                driver2 = webdriver.Chrome(self.driver)
                url2 = link
                driver2.get(url2)

                pics = driver2.find_elements_by_tag_name("img")

                for pic in pics:
                    src = pic.get_attribute('src')
                    if src not in picsList:
                        picsList.append(src)
                # print(picsList)

                driver2.close()

        i = 0

        for pic in picsList:
            # print(pic)
            self.list.append(pic)


            # src = pic.get_attribute('src')
            # print(src)
            # request.urlretrieve(src, "%s.jpg" % i)
            i = i + 1

        self.addSig.emit(self.list)
        driver.close()

