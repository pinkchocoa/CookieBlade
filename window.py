from windowGen import *
from cookieBlade import startCrawl

class UI:
    
    def __init__(self):
        app = StartApp()
        mainM = self.mainMenu()
        mainM.show()
        sys.exit(app.QApp.exec_())

    def mainToUser(self):
        userM = self.userMenu()
        self.mainM.hide()
        userM.show()

    def mainToTopic(self):
        topicM = self.topicMenu()
        self.mainM.hide()
        topicM.show()

    def userCrawlClicked(self):
        snsM = self.snsMenu()
        self.userM.hide()
        self.prev = "user"
        snsM.show()

    def userBackClicked(self):
        self.userM.hide()
        self.mainM.show()

    def topicCrawlClicked(self):
        snsM = self.snsMenu()
        self.topicM.hide()
        self.prev = "topic"
        snsM.show()

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

        
        self.mainM = windowGen("Cookie Crawler", wWidth, wHeight)
        self.mainM.setWindowIcon("CookieIcon.png")
        self.mainM.setLabel(logoX, logoY, logoWidth, logoHeight, "","GUIMainLogo.PNG")
        self.mainM.setPush(buttonX, buttonY, buttonWidth, buttonHeight, self.mainToUser,"User")
        self.mainM.setPush(buttonX + buttonXSpace, buttonY, buttonWidth, buttonHeight, self.mainToTopic,"Topic")
        return self.mainM

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
        labelX = textX - 70
        labelY = textY

        buttonWidth = 150
        buttonHeight = 80
        buttonX = textX + (buttonWidth/2)
        buttonY = textY + 150

        self.userM = windowGen("User Crawler", wWidth, wHeight)
        self.userM.setWindowIcon("CookieIcon.png")
        self.userM.setLabel(logoX, logoY, logoWidth, logoHeight, "","GUIMainLogo.PNG")
        self.userM.setTextbox(textX, textY, textBoxWidth, textBoxHeight, "Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>", "Ariel", fontSize)
        self.userM.setTextbox(textX, textY+50, textBoxWidth, textBoxHeight, "Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>", "Ariel", fontSize)
        self.userM.setLabel(labelX, labelY, labelWidth, labelHeight, "YouTube:", "", "Ariel", fontSize)
        self.userM.setLabel(labelX, labelY+50, labelWidth, labelHeight, "Twitter:", "", "Ariel", fontSize)
        self.userM.setPush(buttonX, buttonY, buttonWidth, buttonHeight, self.userCrawlClicked, "Crawl!", "Ariel", fontSize)
        self.userM.setPush(buttonX+500, buttonY, buttonWidth, buttonHeight, self.userBackClicked, "Back", "Ariel", fontSize)
        self.userM.setLabel(labelX+55, labelY+75, labelWidth+200, labelHeight, "Note: Leave fields empty for random crawl", "", "Ariel", fontSize)
        return self.userM

    def topicMenu(self):

        def crawlClicked():
            pass

        def backClicked():
            pass

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

        self.topicM = windowGen("Topic Crawler", wWidth, wHeight)
        self.topicM.setWindowIcon("CookieIcon.png")
        self.topicM.setLabel(logoX, logoY, logoWidth, logoHeight, "","GUIMainLogo.PNG")
        self.topicM.setTextbox(textX, textY, textBoxWidth, textBoxHeight, "Enter Topic: E.g., Java", "Ariel", fontSize)
        self.topicM.setTextbox(textX, textY+50, textBoxWidth, textBoxHeight, "Enter Country: E.g., Singapore", "Ariel", fontSize)
        self.topicM.setLabel(labelX, labelY, labelWidth, labelHeight, "Topic:", "", "Ariel", fontSize)
        self.topicM.setLabel(labelX, labelY+50, labelWidth, labelHeight, "Country:", "", "Ariel", fontSize)
        self.topicM.setPush(buttonX, buttonY, buttonWidth, buttonHeight, self.topicCrawlClicked, "Crawl!", "Ariel", fontSize)
        self.topicM.setPush(buttonX+250, buttonY, buttonWidth, buttonHeight, self.topicBackClicked, "Back", "Ariel", fontSize)
        self.topicM.setLabel(labelX+55, labelY+75, labelWidth+200, labelHeight, "Note: Leave fields empty for random crawl", "", "Ariel", fontSize)
        return self.topicM

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

        self.snsM = windowGen("Crawled Data", wWidth, wHeight)
        self.snsM.setWindowIcon("CookieIcon.png")
        self.snsM.setLabel(logoX, logoY, logoWidth, logoHeight, "","YouTubeLogo.PNG")
        self.snsM.setLabel(logoX, logoY+120, logoWidth, logoHeight, "","TwitterLogo.PNG")
        self.snsM.setLabel(labelX-12, labelY-10, labelWidth, labelHeight, "Sub Count: " + str(subCount), "", "Ariel", fontSize)
        self.snsM.setLabel(labelX+8, labelY+15, labelWidth, labelHeight, "Total View Count: " + str(viewCount), "", "Ariel", fontSize)
        self.snsM.setLabel(labelX+10, labelY+40, labelWidth, labelHeight, "Total Video Count: " + str(videoCount), "", "Ariel", fontSize)
        self.snsM.setLabel(labelX+19, labelY+65, labelWidth, labelHeight, "Created At: " + str(ytCreateDate), "", "Ariel", fontSize)
        self.snsM.setLabel(labelX, labelY+110, labelWidth, labelHeight, "Follower Count: " + str(followerCount), "", "Ariel", fontSize)
        self.snsM.setLabel(labelX+10, labelY+135, labelWidth, labelHeight, "Total Tweets Liked: " + str(tweetsLiked), "", "Ariel", fontSize)
        self.snsM.setLabel(labelX-5, labelY+160, labelWidth, labelHeight, "Total Tweets: " + str(totalTweets), "", "Ariel", fontSize)
        self.snsM.setLabel(labelX+18, labelY+185, labelWidth, labelHeight, "Created At: " + str(tCreatDate), "", "Ariel", fontSize)
        self.snsM.setLabel(0, labelY+200, labelWidth+1005, labelHeight, "____________________________________________________________________________", "", "Ariel", 2*fontSize)
        self.snsM.setPush(buttonX, buttonY, buttonWidth, buttonHeight, self.snsBackClicked, "Back", "Ariel", fontSize)
        return self.snsM
    
    
