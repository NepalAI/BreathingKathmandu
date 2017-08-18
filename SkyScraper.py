import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        '''
        Scrap script
        '''

        myLink = "https://en.wikipedia.org/wiki/Particulates"

        page = urlopen(myLink)

        pageSource = BeautifulSoup(page, "lxml")
        # print(pageSource)

        # extract all tables
        all_tables = pageSource.find_all('table')

        # get the right table by defining its class
        right_table = pageSource.find('table', class_='wikitable')
        print(right_table)

        '''
        Scrap script
        '''

        l1 = QLabel()
        l1.setText("Hello World")


        # textEdit = QTextEdit()
        # self.setCentralWidget(textEdit)


        exitAct = QAction(QIcon('pic.png'), 'Scrap', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        # Declaring the menu bar
        menubar = self.menuBar()

        # File Menu

        fileMenu = menubar.addMenu('&File')

        toolbar = self.addToolBar('Exit')
        fileMenu.addAction(exitAct)

        # Exit Menu

        editMenu = menubar.addMenu('Edit')

        toolbar.addAction(exitAct)
        undoAct = QAction('Undo', self)

        RedoAct = QAction('Redo', self)

        editMenu.addAction(undoAct)
        editMenu.addAction(RedoAct)

        # exitAct is defined up *** PLEASE CHANGE THIS***

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('SkyScraper')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())