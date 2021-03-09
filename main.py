from twitter import Twitter, TUser, TTweet #contain class: Twitter(), Tuser(), TTweet() #twitter crawler.
from youtube import * #contain class: youtubeVid() #youtube crawler. #issue with youtube crawler class.
from database import database #contain class: database()
from LinkValidation import LinkValidation #contain class: LinkValidation
from UrlExtraction import UrlExtraction
from windowGen import windowGen
from GUIWidgets import StartApp #contain class from GUI.py and GUIwidgets.py.
from GUIWidgets import messageBox
from cookieBlade import *
import sys
#need to clean the imports up later btw


def createMainWindow():
    wWidth = 800
    wHeight = 600
    nLabel = 1
    nText = 2
    nPush = 1
    w = windowGen("Cookie Crawler", wWidth, wHeight, nLabel, nText, nPush)
    w.setWindowIcon("CookieIcon.png")
    w.setLabel(230, 70, 331, 81, "","GUIMainLogo.PNG")
    w.setLabel(60, 160, 61, 31,"Enter URL:")
    w.setTextbox(120, 160, 591, 31,"Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>")
    w.setTextbox(120, 200, 591, 31,"Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>")
    w.setPush(370, 250, 81, 41, startCrawl,"Crawl Link!")
    w.setPush(490, 250, 81, 41, testChangeWindow,"Change Window")
    w.show()
    return w

def secondWindow():
    wWidth = 800
    wHeight = 600
    nLabel = 1
    nText = 2
    nPush = 1
    y = windowGen("aaaaaaaaaaaa", wWidth, wHeight, nLabel, nText, nPush)
    y.setWindowIcon("CookieIcon.png")
    y.setLabel(230, 70, 331, 81, "","GUIMainLogo.PNG")
    y.setLabel(60, 160, 61, 31,"AaAAAA")
    return y

def testChangeWindow():
    w.hide()
    y.show()



App = StartApp() #init
w= createMainWindow()
y= secondWindow()
sys.exit(App.QApp.exec_()) #System X