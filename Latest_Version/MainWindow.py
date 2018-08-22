from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout,\
    QPushButton, QInputDialog, QComboBox, QDockWidget, QFileDialog, QDockWidget
from PyQt5.QtCore import Qt
import sys
from FacebookWindow import FacebookWindow
from VscoWindow import VscoWindow
from InstagramWindow import InstagramWindow
from CenterWidget import CenterWidget
from WebWidget import WebWidget
import re
import time
from urllib import request
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        self.Center = CenterWidget()
        self.WebWidget = WebWidget()

        self.height = 100
        self.width = 250
        self.top = 150
        self.left = 500

        self.linkList = []

        self.initUi()
        self.main()

    def initUi(self):
        self.statusBar().showMessage('Pick One')

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle('Picture Finder')

        self.setCentralWidget(self.Center)

        # dock widget
        webBrowser = QDockWidget("Picture Browser")
        webBrowser.setWidget(self.WebWidget)
        webBrowser.setGeometry(500,300,500,500)

        self.Center.addSig.connect(self.addToFinalList)

        self.addDockWidget(Qt.RightDockWidgetArea, webBrowser)
        webBrowser.setFloating(True)
        self.show()

    def addToFinalList(self, list):
        self.linkList.extend(list)
        self.WebWidget.addToList(self.linkList)
        self.linkList.clear()
        self.WebWidget.start()

    def main(self):
        pass
        # self.WebWidget.setWebUrl('https://im.vsco.co/aws-us-west-2/0feb46/31366164/5b79d0f07b6b841a111d2ff2/vsco5b79d0f4c8c7e.jpg?w=824&dpr=1')

app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())