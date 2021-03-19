## @file window.py
#
# @brief this file generates the widgets for the windows
#
# @section libraries_main Libraries/Modules
# - GUIWidgets (local) 
#   - access to GUIWidget classes
# - windowGen (local)
#   - access to windowGen classes
# - twitter (local)
#   - access to twitter crawler class
# - database (local)
#   - access to database functions
# - twitterGraph
#   - access to twitterGraph function to retrieve data for twitter graph
# - twitterDB
#   - access to database access methods for twitter

# Imports
from GUIWidgets import *
from windowGen import windowGen
from twitter import Twitter, TUser, TTweet
from database import database
import twitterGraph
import twitterDB
import time

## Documentation for window Class
# The window class intialize the different menus and their corresponding widgets
# this allows us to initialize the UI by calling a single class

class window(object):
    """! window class
    Defines the window object which will create the menus and widgets
    """
    #Width and Height values for window and widgets
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

    #X & Y coordinates for widgets
    logoX = pushX = (wWidth- logoWidth)/2
    logoY = (wHeight - logoHeight)/4
    pushY = logoY+200
    textX = logoX - 200
    textY = labelY = logoY + 21
    labelX = textX - 85

    numberOfTweets = 10

    #Widget page navigation
    def mainToUser(self):
        """! switches the widgets from main menu to widgets from user menu
        """ 
        self.stackedWidget.setCurrentWidget(self.userM.window)
    
    def userToMain(self):
        """! switches the widgets from user menu to widgets from main menu
        """
        self.stackedWidget.setCurrentWidget(self.mainM.window)
    
    def mainToTopic(self):
        """! switches the widgets from main menu to widgets from topic menu
        """
        self.stackedWidget.setCurrentWidget(self.topicM.window)
    
    def topicToMain(self):
        """! switches the widgets from topic menu to widgets from main menu
        """
        self.stackedWidget.setCurrentWidget(self.mainM.window)

    def userToSns(self):
        """! switches the widgets from user menu to widgets from sns menu
        """
        self.prev = "user"
        #Retrieve user inputs from textbox
        self.ytlink = self.ytTextBox.returnText()
        self.tlink = self.tTextBox.returnText()

        #Begin Crawl logic.
        if (self.ytlink == ""): #assign random youtube link
            self.ytlink = "https://www.youtube.com/user/LilyPichu"
        if (self.tlink == ""): #assign random twitter link
            self.tlink = "https://www.twitter.com/lilypichu"
        
        test = self.setupSnsMenu()
        
        self.stackedWidget.addWidget(test.window.page)
        self.stackedWidget.setCurrentWidget(test.window)
        
    def snsBack(self):
        """! switches the widgets from sns menu to widgets from either user or topic menu
        """
        if self.prev == "user":
            self.stackedWidget.setCurrentWidget(self.userM.window)
        if self.prev == "topic":
            self.stackedWidget.setCurrentWidget(self.topicM.window)

    #UI setup
    def setupUi(self, window):
        """! create base window and call menu functions to create window widgets
        @param window on which the widgets will be displayed
        """
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

        QtCore.QMetaObject.connectSlotsByName(window.QWin)

    def addToStack(self):
        """! add widget pages into stack widget
        """
        self.stackedWidget.addWidget(self.mainM.window.page)
        self.stackedWidget.addWidget(self.userM.window.page)
        self.stackedWidget.addWidget(self.topicM.window.page)
        
    def setTwitterGraphs(self, window):
        """! create bar chart with data crawled from twitter
        @param widget on which the bar chart will be displayed on
        """
        favList = ["Fav Count"]
        rtList = ["RT Count"]
        dateList = []
        totalRTCount=0
        totalFavCount=0
        amount = 100
        totalDates = 7
        if "twitter" in self.tlink:
            tUser = TUser.byURL(self.tlink)
        else:
            tUser = TUser.byID(self.tlink)
        tweets = tUser.userTweets(amount)
        print(tweets)
        for idx, x in enumerate(tweets):
            tid = x[0]
            date = x[1]
            fav = x[2]
            rt = x[3]
            if len(dateList) >= 7:
                print(idx, " tweets crawled for 7 days of data")
                favList.append(totalFavCount)
                rtList.append(totalRTCount)
                break
            if date in dateList:
                totalFavCount+=fav
                totalRTCount+=rt
            elif not dateList:#first tweet
                dateList.append(date)
            elif dateList:
                favList.append(totalFavCount)
                rtList.append(totalRTCount)
                dateList.append(date) #append new date
                totalRTCount=totalFavCount=0 #reset count
        favList.append(totalFavCount)
        rtList.append(totalRTCount)
        print(favList)
        print(rtList)
        print(dateList)
        window.setBarChart([rtList,favList], dateList, 100, 100, 500, "User's Fav and RT Count")
    
    def setYoutubeGraphs(self, window):
        """! create bar chart with data crawled from youtube
        @param window on which the bar chart will be displayed
        """
        pass

    def setTwitterTopics(self, window):
        """! create pie chart with topics crawled from twitter
        @param window on which the pie chart will be displayed
        """
        t = Twitter()
        data = t.trendingTopics()
        window.setPieChart(data, "Current trending topics", 500, 30)

    def setupMainMenu(self):
        """! create widgets for the main menu page
        """
        #Start of mainMenu
        self.mainM = windowGen()
        self.mainM.setLabel(self.logoX, self.logoY, self.logoWidth, self.logoHeight,"", "GUIMainLogo.PNG","","","",True)
        #user push button
        self.mainM.setPush(self.pushX, self.pushY, self.pushWidth, self.pushHeight, self.mainToUser,"User")
        #topic push button
        self.mainM.setPush(self.pushX+250, self.pushY, self.pushWidth, self.pushHeight, self.mainToTopic, "Topic")
        
    def setupUserMenu(self):
        """! create widgets for the user menu page
        """
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
        self.userM.setLabel(self.labelX-22, self.labelY, self.labelWidth, self.labelHeight, "YouTube Link:")
        #tLabel
        self.userM.setLabel(self.labelX-6, self.labelY+50, self.labelWidth, self.labelHeight, "Twitter Link:")
        #userNoteLabel
        self.userM.setLabel(self.labelX+85, self.labelY+80, self.labelWidth+200, self.labelHeight, "Leave fields empty for a random generation.")
        #userCrawlPush
        self.userM.setPush(self.pushX-125, self.pushY-29, self.pushWidth, self.pushHeight, self.userToSns, "Crawl!")
        #userBackPush
        self.userM.setPush(self.pushX+375, self.pushY-29, self.pushWidth, self.pushHeight, self.userToMain, "Back")


    def setupTopicMenu(self):
        """! create widgets for the topic menu page
        """
        #Start of topicMenu
        self.topicM = windowGen()
        #topicLogo
        self.topicM.setLabel(self.logoX, self.logoY-79, self.logoWidth, self.logoHeight, "", "GUIMainLogo.PNG", "", "", "", True)
        #topicCrawlPush
        self.topicM.setPush(self.pushX, self.pushY-29, self.pushWidth, self.pushHeight, self.topicToMain, "Crawl!")
        #topicbackpush
        self.topicM.setPush(self.pushX+250, self.pushY-29, self.pushWidth, self.pushHeight, self.topicToMain, "Back")
        #topictextbox
        self.topicM.setTextbox(self.textX+200, self.textY, self.textWidth, self.textHeight, "Enter Topic:")
        #countrytextbox
        self.topicM.setTextbox(self.textX+200, self.textY+50, self.textWidth, self.textHeight, "Enter Country:")
        #topiclabel
        self.topicM.setLabel(self.labelX+238, self.labelY, self.labelWidth, self.labelHeight, "Topic:")
        #countrylaebl
        self.topicM.setLabel(self.labelX+218, self.labelY+50, self.labelWidth, self.labelHeight, "Country:")
        #topicnotelabel
        self.topicM.setLabel(self.labelX+285, self.labelY+80, self.labelWidth+200, self.labelHeight, "Leave fields empty for a random generation.", "", "", "", "", True)
        
    def setupSnsMenu(self):
        """! create widgets for the sns menu page
        """
        #Start of snsMenu
        snsM = windowGen()
        self.setYoutubeGraphs(snsM) 
        self.setTwitterGraphs(snsM) 
        self.setTwitterTopics(snsM) 

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

        

    # def retranslateUi(self, window):
    #     _translate = QtCore.QCoreApplication.translate
    #     window.setWindowTitle(_translate("window", "Cookie Crawler"))


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())