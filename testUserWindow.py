from windowGen import *

def userClicked():
    pass

def topicClicked():
    pass

App = StartApp()
testUserwindow = windowGen("User Crawler", 800, 600, 3, 2, 2)
testUserwindow.setLabel(0, 50, 800, 81, "Leave fields empty for random crawl", "Ariel", 20)
testUserwindow.setTextbox(120, 160, 591, 31, "Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>")
testUserwindow.setTextbox(120, 200, 591, 31, "Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>")
testUserwindow.setPush(275, 250, 95, 41, userClicked, "User")
testUserwindow.setPush(450, 250, 81, 41, topicClicked, "Topic")
testUserwindow.showWindow()
sys.exit(App.QApp.exec_())