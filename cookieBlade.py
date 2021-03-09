# import sys
from twitter import Twitter, TUser, TTweet #contain class: Twitter(), Tuser(), TTweet() #twitter crawler.
from youtube import * #contain class: youtubeVid() #youtube crawler. #issue with youtube crawler class.
from database import database #contain class: database()
from LinkValidation import LinkValidation #contain class: LinkValidation
from UrlExtraction import UrlExtraction
from windowGen import windowGen
from GUIWidgets import StartApp #contain class from GUI.py and GUIwidgets.py.
from GUIWidgets import messageBox
import sys

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
        messageBox("Error!", "Error! Missing URLs!", "CookieIcon.png")
    elif("twitter" in youtubeURL): #check if twitter link is placed in youtube box.
        messageBox("Error!", "Error! Twitter URL in wrong box.", "CookieIcon.png")
    elif("youtube" in twitterURL): #check if youtube link is placed in twitter box.
        messageBox("Error!", "Error! Youtube URL in wrong box.", "CookieIcon.png")
    #check if URL is valid
    else:
        youtubeCheck = LinkValidation()
        twitterCheck = LinkValidation()
        youtubeStatus = youtubeCheck.UrlValidation(youtubeURL)
        twitterStatus = twitterCheck.UrlValidation(twitterURL)

        if (youtubeStatus == False):
            messageBox("Error!", "Invalid Youtube URL", "CookieIcon.png")
        elif(twitterStatus == False):
            messageBox("Error!", "Invalid Twitter URL", "CookieIcon.png")
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

