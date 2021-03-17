import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUIWidgets import *
from window import window
from youtube import *
from twitterGraph import twitterGraph

class UI():

    wWidth = 1080
    wHeight = 720
    ytlink = ""
    tlink = ""

    def __init__(self):
        self.win = newWindow("Cookie Crawler", self.wWidth, self.wHeight)
        self.ui = window()
        self.ui.setupUi(self.win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainM.window)


    def show(self):
        self.win.show()

app = startApp()
win = UI()
win.show()
sys.exit(app.QApp.exec_())