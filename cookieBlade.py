# import sys
from GUIWidgets import * #contain class from GUI.py and GUIwidgets.py.
from twitter import * #contain class: Twitter(), Tuser(), TTweet() #twitter crawler.
from youtube import * #contain class: youtubeVid() #youtube crawler. #issue with youtube crawler class.
from database import * #contain class: database(), mkFolder(), UrlExtraction() #database and link validation.
from LinkValidation import LinkValidation #this contain UrlExtraction as well().
from UrlExtraction import UrlExtraction
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox #red underline can be ignored. for now..

#persistant data
ytURL = "" #https://www.youtube.com/channel/UCmGSJVG3mCRXVOP4yZrU1Dw #Johnny Harris
twURL = "" #https://twitter.com/johnnywharris #Johnny harris
ytUser = ""
twUser = ""

#Link Validation and input correctness checks before crawling
def startCrawl():

    global ytURL, twURL, twUser
    ytURL = ytBox.textbox.text()
    twURL = twBox.textbox.text()
    UID = UrlExtraction()
    twUser = UID.getUniqueID(twURL)
 
    linkCheck()
    twCrawl()


#Check Link and Entry Fields
def linkCheck():
    global twURL,ytURL

    #Check if Box is empthy
    if (ytURL == "" or twURL == ""):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Error!")
        msgBox.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Error! Missing URLs!")
        msgBox.exec_()
    elif("twitter" in ytURL):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Error!")
        msgBox.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Error! Twitter URL in wrong box.")
        msgBox.exec_()
    elif("youtube" in twURL):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Error!")
        msgBox.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Error! Youtube URL in wrong box.")
        msgBox.exec_()
    #check if URL is valid
    else:
        ytCheck = LinkValidation()
        twCheck = LinkValidation()
        ytStatus = ytCheck.UrlValidation(ytURL)
        twStatus = twCheck.UrlValidation(twURL)

        if (ytStatus == False):
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error!")
            msgBox.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Invalid Youtube URL")
            msgBox.exec_()
        elif(twStatus == False):
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error!")
            msgBox.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Invalid Twitter URL")
            msgBox.exec_()
        else:
            return True

#start twitter crawling
#crawl and save to database
def twCrawl():
    
    global twURL,twUser

    data = [] #max 10 items.
    #Pad data list with None
    for i in range(10):
        data.append(None)

    #begin crawling and adding to list
    twitterCrawl = TUser(twUser)
    temp = twitterCrawl.followCount()
    data[0] = str(temp)
    temp = twitterCrawl.tweetCount()
    data[1] = str(temp)

    #store to database
    store = database()
    store.insertTableDB(twURL,data)

 
#start youtube crawling
#crawl and save to database
def ytCrawl():
    pass

#show results
def resultWindow():
    pass





















#mainStart
App = StartApp()
mainWindow = NewWindow("Cookie Crawler", 800, 600)
mainWindow.setWindowIcon("CookieIcon.png")
windowLogo = NewLabel(mainWindow.QWin, 230, 70, 331, 81)
windowLogo.setText("")
windowLogo.setImage("GUIMainLogo.PNG")

#set Label
urlLabel = NewLabel(mainWindow.QWin,60, 160, 61, 31)
urlLabel.setText("Enter URL:")

#set youtube box
ytBox = NewTextBox(mainWindow.QWin, 120, 160, 591, 31)
ytBox.setText("Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>")

#set twitter box
twBox = NewTextBox(mainWindow.QWin, 120, 200, 591, 31)
twBox.setText("Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>")

#set Crawl Button
searchPushButton = NewPushButton(mainWindow.QWin, 370, 250, 81, 41, startCrawl)
searchPushButton.setText("Crawl Link!")

mainWindow.QWin.show()
sys.exit(App.QApp.exec_())