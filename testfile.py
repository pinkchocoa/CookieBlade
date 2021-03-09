from windowGen import *
import UserWindow

def userClicked():
    pass

def topicClicked():
    pass

App = StartApp()
testWindow = windowGen("Cookie Crawler", 800, 600, 1, 0, 2)
testWindow.setWindowIcon("CookieIcon.png")
testWindow.setLabel(230, 70, 331, 81, "", "GUIMainLogo.PNG")
testWindow.setPush(275, 250, 95, 41, userClicked, "User")
testWindow.setPush(450, 250, 81, 41, topicClicked, "Topic")
testWindow.showWindow()
sys.exit(App.QApp.exec_())