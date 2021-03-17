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
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainM)
        self.ui.userPushButton.clicked.connect(self.mainToUser)
        self.ui.topicPushButton.clicked.connect(self.mainToTopic)
        self.ui.userCrawlPush.clicked.connect(self.userToSns)
        self.ui.userBackPush.clicked.connect(self.userToMain)
        self.ui.topicCrawlPush.clicked.connect(self.topicToSns)
        self.ui.topicBackPush.clicked.connect(self.topicToMain)
        self.ui.snsBackPush.clicked.connect(self.snsBack)

    def mainToUser(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.userM)
    
    def userToMain(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainM)
    
    def mainToTopic(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.topicM)
    
    def topicToMain(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainM)
    
    def userToSns(self):
        self.prev = "user"
        self.ui.stackedWidget.setCurrentWidget(self.ui.snsM)
        self.ytlink = self.ui.ytTextBox.text()
        self.tlink = self.ui.tTextBox.text()

        #Begin Crawl logic.
        if (self.ytlink and self.tlink == ""):
            #assign random link to twitter and youtube
            pass
        elif (self.ytlink == ""):
            #assign random link to youtube
            pass
        elif (self.tlink == ""):
            #assign random link to twitter
            pass
            
    def topicToSns(self):
        self.prev = "topic"
        self.ui.stackedWidget.setCurrentWidget(self.ui.snsM)
        
        
    def snsBack(self):
        if self.prev == "user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.userM)
        if self.prev == "topic":
            self.ui.stackedWidget.setCurrentWidget(self.ui.topicM)
        
        

    def show(self):
        self.win.show()

app = startApp()
win = UI()
win.show()
sys.exit(app.QApp.exec_())