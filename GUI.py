import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from newWindow import Ui_newWindow

class GUIWindow:
    def __init__(self, Window):
        Window.setObjectName("MainWindow")
        Window.resize(800, 600)
        Window.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
        Window.setWindowTitle("Cookie Crawler")
        self.centralwidget = QtWidgets.QWidget(Window)
        Window.setCentralWidget(self.centralwidget)
        self.setLabel(Window)
        self.setLogo(Window)
        self.setTextBox(Window)
        self.setSearchButton(Window)
        
    def setLabel(self, Window):
        self.labelUID = QtWidgets.QLabel(self.centralwidget)
        self.labelUID.setGeometry(QtCore.QRect(260, 200, 61, 31))
        self.labelUID.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUID.setObjectName("labelUID")
        self.labelUID.setText("Enter UID:")
        self.labelPW = QtWidgets.QLabel(self.centralwidget)
        self.labelPW.setGeometry(QtCore.QRect(230, 240, 91, 31))
        self.labelPW.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPW.setText("Enter Password:")
        self.labelURL = QtWidgets.QLabel(self.centralwidget)
        self.labelURL.setGeometry(QtCore.QRect(60, 160, 61, 31))
        self.labelURL.setAlignment(QtCore.Qt.AlignCenter)
        self.labelURL.setText("Enter URL:")

    def setLogo(self, Window):
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(230, 70, 331, 81))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("GUIMainLogo.PNG"))
        self.logo.setScaledContents(True)
    
    def setTextBox(self, Window):
        self.urlbox = QtWidgets.QLineEdit(self.centralwidget)
        self.urlbox.setGeometry(QtCore.QRect(120, 160, 591, 31))
        self.urlbox.setPlaceholderText("Enter Youtube Channel URL")
        self.uidbox = QtWidgets.QLineEdit(self.centralwidget)
        self.uidbox.setGeometry(QtCore.QRect(320, 200, 181, 31))
        self.uidbox.setPlaceholderText("Enter Twitter UID")
        self.pwbox = QtWidgets.QLineEdit(self.centralwidget)
        self.pwbox.setGeometry(QtCore.QRect(320, 240, 181, 31))
        self.pwbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwbox.setPlaceholderText("Enter Twitter Password")
    
    def setSearchButton(self, Window):
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(370, 280, 81, 41))
        self.SearchButton.setText("Search")
        self.SearchButton.clicked.connect(self.searchClicked)
    
    def searchClicked(self):
        self.yturl = self.urlbox.text()
        self.tuid = self.uidbox.text()
        self.tpw = self.pwbox.text()
        if (self.yturl == "" or self.tuid == "" or self.tpw == ""):
            showerror = self.errorMsgBox()
        else:
            self.newwin = QtWidgets.QMainWindow()
            self.newui = Ui_newWindow()
            self.newui.setupUi(self.newwin)
            self.newui.label_2 .setText(self.yturl)
            self.newui.label_2.adjustSize()
            self.newui.label_3.setText(self.tuid)
            self.newui.label_3.adjustSize()
            self.newui.label_4.setText(self.tpw)
            self.newui.label_4.adjustSize()
            self.newwin.show()


    def errorMsgBox(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Error!")
        msgBox.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Error! Missing Input!")
        error = msgBox.exec_()

app = QtWidgets.QApplication(sys.argv)
win = QtWidgets.QMainWindow()
ui = GUIWindow(win)
win.show()
sys.exit(app.exec_())