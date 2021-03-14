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

buttonXSpace = 300
buttonYSpace = 100

textXSpace = 0
textYSpace = 45

labelXSpace = 70
labelYSpace = 50



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

    nLabel = 3
    nText = 2
    nPush = 2
    buttonX = 275
    buttonY = 250
    buttonX = 310
    buttonY = 250
    textBoxX = 150
    textBoxY = 160
    textBoxWidth = 800
    textBoxHeight = 40
    labelX = 70
    labelY = 160
    fontSize = 10

    App = StartApp()
    testUserwindow = windowGen("User Crawler", wWidth, wHeight, nLabel, nText, nPush)
    testUserwindow.setLabel(labelX+50, labelY-110, 800, 81, "Leave fields empty for random crawl", "", "Ariel", 2*fontSize)
    testUserwindow.setTextbox(textBoxX, textBoxY, textBoxWidth, textBoxHeight, "Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>", "Ariel", 10)
    testUserwindow.setTextbox(textBoxX, textBoxY + textYSpace, textBoxWidth, textBoxHeight, "Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>", "Ariel", 10)
    testUserwindow.setPush(buttonX, buttonY, 150, 80, crawlClicked, "Crawl!", "Ariel", fontSize)
    testUserwindow.setPush(buttonX + buttonXSpace, buttonY, 150, 80, backClicked, "Back", "Ariel", fontSize)
    testUserwindow.setLabel(labelX, labelY, 75, 31, "Enter link:", "", "Ariel", 10)
    testUserwindow.setLabel(labelX, labelY + labelYSpace, 75, 31, "Enter link:", "", "Ariel", fontSize)
    testUserwindow.show()
    sys.exit(App.QApp.exec_())