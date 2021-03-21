## @file main.py
#
# @brief this file generates the window and calls the window class in window.py
#
# @author JiaJun
#
# @section libraries_main Libraries/Modules
# - sys standard library (https://docs.python.org/3/library/sys.html)
#   - access to sys.argv and sys.exit functions
# - PyQt5.QtWidgets external library
#   - access to PyQt5 UI Widgets
# - GUIWidgets (local)
#   - access to classes from GUIWidgets.py
# - window (local)
#   - access to the window class
# - youtube (local)
#   - access to the youtube crawler
# - general (local)
#   - access to delete_file_contents
# - os external library
#   - access to environ

# Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUIWidgets import *
from window import window
from youtube import *
from general import delete_file_contents
from os import environ

def suppress_qt_warnings():
    """! this method is used to supressed 
    """
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

RESULT_FILE = 'result.txt'

## Documentation for a UI Class
# Defines the UI object which will create a window and call the window class to load UI
class UI():
    """! UI class
    Defines the UI object which will create a window and call the window class to load UI
    """
    __wWidth = 1080
    __wHeight = 1080

    def __init__(self):
        """! UI class initializer
        Creates a new empty window and setup the UI
        """
        self.win = newWindow("CookieBlade", self.__wWidth, self.__wHeight)
        self.win.setStyleSheet("Assets/blank.png")
        self.ui = window()
        self.ui.setupUi(self.win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainM.window)


    def show(self):
        """! set window to visible
        """
        self.win.show()

#start of main
suppress_qt_warnings()
delete_file_contents(RESULT_FILE)
app = startApp()
win = UI()
win.show()
sys.exit(app.QApp.exec_())
delete_file_contents(RESULT_FILE)
#end of main