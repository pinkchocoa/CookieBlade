## @file GUIWidgets.py
#
# @brief this file contains GUI Widget Classes
#
# @section libraries_main Libraries/Modules
# - sys standard library (https://docs.python.org/3/library/sys.html)
#   - access to sys.argv and sys.exit functions
# - PyQt5 external library (pip install PyQt5)
#   - access to PyQt5 GUI functions
# - PyQt5.QtWidgets external library
#   - access to PyQt5 UI Widgets

#Imports
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

## Documentation for GUIWidgets.py
# Contains all UI Widget classes
# We can reuse classes to make different widgets for diffferent purpose

#Class to initialize a new instance of QApplication module which is required to run PyQt5
class StartApp:
    """! StartApp class
    Defines the QApplication object which allows the creation of all QtWidgets
    """
    def __init__(self):
        self.QApp = QApplication(sys.argv)

#Class to create a new Window
class NewWindow:
    """! NewWindow class
    Defines the window object used to display widgets
    """
    def __init__(self, name, lenX, lenY):
        """! NewWindow class initializer
        @param name used to name the window title
        @param lenX used to set the horizontal length of the window
        @param lenY used to set the veritical height of the window
        """
        #Initialize new instance of Window UI
        self.QWin = QMainWindow()
        #Set Window Title
        self.QWin.setWindowTitle(name)
        #Set Window Size
        self.QWin.resize(lenX,lenY)

    #Method to set Window icon image
    def setWindowIcon(self,image):
        """! setWindowIcon method used to set image as Window Icon
        @param image image name to be used as Window Icon
        """
        self.QWin.setWindowIcon(QtGui.QIcon(image))

#Class to create a new Label
class NewLabel:
    """! NewLabel class
    Defines the label object used to display text label to guide users
    """
    def __init__(self, window, posX, posY, lenX, lenY):
        """! NewLabel class initializer
        @param window used to determine which window for the widget to appear on
        @param posX used to set the X coordinate of where the label will appear
        @param posY used to set the Y coordinate of where the label will appear
        @param lenX used to set the horizontal length of the label
        @param lenY used to set the vertical height of the label
        """
        #Initialize new instance of Label UI
        self.label = QLabel(window)
        #Set Label x & y position and size
        self.label.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Set alignment of Label text to align center
        self.label.setAlignment(QtCore.Qt.AlignCenter)

    #Method to set Label Text
    def setText(self, text):
        """! setText method 
        @param text used to set the text to be displayed by the label
        """
        self.label.setText(text)
    
    #Method to display image in Label
    def setImage(self, image):
        """! setImage method
        @param image used to determine what image to be displayed in label
        """
        #Set display image in parameter in Label
        self.label.setPixmap(QtGui.QPixmap(image))
        #Enable image scaling to fit Label size
        self.label.setScaledContents(True)

#Class to create new TextBox
class NewTextBox:
    """! NewTextBox class
    Defines the textbox object used to retrieve user input
    """
    def __init__(self, window, posX, posY, lenX, lenY):
        """! NewTextBox class initializer
        @param window used to determine which window for the widget to appear on
        @param posX used to set the X coordinate of where the label will appear
        @param posY used to set the Y coordinate of where the label will appear
        @param lenX used to set the horizontal length of the label
        @param lenY used to set the vertical height of the label
        """
        #Initialize new instance of TextBox UI
        self.textbox = QLineEdit(window)
        #Set TextBox x & y position and size
        self.textbox.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))

    #Method to set palceholder text
    def setText(self, text):
        """! setText method
        @param text used to set the text to be displayed by the label
        """
        self.textbox.setPlaceholderText(text)

#Class to create new PushButton
class NewPushButton:
    """! NewPushButton class
    Defines the PushButton object to recieve button click input
    """
    def __init__(self, window, posX, posY, lenX, lenY, functionName):
        """! NewPushButton class initializer
        @param window used to determine which window for the widget to appear on
        @param posX used to set the X coordinate of where the label will appear
        @param posY used to set the Y coordinate of where the label will appear
        @param lenX used to set the horizontal length of the label
        @param lenY used to set the vertical height of the label
        @param functionname used to determine which function to call when button is clicked
        """
        #Initialize new instance of PushButton UI
        self.PushButton = QPushButton(window)
        #Set PushButton x & y position and size
        self.PushButton.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Calls function when PushButton is clicked
        self.PushButton.clicked.connect(functionName)

    #Set PushButton text
    def setText(self, text):
        """! setText method
        @param text used to set the text to be displayed by the label
        """
        self.PushButton.setText(text)

class messageBox:
    def __init__(self, winTitle="", text="", winIcon="" ,show=True,icon="Critical"):
        self.msgBox = QMessageBox()
        msgBox = self.msgBox
        if winTitle:
            msgBox.setWindowTitle(winTitle)
        if winIcon:
            msgBox.setWindowIcon(QtGui.QIcon(winIcon))
        if text:
            msgBox.setText(text)
        if icon is "Critical":
            msgBox.setIcon(QMessageBox.Critical)
        if show:
            self.show()

    def show(self):
        msgBox = self.msgBox
        msgBox.exec_()