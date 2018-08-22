from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout,\
    QPushButton, QInputDialog, QComboBox, QDockWidget, QFileDialog
from PyQt5.QtCore import Qt, pyqtSignal
import sys
from FacebookWindow import FacebookWindow
from VscoWindow import VscoWindow
from InstagramWindow import InstagramWindow
import re
import time
from urllib import request
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options

class CenterWidget(QWidget):

    addSig = pyqtSignal(list)

    def __init__(self):
        super(CenterWidget, self).__init__()

        self.driver = ""
        self.choice = "Facebook"

        self.initUi()
        self.main()

    def initUi(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Picture Finder2')

        self.button = QPushButton("Submit")

        self.option = QComboBox()
        self.option.addItem("Facebook")
        self.option.addItem("Instagram")
        self.option.addItem("Vsco")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.option)
        mainLayout.addWidget(self.button)


        self.setLayout(mainLayout)

    def addToList(self, list):
        self.addSig.emit(list)

    def boxActivated(self, text):
        self.choice = text

    def clk(self):
        if self.driver == "":
            fname = QFileDialog.getOpenFileName(self, 'open driver')
            try:
                self.driver = fname[0]
            except Exception as e:
                print(e)

        if self.choice == "Facebook":

            try:
                self.FBW = FacebookWindow(self.driver)
                self.FBW.addSig.connect(self.addToList)
                self.FBW.show()
            except Exception as e:
                print(e)
        elif self.choice == "Instagram":
            self.IGW = InstagramWindow(self.driver)

            # signals
            self.IGW.addSig.connect(self.addToList)

            self.IGW.show()
        elif self.choice == "Vsco":
            self.VSW = VscoWindow(self.driver)
            self.VSW.addSig.connect(self.addToList)
            self.VSW.show()
        else:
            print('oops')

    def main(self):
        self.option.activated[str].connect(self.boxActivated)
        self.button.clicked.connect(self.clk)
