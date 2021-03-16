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
    day = [0,1,2,3,4,5,6,7,8,9,10]
    views = [0,30,32,34,32,33,31,29,32,35,45]
    w = windowGen("Cookie Crawler", wWidth, wHeight)
    w.setLineGraph(0, 0, 800, 600, 
    day, views, "b", "o",
    "w",
    "View Count Graph", "r", "30pt",
    "left", "Views", "red", "20pt",
    "bottom", "Day", "red", "20pt",
    "left", views)
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
    y = windowGen("aaaaaaaaaaaa", wWidth, wHeight)
    y.setWindowIcon("CookieIcon.png")
    y.setLabel(230, 70, 331, 81, "","GUIMainLogo.PNG")
    y.setLabel(60, 160, 61, 31,"AaAAAA")
    y.setPush(490, 250, 81, 41, testChangeWindow,"Change Window")
    
    #t = Twitter()
    #data = t.trendingTopics()
    #data = {'WIN5': 18956, 'ギベオン': 19344, '#14MartTıpBayramı': 21399, '#SoloistROSÉonINKIGAYO': 157042, 'taeyong': 201317, 'ホワイトデー': 583881}
    # #data = {"a":20,"b":25,"c":20, "d":25}
    #y.setPieChart(data, "tesT", 300,300)
    

    a = ["a",1,42,13,64]
    b = ["b",12,2,33,14]
    c = ["c",15,23,31,14]
    d = ["d",11,12,32,42]
    e = ["e",19,24,35,42]
    dataList = [a,b,c,d]
    category = ["jan", "feb", "mar", "apr"]
    y.setBarChart(dataList, category, "barChartTEst")
    return y


def testChangeWindow():
    if w.isVisible():
        w.hide()
        y.show()
    else:
        y.hide()
        w.show()


def testUser():
    #tUser = TUser("LilyPichu")
    tUser = TUser.byURL("https://twitter.com/LilyPichu")
    print(tUser.tweetCount())
    print(tUser.followCount())
    tweets = tUser.userTweets()
    for x in tweets:
        tTweet = TTweet(x)
        break
    print(tTweet.tweetID)
    print(tTweet.getDate())

#testUser()



App = StartApp() #init
w = createMainWindow()
y = secondWindow()
w.show()
sys.exit(App.QApp.exec_()) #System X

