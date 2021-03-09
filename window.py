from windowGen import *
from cookieBlade import startCrawl

def testChangeWindow():
    w.hide()
    y.show()

wWidth = 1080
wHeight = 720

bWidth = 150
bHeight = 80

tWidth = 591
tHeight = 31

lWidth = 61
lHeight = 31

xSpace = 100
ySpace = 100



def mainMenu():
    nLabel = 1
    nText = 2
    nPush = 1
    textboxX = 120
    textboxY = 150
    buttonX = 370
    buttonY = 250

    w = windowGen("Cookie Crawler", wWidth, wHeight, nLabel, nText, nPush)
    w.setWindowIcon("CookieIcon.png")
    w.setLabel(wWidth/2, wHeight/2, 331, 81, "","GUIMainLogo.PNG")
    w.setLabel(textboxX-xSpace, textboxY+ySpace, lWidth, lHeight,"Enter URL:")
    w.setTextbox(textboxX, textboxY, tWidth, tHeight,"Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>")
    w.setTextbox(textboxX, textboxY+ySpace, tWidth, tHeight,"Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>")
    w.setPush(buttonX, buttonY, bWidth, bHeight, startCrawl,"Crawl Link!")
    w.setPush(buttonX+xSpace, buttonY, bWidth, bHeight, testChangeWindow,"Change Window")
    return w

def snsMenu():
    
    def crawlClicked():
        pass

    def backClicked():
        pass

    App = StartApp()
    testUserwindow = windowGen("User Crawler", width, wHeight, 3, 2, 2)
    testUserwindow.setLabel(0, 50, 800, 81, "Leave fields empty for random crawl", "Ariel", 20)
    testUserwindow.setTextbox(120, 160, 591, 31, "Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>")
    testUserwindow.setTextbox(120, 200, 591, 31, "Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>")
    testUserwindow.setPush(275, 250, 95, 41, crawlClicked, "Crawl!")
    testUserwindow.setPush(450, 250, 81, 41, backClicked, "Back")
    testUserwindow.showWindow()
    sys.exit(App.QApp.exec_())