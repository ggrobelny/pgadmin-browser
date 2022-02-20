import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://127.0.0.1:5050'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.setWindowTitle(
            "For pgAdmin4 browser")
        #self.setIcon()
        self.setWindowIcon(QtGui.QIcon('pgadmin-icon.png'))
        self.setStyleSheet("QToolBar { background-color: rgb(51,102,153)} ")

     
    #def setIcon(self):
        #appIcon = QIcon("aniol_transparent.ico")
        #self.setWindowIcon(appIcon)

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        navbar.addSeparator()

        back_btn = QAction('<<', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        navbar.addSeparator()
        
        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        navbar.addSeparator()

        forward_btn = QAction('>>', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        navbar.addSeparator()

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        navbar.addSeparator()

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://127.0.0.1:5050'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
