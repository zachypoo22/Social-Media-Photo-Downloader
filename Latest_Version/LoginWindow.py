from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QApplication
import sys

class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.initUi()
        self.main()

    def initUi(self):
        self.userInput = QLineEdit()
        self.passInput = QLineEdit()
        self.button = QPushButton("Submit")

        userLayout = QHBoxLayout()
        passLayout = QHBoxLayout()

        userLayout.addWidget(QLabel('Username'))
        userLayout.addWidget(self.userInput)
        passLayout.addWidget(QLabel('Password'))
        passLayout.addWidget(self.passInput)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(userLayout)
        mainLayout.addLayout(passLayout)
        mainLayout.addWidget(self.button)

        self.setWindowTitle('Login')
        self.setLayout(mainLayout)
        # self.show()

    def main(self):
        pass

