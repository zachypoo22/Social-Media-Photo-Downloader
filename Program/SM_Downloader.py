from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout,\
    QPushButton, QInputDialog, QComboBox, QDockWidget, QFileDialog
from PyQt5.QtCore import Qt
import sys
import re
import time
from urllib import request
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options

class MainWindow(QMainWindow):

    drv = ""

    def __init__(self):
        super().__init__()

        self.MW = self.MainWidget()

        self.initUi()
        self.main()

    def initUi(self):

        self.statusBar().showMessage('Pick One')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Picture Finder')

        self.setCentralWidget(self.MW)

        self.show()

    def setDriver(self, s):
        MainWindow.drv = s
        print('setting drv')
        print(s)
        print(MainWindow.drv)

    def getDriver(self):
        return MainWindow.drv

    def main(self):
        pass


    class MainWidget(QWidget):

        class VscoWindow(QWidget):
            def __init__(self):
                super().__init__()

                self.height = 100
                self.width = 300
                self.top = 500
                self.left = 500

                self.setupUi()
                self.main()

            def setupUi(self):
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
                self.show()

            def main(self):
                self.submitButton.clicked.connect(self.clk)

            def clk(self):
                url = self.urlInput.text()
                driver = webdriver.Chrome(MainWindow.drv)
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
                        print(source)

                driver.close()

        class FBWindow(QWidget):
            def __init__(self):
                super().__init__()

                self.height = 100
                self.width = 300
                self.top = 500
                self.left = 500

                self.driver = MainWindow.drv

                self.setupUi()
                self.main()

            def setupUi(self):
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
                self.show()

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

                print('2')
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
                        print(plink)  # would save here but....testing

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
                        plink = pic.get_attribute("src")
                        print(plink)  # again, would save but still testing

                self.driver.close()

        class InstaWindow(QWidget):

            def __init__(self):
                super().__init__()

                self.height = 100
                self.width = 300
                self.top = 500
                self.left = 500

                self.setupUi()
                self.main()

            def setupUi(self):
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

                self.show()

            def click(self):
                wantToLogin, ok = QInputDialog.getItem(self, "Login", "do you want to login?", ("yes", "no"))

                if not ok:
                    print("oops")

                url = self.urlInput.text()

                if wantToLogin == "yes":
                    myUsername, ok = QInputDialog.getText(self, "Username", "Enter Username:")
                    if not ok:
                        print('oops')
                    myPassword, ok = QInputDialog.getText(self, "Password", "Enter Password:")
                    if not ok:
                        print('oops')

                    driver = webdriver.Chrome(MainWindow.drv)
                    loginUrl = "https://www.instagram.com/accounts/login/?hl=en"
                    driver.get(loginUrl)
                    usr = driver.find_element_by_name("username")
                    pwd = driver.find_element_by_name("password")
                    usr.send_keys(myUsername)
                    pwd.send_keys(myPassword)
                    pwd.send_keys(keys.Keys.ENTER)
                    time.sleep(5)

                else:
                    driver = webdriver.Chrome(MainWindow.drv)

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

                        driver2 = webdriver.Chrome(MainWindow.drv)
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
                    print(pic)
                    # src = pic.get_attribute('src')
                    # print(src)
                    # request.urlretrieve(src, "%s.jpg" % i)
                    i = i + 1

                driver.close()

            def main(self):
                self.submitButton.clicked.connect(self.click)

        def __init__(self):
            super().__init__()

            # self.IGW = self.InstaWindow()
            # self.FBW = self.FBWindow()
            print(MainWindow.drv)
            self.driver = MainWindow.drv
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

            self.show()

        def boxActivated(self, text):
            self.choice = text

        def clk(self):
            if MainWindow.drv == "":
                fname = QFileDialog.getOpenFileName(self, 'open driver')
                try:
                    MainWindow.drv = fname[0]
                except Exception as e:
                    print(e)

            if self.choice == "Facebook":
                self.FBW = self.FBWindow()
                self.FBW.show()
            elif self.choice == "Instagram":
                self.IGW = self.InstaWindow()
                self.IGW.show()
            elif self.choice == "Vsco":
                self.VSW = self.VscoWindow()
                self.VSW.show()
            else:
                print('oops')

        def main(self):

            self.option.activated[str].connect(self.boxActivated)
            self.button.clicked.connect(self.clk)

            # self.dialog = self.InstaWindow()
            # self.dialog.show()


app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())