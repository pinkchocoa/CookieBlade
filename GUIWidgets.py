import sys
#Requires Installation of PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from newWindow import Ui_newWindow

#Class to initialize a new instance of QApplication module which is required to run PyQt5
class StartApp:
    def __init__(self):
        self.QApp = QApplication(sys.argv)

#Class to create a new Window
class NewWindow:
    def __init__(self, name, lenx, leny):
        #Initialize new instance of Window UI
        self.QWin = QMainWindow()
        #Set Window Title
        self.QWin.setWindowTitle(name)
        #Set Window Size
        self.QWin.resize(lenx,leny)

    #Method to set Window icon image
    def setWindowIcon(self,image):
        self.QWin.setWindowIcon(QtGui.QIcon(image))

#Class to create a new Label
class NewLabel:
    def __init__(self, Window, posx, posy, lenx, leny):
        #Initialize new instance of Label UI
        self.label = QLabel(Window)
        #Set window x & y position and window size
        self.label.setGeometry(QtCore.QRect(posx,posy,lenx,leny))
        #Set alignment of Label text to align center
        self.label.setAlignment(QtCore.Qt.AlignCenter)

    #Method to set Label Text
    def setText(self, text):
        self.label.setText(text)
    
    #Method to display image in Label
    def setImage(self, image):
        #Set display image in parameter in Label
        self.label.setPixmap(QtGui.QPixmap(image))
        #Enable image scaling to fit Label size
        self.label.setScaledContents(True)

#Class to create new TextBox
class NewTextBox:
    def __init__(self, Window, posx, posy, lenx, leny):
        #Initialize new instance of TextBox UI
        self.textbox = QLineEdit(Window)
        #Set window x & y position and window size
        self.textbox.setGeometry(QtCore.QRect(posx, posy, lenx, leny))

    #Method to set palceholder text
    def setPlaceHolderText(self, text):
        self.textbox.setPlaceholderText(text)