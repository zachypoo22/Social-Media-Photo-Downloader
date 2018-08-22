from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
from urllib import request
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QApplication, QToolBar, QAction, QHBoxLayout, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
import sys
import re

class WebWidget(QWidget):
    def __init__(self):
        super(WebWidget, self).__init__()

        self.height = 500
        self.width = 500
        self.top = 0
        self.left = 0

        self.url = ""
        self.picList = []
        self.i = 0

        self.initUi()
        # self.main()

    def initUi(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.rightButton = QPushButton("----->")
        self.saveButton = QPushButton("Save")
        self.saveAllButton = QPushButton("Save All")
        self.leftButton = QPushButton("<-----")
        self.rightButton.clicked.connect(self.next)
        self.leftButton.clicked.connect(self.prev)
        self.saveButton.clicked.connect(self.save)
        self.saveAllButton.clicked.connect(self.saveAll)

        buttLayout = QHBoxLayout()
        buttLayout.addSpacing(80)
        buttLayout.addWidget(self.saveButton)
        buttLayout.addSpacing(30)
        buttLayout.addWidget(self.saveAllButton)
        buttLayout.addSpacing(80)

        navLayout = QHBoxLayout()
        navLayout.addWidget(self.leftButton)
        navLayout.addSpacing(30)
        navLayout.addWidget(self.rightButton)


        mainLayout = QVBoxLayout()
        self.browser = QWebEngineView()
        # self.browser.setUrl(QUrl(self.url))

        mainLayout.addLayout(navLayout)
        mainLayout.addWidget(self.browser)
        mainLayout.addLayout(buttLayout)

        self.setLayout(mainLayout)

    def setWebUrl(self, url):
        self.browser.setUrl(QUrl(url))

    def next(self):
        if self.i < len(self.picList)-1:
            self.i += 1
        else:
            # print('oops')
            self.i = 0
        try:
            self.setWebUrl(self.picList[self.i])
        except Exception as e:
            print(e)

    def prev(self):
        if self.i > 0:
            self.i -= 1
        else:
            # print('oops')
            self.i = len(self.picList)-1

        self.setWebUrl(self.picList[self.i])

    def start(self):
        # print('2')
        try:
            # print(self.picList[0])
            self.setWebUrl(self.picList[0])
        except Exception as e:
            print(e)

    def addToList(self, list):
        # print('1')
        try:
            self.picList.extend(list)
            # print(self.picList)
        except Exception as e:
            print(e)

    def save(self):
        name = QFileDialog.getSaveFileName(self, 'save file')
        filename = ""
        if not re.match("(.+)\.(.+)", name[0]):
            filename = "%s.jpg" % name[0]
        else:
            filename = name[0]

        try:
            request.urlretrieve(self.picList[self.i], filename)
        except Exception as e:
            print(e)

    def saveAll(self):
        name = QFileDialog.getSaveFileName(self, 'save file')

        filename = ""
        if not re.match("(.+)\.(.+)", name[0]):
            filename = name[0]
        else:
            filename = name[0].split('.')[0]

        j = 0
        for pic in self.picList:
            try:
                request.urlretrieve(pic, "%s%d.jpg" % (filename, j))
            except Exception as e:
                print(e)
            j += 1