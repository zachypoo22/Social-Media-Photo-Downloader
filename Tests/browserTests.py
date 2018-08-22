from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
from urllib import request
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys

class BrowserTests(QWidget):

    def __init__(self):
        super(BrowserTests, self).__init__()

        self.initUi()
        # self.main()

    def initUi(self):
        mainLayout = QVBoxLayout()
        self.butt = QPushButton("push me")
        self.line = QLineEdit()

        self.webView = QWebEngineView()
        self.webView.setUrl(QUrl("https://www.google.com"))

        mainLayout.addWidget(self.line)
        mainLayout.addWidget(self.butt)
        mainLayout.addWidget(self.webView)

        self.setLayout(mainLayout)

        self.show()

    def main(self):
        driver = webdriver.Chrome('C:\\Users\\zachm\\Documents\\chromedriver_win32\\chromedriver')
        url = "https://www.instagram.com/p/BmoMYKPH2PF/?taken-by=hannah.lutz"

        driver.get(url)

        pics = driver.find_elements_by_tag_name("img")

        picList = []
        i = 0
        for pic in pics:
            src = pic.get_attribute('src')
            picList.append(src)
            # request.urlretrieve(src, "%s.jpg" % i)
            # i = i + 1

app = QApplication(sys.argv)
win = BrowserTests()
sys.exit(app.exec_())