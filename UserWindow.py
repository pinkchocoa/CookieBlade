from windowGen import *

def crawlClicked():
    pass

def backClicked():
    pass

a = 200
xSpace = 300

App = StartApp()
testUserwindow = windowGen("User Crawler", 1080, 720, 3, 2, 2)
testUserwindow.setLabel(0, 50, 800, 81, "Leave fields empty for random crawl", "Ariel", 20)
testUserwindow.setTextbox(120, 160, 600, 30, "Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>")
testUserwindow.setTextbox(120, 200, 600, 30, "Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>")
testUserwindow.setPush(a, 250, 150, 80, crawlClicked, "Crawl!")
testUserwindow.setPush(a + xSpace, 250, 150, 80, backClicked, "Back")
testUserwindow.show()
sys.exit(App.QApp.exec_())