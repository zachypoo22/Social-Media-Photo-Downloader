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

class VscoWindow(QWidget):

    addSig = pyqtSignal(list)

    def __init__(self, driver):
        super(VscoWindow, self).__init__()

        ops = Options()
        ops.add_argument("--disable-notifications")
        self.driver = driver

        self.height = 100
        self.width = 300
        self.top = 500
        self.left = 500

        self.list = []

        self.initUi()
        self.main()

    def initUi(self):
        self.setWindowTitle("VSCO Pics")
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
        self.submitButton.clicked.connect(self.clk)

    def clk(self):
        url = self.urlInput.text()
        driver = webdriver.Chrome(self.driver)
        driver.get(url)

        linksList = []
        nextPage = driver.find_element_by_xpath("//a[@title='Next']")
        nextLink = nextPage.get_attribute('href')

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
                self.list.append(source)

        self.addSig.emit(self.list)
        driver.close()
        self.close()
