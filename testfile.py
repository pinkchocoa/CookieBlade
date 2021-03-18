import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUIWidgets import *
from window import window
from youtube import *

class UI():

    def __init__(self):
        self.win = newWindow("Cookie Crawler", window.wWidth, window.wHeight)
        self.ui = window()
        self.ui.setupUi(self.win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainM.window)


    def show(self):
        self.win.show()

app = startApp()
win = UI()
win.show()
sys.exit(app.QApp.exec_())