from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QApplication
import sys

class TestWidget(QWidget):

    def __init__(self):
        super(TestWidget, self).__init__()

        self.initUi()
        self.main()

    def initUi(self):
        mainLayout = QVBoxLayout()
        self.butt = QPushButton("push me")
        self.line = QLineEdit()

        mainLayout.addWidget(self.line)
        mainLayout.addWidget(self.butt)

        self.setLayout(mainLayout)

    def main(self):
        pass

