import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUIWidgets import *
from windowGen import windowGen
import twitterGraph
from twitter import Twitter
from database import database

class window(object):

    wWidth = 1080
    wHeight = 720
    logoWidth = 400
    logoHeight = 90
    pushWidth = 150
    pushHeight = 80
    textWidth = 400
    textHeight = 40
    labelWidth = 150
    labelHeight = 40
    logoX = pushX = (wWidth- logoWidth)/2
    logoY = (wHeight - logoHeight)/4
    pushY = logoY+200
    textX = logoX - 200
    textY = labelY = logoY + 21
    labelX = textX - 85
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
        
        test = self.setupSnsMenu()
        
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
        self.setupUserMenu()
        self.setupTopicMenu()
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
        # a = ["a",1,42,13,64]
        # b = ["b",12,2,33,14]
        # c = ["c",15,23,31,14]
        # d = ["d",11,12,32,42]
        # e = ["e",19,24,35,42]
        # data = [a,b,c,d]
        # cat = ["jan", "feb", "mar", "apr"]

        rtData,favData,dateData = twitterGraph.twitterGraph(self.numberOfTweets, self.tlink)
        print(rtData)
        print(favData)
        print(dateData)
        window.setBarChart([rtData,favData], dateData, 100, 100, 500, "User's Fav and RT Count")
    

    def setYoutubeGraphs(self, window):
        pass

    def setTwitterTopics(self, window):
        t = Twitter()
        data = t.trendingTopics()
        #data = {'WIN5': 18956, 'ギベオン': 19344, '#14MartTıpBayramı': 21399, '#SoloistROSÉonINKIGAYO': 157042, 'taeyong': 201317, 'ホワイトデー': 583881}
        print(data)
        window.setPieChart(data, "tesT", 700, 30)



    def setupMainMenu(self):

        #Start of mainMenu
        self.mainM = windowGen()
        self.mainM.setLabel(self.logoX, self.logoY, self.logoWidth, self.logoHeight,"", "GUIMainLogo.PNG","","","",True)
        #user push button
        self.mainM.setPush(self.pushX, self.pushY, self.pushWidth, self.pushHeight, self.mainToUser,"User")
        #topic push button
        self.mainM.setPush(self.pushX+250, self.pushY, self.pushWidth, self.pushHeight, self.mainToTopic, "Topic")
        
    def setupUserMenu(self):

        #Start of userMenu
        self.userM = windowGen()
        #userLogo
        self.userM.setLabel(self.logoX, self.logoY-79, self.logoWidth, self.logoHeight, "", "GUIMainLogo.PNG", "","","",True)

        self.ytTextBox = newTextBox(self.userM.window.page, self.textX, self.textY, self.textWidth*2, self.textHeight)
        self.tTextBox = newTextBox(self.userM.window.page, self.textX, self.textY+50, self.textWidth*2, self.textHeight)

        #ytTextbox
        #self.userM.setTextbox(140, 178, 800, 40, "Enter Youtube channel URL:")

        #tTextBox
        #self.userM.setTextbox(140, 228, 800, 40, "Enter Twitter User URL:")


        #ytlabel
        self.userM.setLabel(self.labelX, self.labelY, self.labelWidth, self.labelHeight, "YouTube Link:")
        #tLabel
        self.userM.setLabel(self.labelX+12, self.labelY+50, self.labelWidth, self.labelHeight, "Twitter Link:")
        #userNoteLabel
        self.userM.setLabel(self.labelX+85, self.labelY+80, self.labelWidth+100, self.labelHeight, "Leave fields empty for a random generation.")
        #userCrawlPush
        self.userM.setPush(self.pushX-125, self.pushY-29, self.pushWidth, self.pushHeight, self.userToSns, "Crawl!")
        #userBackPush
        self.userM.setPush(self.pushX+375, self.pushY-29, self.pushWidth, self.pushHeight, self.userToMain, "Back")


    def setupTopicMenu(self):

        #Start of topicMenu
        self.topicM = windowGen()
        #topicLogo
        self.topicM.setLabel(self.logoX, self.logoY-79, self.logoWidth, self.logoHeight, "", "GUIMainLogo.PNG", "", "", "", True)
        #topicCrawlPush
        self.topicM.setPush(self.pushX, self.pushY-29, self.pushWidth, self.pushHeight, self.topicToSns, "Crawl!")
        #topicbackpush
        self.topicM.setPush(self.pushX+250, self.pushY-29, self.pushWidth, self.pushHeight, self.topicToMain, "Back")
        #topictextbox
        self.topicM.setTextbox(self.textX+200, self.textY, self.textWidth, self.textHeight, "Enter Topic:")
        #countrytextbox
        self.topicM.setTextbox(self.textX+200, self.textY+50, self.textWidth, self.textHeight, "Enter Country:")
        #topiclabel
        self.topicM.setLabel(self.labelX+248, self.labelY, self.labelWidth, self.labelHeight, "Topic:")
        #countrylaebl
        self.topicM.setLabel(self.labelX+233, self.labelY+50, self.labelWidth, self.labelHeight, "Country:")
        #topicnotelabel
        self.topicM.setLabel(self.labelX+285, self.labelY+80, self.labelWidth+100, self.labelHeight, "Leave fields empty for a random generation.", "", "", "", "", True)
        
    def setupSnsMenu(self):

        #Start of snsMenu
        snsM = windowGen()
        self.setYoutubeGraphs(snsM) 
        self.setTwitterGraphs(snsM) 

        #ytlogo
        snsM.setLabel(self.logoX-320, self.logoY-137, self.logoWidth-270, self.logoHeight+10, "", "YouTubeLogo.png", "", "", "", True)
        #tLogo
        snsM.setLabel(self.logoX-320, self.logoY-17, self.logoWidth-270, self.logoHeight+10, "", "TwitterLogo.png", "", "", "", True)
        #subcountlabel
        snsM.setLabel(self.labelX+112, self.labelY-168, self.labelWidth, self.labelHeight, "Sub count:")
        #viewcountlabel
        snsM.setLabel(self.labelX+112, self.labelY-143, self.labelWidth, self.labelHeight, "View count:")
        #videocountlabel
        snsM.setLabel(self.labelX+112, self.labelY-118, self.labelWidth, self.labelHeight, "Video count:")
        #ytCreatedLabel
        snsM.setLabel(self.labelX+112, self.labelY-93, self.labelWidth, self.labelHeight, "Created At:")

        #twitter
        #followerCountLabel
        snsM.setLabel(self.labelX+112, self.labelY-48, self.labelWidth, self.labelHeight, "Follower Count:")
        #tweetsLikedLabel
        snsM.setLabel(self.labelX+112, self.labelY-23, self.labelWidth, self.labelHeight, "Liked tweets:")
        #totalTweetsLabel
        snsM.setLabel(self.labelX+112, self.labelY+2, self.labelWidth, self.labelHeight, "Total tweets:")
        #tCreatedLabel
        snsM.setLabel(self.labelX+112, self.labelY+27, self.labelWidth, self.labelHeight, "Created at:")
        #seperateLineLabel
        #snsM.setLabel(-20, 210, 1100, 40, "", "", "Arial", 20)
        #snsBackPush
        snsM.setPush(self.pushX+580, self.pushY+223, self.pushWidth, self.pushHeight, self.snsBack, "Back")
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
