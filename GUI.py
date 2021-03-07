from GUIWidgets import *

def searchClicked():
    YTURL = URLBox.textbox.text()
    TURL = TURLBox.textbox.text()
    if (YTURL == "" or TURL == ""):
        print("Error!")
    else:
        print(YTURL,TURL)

App = StartApp()
MainWindow = NewWindow("Cookie Crawler", 800, 600)
MainWindow.setWindowIcon("CookieIcon.png")
WindowLogo = NewLabel(MainWindow.QWin, 230, 70, 331, 81)
WindowLogo.setText("")
WindowLogo.setImage("GUIMainLogo.PNG")
URLLabel = NewLabel(MainWindow.QWin,60, 160, 61, 31)
URLLabel.setText("Enter URL:")
UIDLabel = NewLabel(MainWindow.QWin,260, 200, 61, 31)
UIDLabel.setText("Enter UID:")
URLBox = NewTextBox(MainWindow.QWin, 120, 160, 591, 31)
URLBox.setText("Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>")
TURLBox = NewTextBox(MainWindow.QWin, 120, 200, 591, 31)
TURLBox.setText("Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>")
SearchPushButton = NewPushButton(MainWindow.QWin, 370, 250, 81, 41, searchClicked)
SearchPushButton.setText("Crawl Link!")
MainWindow.QWin.show()
sys.exit(App.QApp.exec_())


