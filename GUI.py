import sys
#Requires Installation of PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from GUIWidgets import *
from newWindow import Ui_newWindow

class GUIWindow:
    def __init__(self, Window):
        self.setLabel(Window)
        self.setLogo(Window)
        self.setTextBox(Window)
        self.setSearchButton(Window)
        
    def setLabel(self, Window):
        self.labelUID = QLabel(Window)
        self.labelUID.setGeometry(QtCore.QRect(260, 200, 61, 31))
        self.labelUID.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUID.setObjectName("labelUID")
        self.labelUID.setText("Enter UID:")
        self.labelURL = QLabel(Window)
        self.labelURL.setGeometry(QtCore.QRect(60, 160, 61, 31))
        self.labelURL.setAlignment(QtCore.Qt.AlignCenter)
        self.labelURL.setText("Enter URL:")

    def setLogo(self, Window):
        self.logo = QLabel(Window)
        self.logo.setGeometry(QtCore.QRect(230, 70, 331, 81))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("GUIMainLogo.PNG"))
        self.logo.setScaledContents(True)
    
    def setTextBox(self, Window):
        self.urlbox = QLineEdit(Window)
        self.urlbox.setGeometry(QtCore.QRect(120, 160, 591, 31))
        self.urlbox.setPlaceholderText("Enter Youtube Channel URL")
        self.uidbox = QLineEdit(Window)
        self.uidbox.setGeometry(QtCore.QRect(320, 200, 181, 31))
        self.uidbox.setPlaceholderText("Enter Twitter UID")
    
    def setSearchButton(self, Window):
        self.SearchButton = QPushButton(Window)
        self.SearchButton.setGeometry(QtCore.QRect(370, 280, 81, 41))
        self.SearchButton.setText("Search")
        self.SearchButton.clicked.connect(self.searchClicked)
    
    def searchClicked(self):
        self.yturl = self.urlbox.text()
        self.tuid = self.uidbox.text()
        if (self.yturl == "" or self.tuid == ""):
            showerror = self.errorMsgBox()
        else:
            self.newwin = QMainWindow()
            self.newui = Ui_newWindow()
            self.newui.setupUi(self.newwin)
            self.newui.label_2 .setText(self.yturl)
            self.newui.label_2.adjustSize()
            self.newui.label_3.setText(self.tuid)
            self.newui.label_3.adjustSize()
            self.newwin.show()

    def errorMsgBox(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Error!")
        msgBox.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Error! Missing Input!")
        error = msgBox.exec_()

App = StartApp()
MainWindow = NewWindow("Cookie Crawler", 800, 600)
MainWindow.setWindowIcon("CookieIcon.png")
ui = GUIWindow(MainWindow.QWin)
MainWindow.QWin.show()
sys.exit(App.QApp.exec_())


