from windowGen import *
wWidth = 1080
wHeight = 720



def snsMenu():
    
    def crawlClicked():
        pass

    def backClicked():
        pass

    App = StartApp()
    testUserwindow = windowGen("User Crawler", width, wHeight, 3, 2, 2)
    testUserwindow.setLabel(0, 50, 800, 81, "Leave fields empty for random crawl", "Ariel", 20)
    testUserwindow.setTextbox(120, 160, 591, 31, "Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>")
    testUserwindow.setTextbox(120, 200, 591, 31, "Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>")
    testUserwindow.setPush(275, 250, 95, 41, crawlClicked, "Crawl!")
    testUserwindow.setPush(450, 250, 81, 41, backClicked, "Back")
    testUserwindow.showWindow()
    sys.exit(App.QApp.exec_())