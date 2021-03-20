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
# - webbrower standard library
#   - access to webbrowser

# Imports
from GUIWidgets import *
from windowGen import windowGen
from twitter import Twitter, TUser, TTweet
from database import database
import twitterGraph
import twitterDB
import time
from general import file_to_set, delete_file_contents
import webbrowser
import youtubeGraph
from LinkValidation import LinkValidation

RESULT_FILE = 'result.txt'

## Documentation for window Class
# The window class intialize the different menus and their corresponding widgets
# this allows us to initialize the UI by calling a single class

class window(object):
    """! window class
    Defines the window object which will create the menus and widgets
    """
    #Width and Height values for window and widgets
    __wWidth = 1080 
    __wHeight = 1080 
    __logoWidth = 400
    __logoHeight = 90
    __pushWidth = 150
    __pushHeight = 80
    __textWidth = 400
    __textHeight = 40
    __labelWidth = 150
    __labelHeight = 40

    #X & Y coordinates for widgets
    __logoX = pushX = (__wWidth- __logoWidth)/2
    __logoY = (__wHeight - __logoHeight)/4
    __pushY = __logoY+200
    __textX = __logoX - 200
    __textY = __labelY = __logoY + 21
    __labelX = __textX - 85

    __numberOfTweets = 10

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
        #Retrieve user inputs from textbox
        self.ytlink = self.ytTextBox.returnText()
        self.tlink = self.tTextBox.returnText()

        if (self.ytlink == ""): #assign random youtube link
            self.ytlink = "https://www.youtube.com/channel/UCvWU1K29wCZ8j1NsXsRrKnA"
        if (self.tlink == ""): #assign random twitter link
            self.tlink = "https://www.twitter.com/lilypichu"
        #check user input
        check = LinkValidation()
        if not check.UrlValidation(self.ytlink): #return True if valid else False.
            messageBox("Alert", "Please enter a valid youtube link or leave it empty.")
            return
        if not check.UrlValidation(self.tlink):
            messageBox("Alert", "Please enter a valid twitter link or leave it empty.")
            return

        self.prev = "user"

        #Begin Crawl logic.
        
 
        test = self.setupSnsMenu()
        
        self.stackedWidget.addWidget(test.window.page)
        self.stackedWidget.setCurrentWidget(test.window)
        
    def snsBack(self):
        """! switches the widgets from sns menu to widgets from either user or topic menu
        """
        delete_file_contents(RESULT_FILE)
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
        self.stackedWidget = newStackWidget(self.centralwidget, 0,0, self.__wWidth, self.__wHeight)

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
    

    def crawlTwitterGraph(self):
        #start_time = time.time()
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
            if len(dateList) > 7:
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
        favList.pop()
        rtList.pop()
        dateList.pop()
        #print("--- %s seconds ---" % (time.time() - start_time))
        return favList, rtList, dateList

    def setTwitterGraphs(self, window):
        """! create bar chart with data crawled from twitter
        @param widget on which the bar chart will be displayed on
        """
        #uncomment this line to actually crawl
        #favList, rtList, dateList = self.crawlTwitterGraph()
        
        favList = ['Fav Count', 29530, 19848, 113188, 68611, 38661, 76062, 73379]
        rtList = ['RT Count', 806, 291, 21911, 1394, 2644, 7678, 2969]
        dateList = ['2021-03-19', '2021-03-18', '2021-03-17', '2021-03-16', '2021-03-15', '2021-03-14', '2021-03-13']
        window.setBarChart([rtList,favList], dateList, 500, self.__wHeight - 600, 600, 200, "User's Fav and RT Count")
    
    def setYoutubeGraphs(self, window):
        """! create bar chart with data crawled from youtube
        @param window on which the bar chart will be displayed
        """
        posX = 500
        posY = 10
        widthX = 600
        heightY = 450
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        # youtubeGraph.setRevenueData(self.ytlink) #this crawl youtube to get revenue and save to db.
        # revenueData = youtubeGraph.getRevenueData(self.tlink) #this return revenue data from db
        # revenueData.pop(0) #remove the date string in the list.
        #print(revenueData)
        #Testing
        revenueData = [10,30,32,34,32,33,31,29,32,35,45,11]
        window.setLineGraph(posX, posY, widthX, heightY, 
            months, revenueData, "g", "o",
            "00000000",
            "Revenue Graph", "r", "8pt",
            "left", "$ Revenue $", "red", "8pt",
            "bottom", "Months", "red", "8pt",
            "left", revenueData)


    def crawlTwitterTopics(self):
        t = Twitter()
        return t.trendingTopics()

    def setTwitterTopics(self, window):
        """! create pie chart with topics crawled from twitter
        @param window on which the pie chart will be displayed
        """
        #uncomment this line to actually crawl
        #data = self.crawlTwitterTopics()
        data = {'#JusticeTheAlbum': 90358, '#FalconAndWinterSoldier': 73400, 'Lana': 278975, '#一番プレイ時間長かったゲーム': 16288, 'Justin Bieber': 192695, '#HayırlıCumalar': 21367}
        y = self.__wHeight - 500
        window.setPieChart(data, "Current trending topics", 50, y)

    def setupMainMenu(self):
        """! create widgets for the main menu page
        """
        #Start of mainMenu
        self.mainM = windowGen()
        self.mainM.setLabel(self.__logoX, self.__logoY, self.__logoWidth, self.__logoHeight,"", "GUIMainLogo.PNG","","","",True)
        #user push button
        self.mainM.setPush(self.pushX, self.__pushY, self.__pushWidth, self.__pushHeight, self.mainToUser,"User")
        #topic push button
        self.mainM.setPush(self.pushX+250, self.__pushY, self.__pushWidth, self.__pushHeight, self.mainToTopic, "Topic")
        
    def setupUserMenu(self):
        """! create widgets for the user menu page
        """
        #Start of userMenu
        self.userM = windowGen()
        #userLogo
        self.userM.setLabel(self.__logoX, self.__logoY-79, self.__logoWidth, self.__logoHeight, "", "GUIMainLogo.PNG", "","","",True)

        #ytTextbox
        self.ytTextBox = self.userM.setTextbox(self.__textX, self.__textY, self.__textWidth*2, self.__textHeight, "Enter Youtube channel URL:")
        #tTextBox
        self.tTextBox = self.userM.setTextbox(self.__textX, self.__textY+50, self.__textWidth*2, self.__textHeight,"Enter Twitter User URL:")

        #ytlabel
        self.userM.setLabel(self.__labelX-22, self.__labelY, self.__labelWidth, self.__labelHeight, "YouTube Link:")
        #tLabel
        self.userM.setLabel(self.__labelX-6, self.__labelY+50, self.__labelWidth, self.__labelHeight, "Twitter Link:")
        #userNoteLabel
        self.userM.setLabel(self.__labelX+85, self.__labelY+80, self.__labelWidth+200, self.__labelHeight, "Leave fields empty for a random generation.")
        #userCrawlPush
        self.userM.setPush(self.pushX-125, self.__pushY-29, self.__pushWidth, self.__pushHeight, self.userToSns, "Crawl!")
        #userBackPush
        self.userM.setPush(self.__wWidth-self.__pushWidth-10, self.__wHeight-100, self.__pushWidth, self.__pushHeight, self.userToMain, "Back")

    def setupTopicMenu(self):
        """! create widgets for the topic menu page
        """
        #Start of topicMenu
        self.topicM = windowGen()
        #topicLogo
        self.topicM.setLabel(self.__logoX, self.__logoY-79, self.__logoWidth, self.__logoHeight, "", "GUIMainLogo.PNG", "", "", "", True)
        #topicCrawlPush
        self.topicM.setPush(self.pushX, self.__pushY-29, self.__pushWidth, self.__pushHeight, self.topicToMain, "Crawl!")
        #topicbackpush
        self.topicM.setPush(self.__wWidth-self.__pushWidth-10, self.__wHeight-100, self.__pushWidth, self.__pushHeight, self.topicToMain, "Back")
        #topictextbox
        self.topicM.setTextbox(self.__textX+200, self.__textY, self.__textWidth, self.__textHeight, "Enter Topic:")
        #countrytextbox
        self.topicM.setTextbox(self.__textX+200, self.__textY+50, self.__textWidth, self.__textHeight, "Enter Country:")
        #topiclabel
        self.topicM.setLabel(self.__labelX+238, self.__labelY, self.__labelWidth, self.__labelHeight, "Topic:")
        #countrylaebl
        self.topicM.setLabel(self.__labelX+218, self.__labelY+50, self.__labelWidth, self.__labelHeight, "Country:")
        #topicnotelabel
        self.topicM.setLabel(self.__labelX+285, self.__labelY+80, self.__labelWidth+200, self.__labelHeight, "Leave fields empty for a random generation.", "", "", "", "", True)
        
    def setupSnsMenu(self):
        """! create widgets for the sns menu page
        """
        #Start of snsMenu
        snsM = windowGen()
        self.setTwitterGraphs(snsM) 
        self.setTwitterTopics(snsM) 
        self.setYoutubeGraphs(snsM)

        #ytlogo
        snsM.setLabel(self.__logoX-320, self.__logoY-137, self.__logoWidth-270, self.__logoHeight+10, "", "YouTubeLogo.png", "", "", "", True)
        #tLogo
        snsM.setLabel(self.__logoX-303, self.__logoY-17, self.__logoWidth-300, self.__logoHeight+10, "", "TwitterLogo.png", "", "", "", True)
        
        #Youtube
        youtubeGraph.setYoutubeChannelStats(self.ytlink)
        youtubeStats = youtubeGraph.getYoutubeChannelStats(self.ytlink)
        #subcountlabel
        text = "Sub count: " + str(youtubeStats[2])
        snsM.setLabel(self.__labelX+112, self.__labelY-168, self.__labelWidth, self.__labelHeight, text)
        #viewcountlabel
        text = "View count: " + str(youtubeStats[3])
        snsM.setLabel(self.__labelX+112, self.__labelY-143, self.__labelWidth, self.__labelHeight, text)
        #videocountlabel
        text = "Video count: " + str(youtubeStats[1])
        snsM.setLabel(self.__labelX+112, self.__labelY-118, self.__labelWidth, self.__labelHeight, text)
        #ytCreatedLabel
        text = "Created At: " + str(youtubeStats[0])
        snsM.setLabel(self.__labelX+112, self.__labelY-93, self.__labelWidth, self.__labelHeight, text)

        if "twitter" in self.tlink:
            tUser = TUser.byURL(self.tlink)
        else:
            tUser = TUser.byID(self.tlink)

        #twitter
        labelW = 300
        #followerCountLabel
        text = "Follower Count: " + str(tUser.followCount())
        snsM.setLabel(self.__labelX+112, self.__labelY-48, labelW, self.__labelHeight, text)
        #tweetsLikedLabel
        text = "Total favourited tweets: " + str(tUser.favTweetCount())
        snsM.setLabel(self.__labelX+112, self.__labelY-23, labelW, self.__labelHeight, text)
        #totalTweetsLabel
        text = "Total tweets: " + str(tUser.tweetCount())
        snsM.setLabel(self.__labelX+112, self.__labelY+2, labelW, self.__labelHeight, text)
        #tCreatedLabel
        text = "Created at: " + str(tUser.userCreatedAt())
        snsM.setLabel(self.__labelX+112, self.__labelY+27, labelW, self.__labelHeight, text)
        #seperateLineLabel
        #snsM.setLabel(-20, 210, 1100, 40, "", "", "Arial", 20)
        

        #make sure that these labels are the last to be generated
        #these are to generate labels for the double click functionality for piechart usage
        x = 50
        y = self.__wHeight - 400
        textWidth = 500
        textHeight = 90
        snsM.setLabel(x+400, y, textWidth, self.__labelHeight, "Double click for on the piechart for recent tweets!")
        for i in range(3):
            y+=30
            snsM.setLabel(x+400, y, textWidth, 20, "")
            y+=25
            snsM.setLabel(x+400, y, textWidth, textHeight, "").setAlignmentTop()
            y+=textHeight-30

        #snsBackPush
        snsM.setPush(self.__wWidth-self.__pushWidth-10, self.__wHeight-100, self.__pushWidth, self.__pushHeight, self.snsBack, "Back")

        y = self.__wHeight - 150
        snsM.setLabel(x+60, y-30, textWidth, self.__labelHeight, "Current twitter trending topics")
        snsM.setLabel(x, y, textWidth, self.__labelHeight, "Double click on the piechart for news article links")
        for i in range(3):
            y+=30
            text = "Article " + str(i+1)
            snsM.setLabel(x+self.__labelWidth-30, y, 1000, 25, "Double click on the piechart!")
            if i == 0:
                snsM.setPush(x, y, self.__labelWidth-40, 25, self.goToUrl0, text)
            elif i == 1:
                snsM.setPush(x, y, self.__labelWidth-40, 25, self.goToUrl1, text)
            elif i == 2:
                snsM.setPush(x, y, self.__labelWidth-40, 25, self.goToUrl2, text)
        
        
        
        return snsM

    def goToUrl0(self):
        results = list(file_to_set('result.txt'))
        if results and results[0]:
            webbrowser.open_new(results[0])
        else:
            messageBox("Alert", "Please generate links by double clicking on the pie chart first.")
        

    def goToUrl1(self):
        results = list(file_to_set('result.txt'))
        if results and results[1]:
            webbrowser.open_new(results[1])
        else:
            messageBox("Alert", "Please generate links by double clicking on the pie chart first.")
        

    def goToUrl2(self):
        results = list(file_to_set('result.txt'))
        if results and results[2]:
            webbrowser.open_new(results[2])
        else:
            messageBox("Alert", "Please generate links by double clicking on the pie chart first.")