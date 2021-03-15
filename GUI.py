#NOT IN USE#
from GUIWidgets import *
#from newWindow import *
from UserWindow import *
from graphwindow import GraphWindow

RandomYTURL = "https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ"
RandomTURL = "https://twitter.com/ECOOPconf"

def userClicked():
    uiWindow.QWin.hide()
    userWindow.QWin.show()
    

def topicClicked():
    YTURL = RandomYTURL
    TURL = RandomTURL
    MainWindow.QWin.show()



App = StartApp()
uiWindow = NewWindow("Cookie Crawler", 800, 600)
uiWindow.setWindowIcon("CookieIcon.png")
WindowLogo = NewLabel(uiWindow.QWin, 230, 70, 331, 81)
WindowLogo.setText("")
WindowLogo.setImage("GUIMainLogo.PNG")
UserPushButton = NewPushButton(uiWindow.QWin, 275, 250, 95, 41, userClicked)
UserPushButton.setText("User")
TopicPushButton = NewPushButton(uiWindow.QWin, 450, 250, 81, 41, topicClicked)
TopicPushButton.setText("Topic")
uiWindow.QWin.show()
sys.exit(App.QApp.exec_())


