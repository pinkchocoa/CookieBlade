## @file window.py
#
# @brief this file generates the widgets for the windows
#
# @author JiaJun(40%)
# @author Jodie(59%)
# @author JunHao(1%)
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
# - general (local)
#   - access to delete_file_contents
#   - access to file_to_set
# - webbrower standard library
#   - access to webbrowser
# - youtubeGraph (local)
#   - to generate reveneue graph for youtube data
# - LinkValidation (local)
#   - used to validate url links
# - geopy.geocoders
#   - access to Nominatim to translate between lat and longititude of location

# Imports
from GUIWidgets import *
from windowGen import windowGen
from twitter import Twitter, TUser, TTweet
from database import database
import twitterGraph
import twitterDB
from general import file_to_set, delete_file_contents
import webbrowser
import youtubeGraph
from LinkValidation import LinkValidation
from geopy.geocoders import Nominatim
#pip install geopandas
#pip install geopy

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
        self.ytlink = self.ytTextBox.getText()
        self.tlink = self.tTextBox.getText()

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
        userSnsM = self.setupSnsMenu()
        
        self.stackedWidget.addWidget(userSnsM.window.page)
        self.stackedWidget.setCurrentWidget(userSnsM.window)
    
    def topicToSns(self):
        """! switches the widgets from user topic menu to topic display menu
        """
        self.topicInput = self.topicTextBox.getText()
        self.locationInput = self.countryTextBox.getText()
        if (self.topicInput == ""):
            messageBox("Alert", "Please enter a topic.")
            return
        
        if (self.locationInput == ""):
            self.worldWide = True
            self.lat = 1.3521
            self.lng=103.8198
            self.locationInput = "World Wide"
        else:
            geolocator = Nominatim(user_agent="cookieBlade")
            data = geolocator.geocode(self.locationInput)
            self.worldWide = False
            self.lat = data.raw.get("lat")
            self.lng = data.raw.get("lon")
            text = str(self.lat) + ", " + str(self.lng)
            self.locationInput = geolocator.reverse(text, language='en')
            self.locationInput = str(self.locationInput)
            self.locationInput = self.locationInput.split(',')[-1]
            self.locationInput = self.locationInput[1:]
        
        self.prev = "topic"
        topicSnsM = self.setupTopicSnsMenu()
        self.stackedWidget.addWidget(topicSnsM.window.page)
        self.stackedWidget.setCurrentWidget(topicSnsM.window)
        
    def snsBack(self):
        """! switches the widgets from sns menu to widgets from either user or topic menu
        """
        delete_file_contents(RESULT_FILE)
        if self.prev == "user":
            self.stackedWidget.setCurrentWidget(self.userM.window)
        if self.prev == "topic":
            self.stackedWidget.setCurrentWidget(self.topicM.window)

    def setupUi(self, window):
        """! create base window and call menu functions to create window widgets
        @param window on which the widgets will be displayed
        """
        window.setWindowIcon("Assets/CookieIcon.png")
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
        """! crawl user's tweets
        @return favList, rtList, dateList
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
        #print(tweets)
        for idx, x in enumerate(tweets):
            tid = x[0]
            date = x[1]
            fav = x[2]
            rt = x[3]
            if len(dateList) > 7:
                #print(idx, " tweets crawled for 7 days of data")
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
        window.setBarChart([rtList,favList], dateList, 410, self.__wHeight - 650, 600, 200, "User's Fav and RT Count")
    
    def setYoutubeGraphs(self, window):
        """! create line chart with data crawled from youtube
        @param window on which the line chart will be displayed
        """
        posX = 450
        posY = 15
        widthX = 600
        heightY = 370
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        #uncomment
        #youtubeGraph.setRevenueData(self.ytlink) #this crawl youtube to get revenue and save to db.
        #revenueData = youtubeGraph.getRevenueData(self.ytlink) #this return revenue data from db
        #revenueData.pop(0) #remove the date string in the list.
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

    def crawlTwitterTopic(self, getLoc):
        """! crawl twitter tweets on topic
        @return tweets crawled
        """
        t = Twitter()
        tweets = t.searchKeyword(self.topicInput, "recent", 5, getLoc, self.lat, self.lng)
        return tweets

    def crawlTwitterTrending(self, worldWide, lat, lng):
        """! crawl twitter trending topics
        @return trending topics 
        """
        t = Twitter()
        return t.trendingTopics(worldWide, lat, lng)

    def setTwitterTopic(self, window):
        """! display tweets 
        @param widget on which the tweets will be displayed on
        """
        getLoc = not self.worldWide
        #uncomment this line to actually crawl
        #tweets = self.crawlTwitterTopic(getLoc)
        tweets = [['mindofhalo', '@calamityfairy what seriously no joke i do that w marcy a lot even though he doesn’t notice it at all', 1373505096923848704, []], ['Chikin10DZ', 'If you make clocks, you must have a lot of time on your hands.', 1373505096819040261, []], ['PChaldea', '&gt;&gt;one of the members tell you to head to the bar area and you find Marco sitting on a stool drinking some alcohol from a shot glass. You go closer and after slamming his drink down, Marco turns to face you with a bright smile. "Ah! So you must be the new person! What makes you&gt;&gt;', 1373505096785534976, []], ['porsha_whitmore', '@Retrievals1 Support: 👏👏...you deserve a little boobie for that babe....🥰🥰💕💕  ', 1373505096651317249, []], ['bird_dapper', '@AVI_Parrot a complete nobody like me made it on?', 1373505096307326976, []]]
        index = 22
        for idx, x in enumerate(tweets):
            user = x[0]
            text = x[1]
            link = "www.twitter.com/status/" + str(x[2])
            user = user + " " + link
            window.labelList[window.totalNLabel-index+(idx*2)].label.setText(user)
            window.labelList[window.totalNLabel-index+(idx*2)+1].label.setText(text)

    def setTwitterTrending(self, window, worldWide = True, lat=1.3521, lng=103.8198):
        """! create pie chart with topics crawled from twitter
        @param window on which the pie chart will be displayed
        """
        #uncomment this line to actually crawl
        #data = self.crawlTwitterTrending(worldWide, lat, lng)
        data = {'#JusticeTheAlbum': 90358, '#FalconAndWinterSoldier': 73400, 'Lana': 278975, '#一番プレイ時間長かったゲーム': 16288, 'Justin Bieber': 192695, '#HayırlıCumalar': 21367}
        y = self.__wHeight - 600
        window.setPieChart(data, "Current trending topics", 50, y)

    def setupMainMenu(self):
        """! create widgets for the main menu page
        """
        #Start of mainMenu
        self.mainM = windowGen()
        self.mainM.setLabel(self.__logoX, self.__logoY, self.__logoWidth, self.__logoHeight,"", "Assets/mainLogo.png","","","",True)
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
        self.userM.setLabel(self.__logoX, self.__logoY-79, self.__logoWidth, self.__logoHeight, "", "Assets/mainLogo.png", "","","",True)
        #ytlabel
        self.userM.setLabel(self.__labelX-22, self.__labelY, self.__labelWidth, self.__labelHeight, "YouTube Link:")
        #tLabel
        self.userM.setLabel(self.__labelX-6, self.__labelY+50, self.__labelWidth, self.__labelHeight, "Twitter Link:")
        #userNoteLabel
        self.userM.setLabel(self.__labelX+85, self.__labelY+80, self.__labelWidth+200, self.__labelHeight, "Leave fields empty for a random generation.")
        #userCrawlPush
        self.userM.setPush(self.pushX-125, self.__pushY-29, self.__pushWidth, self.__pushHeight, self.userToSns, "Crawl!")
        #userBackPush
        self.userM.setPush(self.__wWidth-self.__pushWidth-50, self.__wHeight-150, self.__pushWidth, self.__pushHeight, self.userToMain, "Back")
        #ytTextbox
        self.ytTextBox = self.userM.setTextbox(self.__textX, self.__textY, self.__textWidth*2, self.__textHeight, "Enter Youtube channel URL:")
        #tTextBox
        self.tTextBox = self.userM.setTextbox(self.__textX, self.__textY+50, self.__textWidth*2, self.__textHeight,"Enter Twitter User URL:")

    def setupTopicMenu(self):
        """! create widgets for the topic menu page
        """
        #Start of topicMenu
        self.topicM = windowGen()
        #topicLogo
        self.topicM.setLabel(self.__logoX, self.__logoY-79, self.__logoWidth, self.__logoHeight, "", "Assets/mainLogo.png", "", "", "", True)
        #topicCrawlPush
        self.topicM.setPush(self.pushX, self.__pushY-29, self.__pushWidth, self.__pushHeight, self.topicToSns, "Crawl!")
        #topicbackpush
        self.topicM.setPush(self.__wWidth-self.__pushWidth-50, self.__wHeight-150, self.__pushWidth, self.__pushHeight, self.topicToMain, "Back")
        #topiclabel
        self.topicM.setLabel(self.__labelX+238, self.__labelY, self.__labelWidth, self.__labelHeight, "Topic:")
        #countrylaebl
        self.topicM.setLabel(self.__labelX+218, self.__labelY+50, self.__labelWidth, self.__labelHeight, "Country:")
        #topicnotelabel
        self.topicM.setLabel(self.__labelX+285, self.__labelY+80, self.__labelWidth+200, self.__labelHeight, "Leave fields empty for a random generation.", "", "", "", "", True)
        #topictextbox
        self.topicTextBox = self.topicM.setTextbox(self.__textX+200, self.__textY, self.__textWidth, self.__textHeight, "Enter Topic:")
        #countrytextbox
        self.countryTextBox = self.topicM.setTextbox(self.__textX+200, self.__textY+50, self.__textWidth, self.__textHeight, "Enter Country:")
        
    def setupSnsMenu(self):
        """! create widgets for the sns menu page
        """
        #Start of snsMenu
        snsM = windowGen()
        
        #graphics
        snsM.setLabel(15, 100, 355, 150, "", "Assets/ysmallbox.png", "", "", "", True)
        snsM.setLabel(15, 245, 355, 150, "", "Assets/tsmallbox.png", "", "", "", True)
        snsM.setLabel(10, 10, 355, 75, "", "Assets/mainLogo.png", "", "", "", True)
        snsM.setLabel(20, 410, 865, 635, "", "Assets/piechart.png", "", "", "", True)
        snsM.setLabel(375,390, 689, 240, "", "Assets/rtfav.png", "", "", "", True)
        snsM.setLabel(425,0, 656, 400, "", "Assets/ytrev.png", "", "", "", True)

        self.setTwitterGraphs(snsM) 
        self.setTwitterTrending(snsM) 
        self.setYoutubeGraphs(snsM)
        
        #ytlogo
        snsM.setLabel(self.__logoX-310, self.__logoY-112, self.__logoWidth-270, self.__logoHeight+10, "", "Assets/YouTubeLogo.png", "", "", "", True)
        #tLogo
        snsM.setLabel(self.__logoX-303, self.__logoY+30, self.__logoWidth-300, self.__logoHeight+10, "", "Assets/TwitterLogo.png", "", "", "", True)
        
        labelW = 300
        diff = 25
        y = self.__labelY-143
        #Youtube
        #uncomment
        #youtubeGraph.setYoutubeChannelStats(self.ytlink)
        #youtubeStats = youtubeGraph.getYoutubeChannelStats(self.ytlink)
        youtubeStats = ['YT API Limit Error', 'YT API Limit Error', 'YT API Limit Error', 'YT API Limit Error']
        #subcountlabel
        text = "Sub count: " + str(youtubeStats[2])
        snsM.setLabel(self.__labelX+112, y, labelW, self.__labelHeight, text)
        #viewcountlabel
        y+=diff
        text = "View count: " + str(youtubeStats[3])
        snsM.setLabel(self.__labelX+112, y, labelW, self.__labelHeight, text)
        #videocountlabel
        y+=diff
        text = "Video count: " + str(youtubeStats[1])
        snsM.setLabel(self.__labelX+112, y, labelW, self.__labelHeight, text)
        #ytCreatedLabel
        y+=diff
        text = "Created At: " + str(youtubeStats[0])
        snsM.setLabel(self.__labelX+112, y, labelW, self.__labelHeight, text)

        if "twitter" in self.tlink:
            tUser = TUser.byURL(self.tlink)
        else:
            tUser = TUser.byID(self.tlink)

        #twitter
        
        #followerCountLabel
        #uncomment
        y = self.__labelY+2
        text = "Follower Count: " + "1232123"#+ str(tUser.followCount())
        snsM.setLabel(self.__labelX+112, y, labelW, self.__labelHeight, text)
        #tweetsLikedLabel
        y+=diff
        text = "Total favourited tweets: " + "1232123"#+ str(tUser.favTweetCount())
        snsM.setLabel(self.__labelX+112, y, labelW, self.__labelHeight, text)
        #totalTweetsLabel
        y+=diff
        text = "Total tweets: " + "1232123"#+ str(tUser.tweetCount())
        snsM.setLabel(self.__labelX+112, y, labelW, self.__labelHeight, text)
        #tCreatedLabel
        y+=diff
        text = "Created at: " + "1232123"#+ str(tUser.userCreatedAt())
        snsM.setLabel(self.__labelX+112, y, labelW, self.__labelHeight, text)
        

        #make sure that these labels are the last to be generated
        #these are to generate labels for the double click functionality for piechart usage
        x = 50
        y = self.__wHeight - 400
        textWidth = 500
        textHeight = 90
        snsM.setLabel(x+325, y, textWidth, self.__labelHeight, "Double click for on the piechart for recent tweets!")
        for i in range(3):
            y+=30
            snsM.setLabel(x+325, y, textWidth, 20, "")
            y+=25
            snsM.setLabel(x+325, y, textWidth, textHeight, "").setAlignmentTop()
            y+=textHeight-30

        y = self.__wHeight - 200
        snsM.setLabel(x+60, y-60, textWidth, self.__labelHeight, "Current twitter trending topics")
        x+=10
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
        
        #snsBackPush
        snsM.setPush(self.__wWidth-self.__pushWidth-50, self.__wHeight-150, self.__pushWidth, self.__pushHeight, self.snsBack, "Back")
        
        return snsM

    def setupTopicSnsMenu(self):
        """! create widgets for the topic sns menu page
        """
        snsM = windowGen()

        snsM.setLabel(10, 10, 355, 75, "", "Assets/mainLogo.png", "", "", "", True)
        snsM.setLabel(20, 410, 865, 635, "", "Assets/piechart.png", "", "", "", True)
        snsM.setLabel(400, 0, 670, 640, "", "Assets/topictweets.png", "", "", "", True)
        snsM.setLabel(50, 100, 300, 300, "", "Assets/globe.png", "", "", "", True)

        #make sure that these labels are the last to be generated
        #these are to generate labels for the double click functionality for chart usage
        #recent tweets display
        x = 450
        y = 30
        textWidth = 500
        textHeight = 80
        text = "Recent tweets based on '" + self.topicInput + "' at " + self.locationInput
        snsM.setLabel(x, y, textWidth, self.__labelHeight, text)
        
        for i in range(5):
            y+=30
            snsM.setLabel(x, y, textWidth, 20, "1")
            y+=25
            snsM.setLabel(x, y, textWidth, textHeight, "2").setAlignmentTop()
            y+=textHeight-30
            
        #piechart trend display
        x = 50
        y = self.__wHeight - 400
        textWidth = 500
        textHeight = 80
        snsM.setLabel(x+325, y, textWidth, self.__labelHeight, "Double click for on the piechart for recent tweets!")
        for i in range(3):
            y+=30
            snsM.setLabel(x+325, y, textWidth, 20, "")
            y+=25
            snsM.setLabel(x+325, y, textWidth, textHeight, "").setAlignmentTop()
            y+=textHeight-30

        y = self.__wHeight - 200
        text = "Current " + self.locationInput + " twitter trending topics"
        snsM.setLabel(x+30, y-60, textWidth, self.__labelHeight, text)
        x+=10
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

        self.setTwitterTopic(snsM)
        self.setTwitterTrending(snsM, self.worldWide, self.lat, self.lng) 
        #snsBackPush
        snsM.setPush(self.__wWidth-self.__pushWidth-50, self.__wHeight-150, self.__pushWidth, self.__pushHeight, self.snsBack, "Back")
        return snsM

    def goToUrl0(self):
        """! opens the web browser for the first link
        """
        results = list(file_to_set('result.txt'))
        if results and results[0]:
            webbrowser.open_new(results[0])
        else:
            messageBox("Alert", "Please generate links by double clicking on the pie chart first.")
        
    def goToUrl1(self):
        """! opens the web browser for the second link
        """
        results = list(file_to_set('result.txt'))
        if results and results[1]:
            webbrowser.open_new(results[1])
        else:
            messageBox("Alert", "Please generate links by double clicking on the pie chart first.")
        
    def goToUrl2(self):
        """! opens the web browser for the third link
        """
        results = list(file_to_set('result.txt'))
        if results and results[2]:
            webbrowser.open_new(results[2])
        else:
            messageBox("Alert", "Please generate links by double clicking on the pie chart first.")