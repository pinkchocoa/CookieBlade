import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUIWidgets import *
from windowGen import windowGen

class window(object):

    wWidth = 1080
    wHeight = 720
    ytlink = ""
    tlink = ""

    def mainToUser(self):
        self.stackedWidget.setCurrentWidget(self.userM.window)
    
    def userToMain(self):
        self.stackedWidget.setCurrentWidget(self.mainM.window)
    
    def mainToTopic(self):
        self.stackedWidget.setCurrentWidget(self.topicM.window)
    
    def topicToMain(self):
        self.stackedWidget.setCurrentWidget(self.mainM.window)
    
    def userToSns(self):
        self.prev = "user"
        self.stackedWidget.setCurrentWidget(self.snsM.window)

        self.ytlink = self.userM.textList[0]
        self.tlink = self.userM.textList[1]

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
        self.stackedWidget.setCurrentWidget(self.snsM.window)
        
        
    def snsBack(self):
        if self.prev == "user":
            self.stackedWidget.setCurrentWidget(self.userM.window)
        if self.prev == "topic":
            self.stackedWidget.setCurrentWidget(self.topicM.window)

    def setupUi(self, window):
        window.setWindowIcon("CookieIcon.png")
        self.centralwidget = QtWidgets.QWidget(window.QWin)
        self.stackedWidget = newStackWidget(self.centralwidget, 0,0, 1080, 720)

        self.setupMainMenu()
        self.setupTopicMenu()
        self.setupUserMenu()
        self.setupsnsMenu()

        self.addToStack()

        window.QWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window.QWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        window.QWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window.QWin)
        window.QWin.setStatusBar(self.statusbar)

        self.retranslateUi(window.QWin)
        QtCore.QMetaObject.connectSlotsByName(window.QWin)


    def addToStack(self):
        self.stackedWidget.addWidget(self.mainM.window.page)
        self.stackedWidget.addWidget(self.userM.window.page)
        self.stackedWidget.addWidget(self.topicM.window.page)
        self.stackedWidget.addWidget(self.snsM.window.page)


    def setupMainMenu(self):
        #Start of mainMenu
        self.mainM = windowGen()
        self.mainM.setLabel(340, 157, 400, 90,"","GUIMainLogo.PNG","","","",True)
        #user push button
        self.mainM.setPush(340, 357, 150, 80, self.mainToUser,"User")
        #topic push button
        self.mainM.setPush(590, 357, 150, 80, self.topicToSns, "Topic")
        

    def setupUserMenu(self):
        #Start of userMenu
        self.userM = windowGen()
        #userLogo
        self.userM.setLabel(340, 78, 400, 90, "", "GUIMainLogo.PNG", "","","",True)
        #ytTextbox
        self.userM.setTextbox(140, 178, 800, 40, "Enter Youtube channel URL:")
        #tTextBox
        self.userM.setTextbox(140, 228, 800, 40, "Enter Twitter User URL:")
        #ytlabel
        self.userM.setLabel(65, 178, 75, 40, "Enter yt Link")
        #tLabel
        self.userM.setLabel(70, 228, 75, 40, "Enter twitter link")
        #userNoteLabel
        self.userM.setLabel(125, 253, 350, 40, "Leave fields empty for a random generation.")
        #userCrawlPush
        self.userM.setPush(215, 328, 150, 80, self.userToSns, "Crawl!")
        #userBackPush
        self.userM.setPush(715, 328, 150, 80, self.userToMain, "Back")
        

    def setupTopicMenu(self):
        #Start of topicMenu
        self.topicM = windowGen()
        #topicLogo
        self.topicM.setLabel(340, 78, 400, 90, "", "GUIMainLogo.PNG", "", "", "", True)
        #topicCrawlPush
        self.topicM.setPush(340, 328, 150, 80, self.topicToSns, "Crawl!")
        #topicbackpush
        self.topicM.setPush(590, 328, 150, 80, self.topicToMain, "Back")
        #topictextbox
        self.topicM.setTextbox(340, 178, 400, 40, "Enter Topic:")
        #countrytextbox
        self.topicM.setTextbox(340, 228, 400, 40, "Enter Country:")
        #topiclabel
        self.topicM.setLabel(270, 178, 75, 40, "Topic:")
        #countrylaebl
        self.topicM.setLabel(270, 228, 75, 40, "country" )
        #topicnotelabel
        self.topicM.setLabel(325, 253, 350, 40, "Leave fields empty for random crawl.", "", "", "", "", True)
        

    def setupsnsMenu(self):
        #Start of snsMenu
        self.snsM = windowGen()
        #ytlogo
        self.snsM.setLabel(20, 20, 130, 100, "", "YouTubeLogo.png", "", "", "", True)
        #tLogo
        self.snsM.setLabel(20, 140, 130, 100, "", "TwitterLogo.png", "", "", "", True)
        #subcountlabel
        self.snsM.setLabel(132, 10, 150, 40, "Sub count:")
        #viewcountlabel
        self.snsM.setLabel(158, 35, 150, 40, "View count:")
        #videocountlabel
        self.snsM.setLabel(160, 60, 150, 40, "Video count:")
        #ytCreatedLabel
        self.snsM.setLabel(152, 130, 150, 40, "Created At:")

        #twitter
        #followerCountLabel
        self.snsM.setLabel(152, 130, 150, 40, "Follower Count:")
        #tweetsLikedLabel
        self.snsM.setLabel(165, 155, 150, 40, "Liked tweets:")
        #totalTweetsLabel
        self.snsM.setLabel(145, 180, 150, 40, "Total tweets:")
        #tCreatedLabel
        self.snsM.setLabel(137, 205, 150, 40, "Created at:")
        #seperateLineLabel
        self.snsM.setLabel(-20, 210, 1100, 40, "", "", "Arial", 20)
        #snsBackPush
        self.snsM.setPush(920, 580, 150, 80, self.snsBack, "Back")


    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Cookie Crawler"))



# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
