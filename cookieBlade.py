# import sys
from GUIWidgets import * #contain class from GUI.py and GUIwidgets.py.
from twitter import Twitter, TUser, TTweet #contain class: Twitter(), Tuser(), TTweet() #twitter crawler.
from youtube import * #contain class: youtubeVid() #youtube crawler. #issue with youtube crawler class.
from database import database #contain class: database()
from LinkValidation import LinkValidation #contain class: LinkValidation
from UrlExtraction import UrlExtraction
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox #red underline can be ignored. for now..

#persistant data
youtubeURL = "" #https://www.youtube.com/channel/UCmGSJVG3mCRXVOP4yZrU1Dw #Johnny Harris
twitterURL = "" #https://twitter.com/johnnywharris #Johnny harris
youtubeUsername = ""
twitterUsername = ""
status = False

#Link Validation and input correctness checks before crawling
def startCrawl():

    global youtubeURL, twitterURL, youtubeUsername, twitterUsername,status
    youtubeURL = "https://www.youtube.com/channel/UCmGSJVG3mCRXVOP4yZrU1Dw" #ytBox.textbox.text()
    twitterURL = "https://twitter.com/johnnywharris" #twBox.textbox.text()
    userID = UrlExtraction()
    twitterUsername = userID.getUniqueID(twitterURL)
 
    if linkCheck() == True:
        #twitterCrawl()
        resultWindow()
        status = True #Set after complition of crawl.
        if status == True:
            mainWindow.QWin.close() #auto close window if crawl is done

#User input exception handling
def linkCheck():
    global twitterURL,youtubeURL

    #Check if Box is empthy
    if (youtubeURL == "" or twitterURL == ""): #check if text box is empty
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Error!")
        msgBox.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Error! Missing URLs!")
        msgBox.exec_()
    elif("twitter" in youtubeURL): #check if twitter link is placed in youtube box.
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Error!")
        msgBox.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Error! Twitter URL in wrong box.")
        msgBox.exec_()
    elif("youtube" in twitterURL): #check if youtube link is placed in twitter box.
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Error!")
        msgBox.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Error! Youtube URL in wrong box.")
        msgBox.exec_()
    #check if URL is valid
    else:
        youtubeCheck = LinkValidation()
        twitterCheck = LinkValidation()
        youtubeStatus = youtubeCheck.UrlValidation(youtubeURL)
        twitterStatus = twitterCheck.UrlValidation(twitterURL)

        if (youtubeStatus == False):
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error!")
            msgBox.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Invalid Youtube URL")
            msgBox.exec_()
        elif(twitterStatus == False):
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
def twitterCrawl():
    
    global twitterURL,twitterUsername

    crawledData = [] #max 10 items.
    #Pad data list with None
    for i in range(10):
        crawledData.append(None)

    #begin crawling and adding to list
    twitterCrawl = TUser(twitterUsername)
    temp = twitterCrawl.followCount()
    crawledData[0] = str(temp)
    temp = twitterCrawl.tweetCount()
    crawledData[1] = str(temp)

    #store to database
    store = database()
    store.insertTableDB(twitterURL,crawledData)

#start youtube crawling
#crawl and save to database
def youtubeCrawl():
    global youtubeURL,youtubeUsername
    pass

#show results
def resultWindow():
    global twitterURL,youtubeURL
    retrive = database()
    twitterData = retrive.getTableDB(twitterURL)
    print(twitterData)

#main
App = StartApp() #init
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

sys.exit(App.QApp.exec_()) #System X