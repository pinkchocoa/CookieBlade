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
import window as wind
#need to clean the imports up later btw


def createMainWindow():
    wWidth = 800
    wHeight = 600
    nLabel = 1
    nText = 2
    nPush = 1
    nGraph = 1
    day = [0,1,2,3,4,5,6,7,8,9,10]
    views = [0,30,32,34,32,33,31,29,32,35,45]
    w = windowGen("Cookie Crawler", wWidth, wHeight, nLabel, nText, nPush, nGraph)
    w.setWindowIcon("CookieIcon.png")
    w.setLabel(230, 70, 331, 81, "","GUIMainLogo.PNG")
    w.setLabel(60, 160, 61, 31,"Enter URL:")
    w.setTextbox(120, 160, 591, 31,"Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>")
    w.setTextbox(120, 200, 591, 31,"Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>")
    w.setPush(370, 250, 81, 41, startCrawl,"Crawl Link!")
    w.setPush(490, 250, 81, 41, testChangeWindow,"Change Window")
    w.setGraph(0, 0, 800, 600, 
    day, views, "b", "o",
    "w",
    "View Count Graph", "r", "30pt",
    "left", "Views", "red", "20pt",
    "bottom", "Day", "red", "20pt",
    "left", views)
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
w = createMainWindow()
w.show()
y= secondWindow()
sys.exit(App.QApp.exec_()) #System X