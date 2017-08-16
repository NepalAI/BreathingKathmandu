import sys
from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 1000, 700)
        self.setWindowTitle('SkyScraper')
        # self.setWindowIcon(QIcon('pic.png'))

        # File>>Options list are defined here

        fileNew = QAction('&New', self)
        fileNew.setShortcut('Ctrl+N')
        fileNew.setStatusTip('leave the app')
        fileNew.triggered.connect(self.close_application)

        fileExit = QAction('&Exit', self)
        fileExit.setShortcut('Ctrl+Q')
        fileExit.setStatusTip('leave the app')
        fileExit.triggered.connect(self.close_application)

        self.statusBar()

        # File option

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(fileNew)
        fileMenu.addAction(fileExit)

        extractAction = QAction(QIcon('pic.png'), 'flee the scene', self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)

        self.home()

    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(500, 600)

        self.show()

    def close_application(self):
        print('whooo so custom')
        sys.exit()

if __name__ == "__main__":
    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()




