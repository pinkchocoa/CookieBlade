import sys
#Requires Installation of PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from GUIWidgets import *
from newWindow import Ui_newWindow

class GUIWindow:
    def __init__(self, Window):
        self.setSearchButton(Window)
    
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
WindowLogo = NewLabel(MainWindow.QWin, 230, 70, 331, 81)
WindowLogo.setText("")
WindowLogo.setImage("GUIMainLogo.PNG")
URLLabel = NewLabel(MainWindow.QWin,60, 160, 61, 31)
URLLabel.setText("Enter URL:")
UIDLabel = NewLabel(MainWindow.QWin,260, 200, 61, 31)
UIDLabel.setText("Enter UID:")
URLBox = NewTextBox(MainWindow.QWin, 120, 160, 591, 31)
URLBox.setPlaceHolderText("Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>")
TUIDBox = NewTextBox(MainWindow.QWin, 120, 200, 591, 31)
TUIDBox.setPlaceHolderText("Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>")
ui = GUIWindow(MainWindow.QWin)
MainWindow.QWin.show()
sys.exit(App.QApp.exec_())


