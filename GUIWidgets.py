import sys
#Requires Installation of PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from newWindow import Ui_newWindow

#Class to initialize a new instance of QApplication module which is required to run PyQt5
class StartApp:
    def __init__(self):
        self.QApp = QApplication(sys.argv)

#Class to create a new window
class NewWindow:
    def __init__(self,name,xlen,ylen):
        #Initialize new instance of window ui
        self.QWin = QMainWindow()
        #Set Window Title
        self.QWin.setWindowTitle(name)
        #Set Window Size
        self.QWin.resize(xlen,ylen)

    #Method to set Window icon image
    def setWindowIcon(self,image):
        self.QWin.setWindowIcon(QtGui.QIcon(image))

class NewLabel:
    def __init__(self):
        pass