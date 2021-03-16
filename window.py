from windowGen import *
from cookieBlade import startCrawl

class UI:
    
    def __init__(self):
        self.app = StartApp()
        self.userM = self.userMenu()
        self.userM.hide()
        self.topicM = self.topicMenu()
        self.topicM.hide()
        self.snsM = self.snsMenu()
        self.snsM.hide()
        self.mainM = self.mainMenu()
        self.mainM.show()
        sys.exit(self.app.QApp.exec_())

    def mainToUser(self):
        self.mainM.hide()
        self.userM.show()

    def mainToTopic(self):
        self.mainM.hide()
        self.topicM.show()

    def userCrawlClicked(self):
        self.userM.hide()
        self.prev = "user"
        self.snsM.show()

    def userBackClicked(self):
        self.userM.hide()
        self.mainM.show()

    def topicCrawlClicked(self):
        self.snsM = self.snsMenu()
        self.topicM.hide()
        self.prev = "topic"
        self.snsM.show()

    def topicBackClicked(self):
        self.topicM.hide()
        self.mainM.show()

    def snsBackClicked(self):
        if self.prev == "user":
            self.snsM.hide()
            self.userM.show()
        if self.prev == "topic":
            self.snsM.hide()
            self.topicM.show()

    def mainMenu(self):
        
        wWidth = 1080
        wHeight = 720
        fontSize = 10

        logoWidth = 400
        logoHeight = 90

        buttonXSpace = 250
        buttonYSpace = 200

        logoX = (wWidth - logoWidth) / 2
        logoY = (wHeight - logoHeight) / 4

        buttonWidth = 150
        buttonHeight = 80

        buttonX = logoX
        buttonY = logoY + buttonYSpace

        
        mainM = windowGen("Cookie Crawler", wWidth, wHeight)
        mainM.setWindowIcon("CookieIcon.png")
        mainM.setLabel(logoX, logoY, logoWidth, logoHeight, "","GUIMainLogo.PNG")
        mainM.setPush(buttonX, buttonY, buttonWidth, buttonHeight, self.mainToUser,"User", "Ariel", fontSize)
        mainM.setPush(buttonX + buttonXSpace, buttonY, buttonWidth, buttonHeight, self.mainToTopic,"Topic", "Ariel", fontSize)
        return mainM

    def userMenu(self):
        
        wWidth = 1080
        wHeight = 720
        fontSize = 10

        logoWidth = 400
        logoHeight = 90
        logoX = (wWidth - logoWidth) / 2
        logoY = (wHeight - logoHeight) / 8

        textBoxWidth = 800
        textBoxHeight = 40
        textX = (wWidth - textBoxWidth)/2
        textY = logoY + 100

        labelWidth = 75
        labelHeight = 40
        labelX = textX - 75
        labelY = textY

        buttonWidth = 150
        buttonHeight = 80
        buttonX = textX + (buttonWidth/2)
        buttonY = textY + 150

        userM = windowGen("User Crawler", wWidth, wHeight)
        userM.setLabel(logoX, logoY, logoWidth, logoHeight, "","GUIMainLogo.PNG")
        userM.setTextbox(textX, textY, textBoxWidth, textBoxHeight, "Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>", "Ariel", fontSize)
        userM.setTextbox(textX, textY+50, textBoxWidth, textBoxHeight, "Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>", "Ariel", fontSize)
        userM.setLabel(labelX, labelY, labelWidth, labelHeight, "YouTube:", "", "Ariel", fontSize)
        userM.setLabel(labelX, labelY+50, labelWidth, labelHeight, "Twitter:", "", "Ariel", fontSize)
        userM.setPush(buttonX, buttonY, buttonWidth, buttonHeight, self.userCrawlClicked, "Crawl!", "Ariel", fontSize)
        userM.setPush(buttonX+500, buttonY, buttonWidth, buttonHeight, self.userBackClicked, "Back", "Ariel", fontSize)
        userM.setLabel(labelX+55, labelY+75, labelWidth+275, labelHeight, "Note: Leave fields empty for random crawl", "", "Ariel", fontSize)
        userM.setWindowIcon("CookieIcon.png")
        return userM

    def topicMenu(self):

        wWidth = 1080
        wHeight = 720
        fontSize = 10

        logoWidth = 400
        logoHeight = 90
        logoX = (wWidth - logoWidth) / 2
        logoY = (wHeight - logoHeight) / 8

        textBoxWidth = 400
        textBoxHeight = 40
        textX = (wWidth - textBoxWidth)/2
        textY = logoY + 100

        labelWidth = 75
        labelHeight = 40
        labelX = textX - 70
        labelY = textY

        buttonWidth = 150
        buttonHeight = 80
        buttonX = textX
        buttonY = textY + 150

        topicM = windowGen("Topic Crawler", wWidth, wHeight)
        topicM.setLabel(logoX, logoY, logoWidth, logoHeight, "","GUIMainLogo.PNG")
        topicM.setTextbox(textX, textY, textBoxWidth, textBoxHeight, "Enter Topic: E.g., Java", "Ariel", fontSize)
        topicM.setTextbox(textX, textY+50, textBoxWidth, textBoxHeight, "Enter Country: E.g., Singapore", "Ariel", fontSize)
        topicM.setLabel(labelX, labelY, labelWidth, labelHeight, "Topic:", "", "Ariel", fontSize)
        topicM.setLabel(labelX, labelY+50, labelWidth, labelHeight, "Country:", "", "Ariel", fontSize)
        topicM.setPush(buttonX, buttonY, buttonWidth, buttonHeight, self.topicCrawlClicked, "Crawl!", "Ariel", fontSize)
        topicM.setPush(buttonX+250, buttonY, buttonWidth, buttonHeight, self.topicBackClicked, "Back", "Ariel", fontSize)
        topicM.setLabel(labelX+55, labelY+75, labelWidth+200, labelHeight, "Note: Leave fields empty for random crawl", "", "Ariel", fontSize)
        topicM.setWindowIcon("CookieIcon.png")
        return topicM

    def snsMenu(self):
        
        def backClicked():
            pass

        wWidth = 1080
        wHeight = 720
        fontSize = 10

        logoWidth = 120
        logoHeight = 100
        logoX = 50
        logoY = 20

        labelWidth = 150
        labelHeight = 40
        labelX = logoX+100
        labelY = logoY

        buttonWidth = 150
        buttonHeight = 80
        buttonX = 900
        buttonY = 600

        subCount = 1
        viewCount = 2
        videoCount = 3
        ytCreateDate = "01/01/2020"

        followerCount = 4
        tweetsLiked = 5
        totalTweets = 6
        tCreatDate = "02/02/2020"

        snsM = windowGen("Crawled Data", wWidth, wHeight)
        snsM.setWindowIcon("CookieIcon.png")
        snsM.setLabel(logoX, logoY, logoWidth, logoHeight, "","YouTubeLogo.PNG")
        snsM.setLabel(logoX, logoY+120, logoWidth, logoHeight, "","TwitterLogo.PNG")
        snsM.setLabel(labelX-12, labelY-10, labelWidth, labelHeight, "Sub Count: " + str(subCount), "", "Ariel", fontSize)
        snsM.setLabel(labelX+8, labelY+15, labelWidth, labelHeight, "Total View Count: " + str(viewCount), "", "Ariel", fontSize)
        snsM.setLabel(labelX+10, labelY+40, labelWidth, labelHeight, "Total Video Count: " + str(videoCount), "", "Ariel", fontSize)
        snsM.setLabel(labelX+19, labelY+65, labelWidth, labelHeight, "Created At: " + str(ytCreateDate), "", "Ariel", fontSize)
        snsM.setLabel(labelX, labelY+110, labelWidth, labelHeight, "Follower Count: " + str(followerCount), "", "Ariel", fontSize)
        snsM.setLabel(labelX+10, labelY+135, labelWidth, labelHeight, "Total Tweets Liked: " + str(tweetsLiked), "", "Ariel", fontSize)
        snsM.setLabel(labelX-5, labelY+160, labelWidth, labelHeight, "Total Tweets: " + str(totalTweets), "", "Ariel", fontSize)
        snsM.setLabel(labelX+18, labelY+185, labelWidth, labelHeight, "Created At: " + str(tCreatDate), "", "Ariel", fontSize)
        snsM.setLabel(0, labelY+200, labelWidth+1005, labelHeight, "____________________________________________________________________________", "", "Ariel", 2*fontSize)
        snsM.setPush(buttonX, buttonY, buttonWidth, buttonHeight, self.snsBackClicked, "Back", "Ariel", fontSize)
        return snsM
    