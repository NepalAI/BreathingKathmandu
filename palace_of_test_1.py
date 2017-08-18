import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from urllib.request import urlopen
from bs4 import BeautifulSoup


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    l1 = QLabel()
    l2 = QLabel()
    l3 = QLabel()
    l4 = QLabel()

    myLink = "https://en.wikipedia.org/wiki/Particulates"

    page = urlopen(myLink)

    pageSource = BeautifulSoup(page, "lxml")
    # print(pageSource)

    # extract all tables
    all_tables = pageSource.find_all('table')

    # get the right table by defining its class
    right_table = pageSource.find('table', class_='wikitable')
    # print(right_table)
    cleantext = BeautifulSoup(right_table).text

    # l1.setText(cleantext)
    print(cleantext)
    l4.setText("<b>Better code now!</b>")
    l2.setText("welcome to Python GUI Programming")


    l3.setPixmap(QPixmap("pic.png"))

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()
    vbox.addWidget(l4)

    l1.setOpenExternalLinks(True)
    l4.linkActivated.connect(clicked)
    l2.linkHovered.connect(hovered)

    win.setLayout(vbox)

    win.setWindowTitle("QLabel Demo")
    win.show()
    sys.exit(app.exec_())


def hovered():
    print
    "hovering"


def clicked():
    print
    "clicked"


if __name__ == '__main__':
    window()