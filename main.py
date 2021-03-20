## @file testfile.py
#
# @brief this file generates the window and calls the window class in window.py
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

# Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUIWidgets import *
from window import window
from youtube import *
from general import delete_file_contents

RESULT_FILE = 'result.txt'

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
        self.win = newWindow("Cookie Crawler", self.__wWidth, self.__wHeight)
        self.ui = window()
        self.ui.setupUi(self.win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainM.window)


    def show(self):
        """! set window to visible
        """
        self.win.show()

delete_file_contents(RESULT_FILE)
app = startApp()
win = UI()
win.show()
sys.exit(app.QApp.exec_())
delete_file_contents(RESULT_FILE)