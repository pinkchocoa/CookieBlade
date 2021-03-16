import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from testwindow import window

class UI():
    def __init__(self):
        self.win = QMainWindow()
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

app = QApplication(sys.argv)
win = UI()
win.show()
sys.exit(app.exec_())