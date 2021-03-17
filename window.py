import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUIWidgets import *
from windowGen import windowGen
import twitterGraph

class window(object):

    wWidth = 1080
    wHeight = 720
    numberOfTweets = 10

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

        self.ytlink = self.ytTextBox.returnText()
        self.tlink = self.tTextBox.returnText()

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
        
        test = self.setupsnsMenu()
        
        self.stackedWidget.addWidget(test.window.page)
        self.stackedWidget.setCurrentWidget(test.window)
            
    def topicToSns(self):
        self.prev = "topic"
        self.stackedWidget.setCurrentWidget(self.topicM.window)
        
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
        #can't set up sns menu here as the graphs needs to be added in before
        #self.setupsnsMenu()

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
        
    def setTwitterGraphs(self, window):
        a = ["a",1,42,13,64]
        b = ["b",12,2,33,14]
        c = ["c",15,23,31,14]
        d = ["d",11,12,32,42]
        e = ["e",19,24,35,42]
        data = [a,b,c,d]
        cat = ["jan", "feb", "mar", "apr"]

        #data,cat = twitterGraph.twitterGraph(self.numberOfTweets, self.tlink)
        print(data)
        print(cat)
        window.setBarChart(data, cat, 100, 100, 500, "User's Fav and RT Count")
    
    def setYoutubeGraphs(self, window):
        #t = Twitter()
        #data = t.trendingTopics()
        data = {'WIN5': 18956, 'ギベオン': 19344, '#14MartTıpBayramı': 21399, '#SoloistROSÉonINKIGAYO': 157042, 'taeyong': 201317, 'ホワイトデー': 583881}
        print(data)
        window.setPieChart(data, "tesT", 500, 30)



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

        self.ytTextBox = newTextBox(self.userM.window.page, 140, 178, 800, 40)
        self.tTextBox = newTextBox(self.userM.window.page, 140, 228, 800, 40)

        #ytTextbox
        #self.userM.setTextbox(140, 178, 800, 40, "Enter Youtube channel URL:")

        #tTextBox
        #self.userM.setTextbox(140, 228, 800, 40, "Enter Twitter User URL:")


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
        snsM = windowGen()
        self.setYoutubeGraphs(snsM) 
        self.setTwitterGraphs(snsM) 
        #ytlogo
        snsM.setLabel(20, 20, 130, 100, "", "YouTubeLogo.png", "", "", "", True)
        #tLogo
        snsM.setLabel(20, 140, 130, 100, "", "TwitterLogo.png", "", "", "", True)
        #subcountlabel
        snsM.setLabel(132, 10, 150, 40, "Sub count:")
        #viewcountlabel
        snsM.setLabel(158, 35, 150, 40, "View count:")
        #videocountlabel
        snsM.setLabel(160, 60, 150, 40, "Video count:")
        #ytCreatedLabel
        snsM.setLabel(152, 130, 150, 40, "Created At:")

        #twitter
        #followerCountLabel
        snsM.setLabel(152, 130, 150, 40, "Follower Count:")
        #tweetsLikedLabel
        snsM.setLabel(165, 155, 150, 40, "Liked tweets:")
        #totalTweetsLabel
        snsM.setLabel(145, 180, 150, 40, "Total tweets:")
        #tCreatedLabel
        snsM.setLabel(137, 205, 150, 40, "Created at:")
        #seperateLineLabel
        snsM.setLabel(-20, 210, 1100, 40, "", "", "Arial", 20)
        #snsBackPush
        snsM.setPush(920, 580, 150, 80, self.snsBack, "Back")
        return snsM

        

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
