from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
import sys
from testWidget import TestWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.tw = TestWidget()

        self.initUi()
        self.main()

    def initUi(self):
        self.statusBar().showMessage('Pick One')
        self.setWindowTitle('main window')

        self.setCentralWidget(self.tw)

        self.show()

    def main(self):
        pass

app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())