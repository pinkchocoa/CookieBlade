#NOT IN USE#
from windowGen import *

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

App = StartApp()
userWindow = windowGen("Crawled Data", wWidth, wHeight)
userWindow.setWindowIcon("CookieIcon.png")
userWindow.setLabel(logoX, logoY, logoWidth, logoHeight, "","YouTubeLogo.PNG")
userWindow.setLabel(logoX, logoY+120, logoWidth, logoHeight, "","TwitterLogo.PNG")
userWindow.setLabel(labelX-12, labelY-10, labelWidth, labelHeight, "Sub Count: " + str(subCount), "", "Ariel", fontSize)
userWindow.setLabel(labelX+8, labelY+15, labelWidth, labelHeight, "Total View Count: " + str(viewCount), "", "Ariel", fontSize)
userWindow.setLabel(labelX+10, labelY+40, labelWidth, labelHeight, "Total Video Count: " + str(videoCount), "", "Ariel", fontSize)
userWindow.setLabel(labelX+19, labelY+65, labelWidth, labelHeight, "Created At: " + str(ytCreateDate), "", "Ariel", fontSize)
userWindow.setLabel(labelX, labelY+110, labelWidth, labelHeight, "Follower Count: " + str(followerCount), "", "Ariel", fontSize)
userWindow.setLabel(labelX+10, labelY+135, labelWidth, labelHeight, "Total Tweets Liked: " + str(tweetsLiked), "", "Ariel", fontSize)
userWindow.setLabel(labelX-5, labelY+160, labelWidth, labelHeight, "Total Tweets: " + str(totalTweets), "", "Ariel", fontSize)
userWindow.setLabel(labelX+18, labelY+185, labelWidth, labelHeight, "Created At: " + str(tCreatDate), "", "Ariel", fontSize)
userWindow.setLabel(0, labelY+200, labelWidth+1005, labelHeight, "____________________________________________________________________________", "", "Ariel", 2*fontSize)
userWindow.setPush(buttonX, buttonY, buttonWidth, buttonHeight, backClicked, "Back", "Ariel", fontSize)
userWindow.show()
sys.exit(App.QApp.exec_())