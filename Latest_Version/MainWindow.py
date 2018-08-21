from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout,\
    QPushButton, QInputDialog, QComboBox, QDockWidget, QFileDialog
from PyQt5.QtCore import Qt
import sys
from FacebookWindow import FacebookWindow
from VscoWindow import VscoWindow
from InstagramWindow import InstagramWindow
from CenterWidget import CenterWidget
import re
import time
from urllib import request
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options

class MainWindow(QMainWindow):

    # drv = ""

    def __init__(self):
        super().__init__()

        self.Center = CenterWidget()

        self.initUi()
        self.main()

    def initUi(self):

        self.statusBar().showMessage('Pick One')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Picture Finder')

        self.setCentralWidget(self.Center)

        self.show()

    def main(self):
        pass

app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())