from GUIWidgets import *

class UI:

    wWidth = 1080
    wHeight = 720

    def __init__(self):
        self.window = NewWindow("Cookie Crawler", self.wWidth, self.wHeight)
        self.window.setWindowIcon("CookieIcon.png")
        self.userInterface = self.mainWindow(self.window.QWin)

    def mainWindow(self, window):
        wWidth = 1080
        wHeight = 720

        logoWidth = 400
        logoHeight = 90

        buttonXSpace = 250
        buttonYSpace = 200

        logoX = (wWidth - logoWidth) / 2
        logoY = (wHeight - logoHeight) / 4

        buttonWidth = 150
        buttonHeight = 80

        buttonX = logoX
        buttonY = logoY + buttonYSpace

        self.logo = NewLabel(window, logoX, logoY, logoWidth, logoHeight)
        self.logo.setImage("GUIMainLogo.PNG")
        self.userButton = NewPushButton(window, buttonX, buttonY, buttonWidth, buttonHeight, self.mainToUser)
        self.userButton.setText("User")
        self.topicButton = NewPushButton(window, buttonX + buttonXSpace, buttonY, buttonWidth, buttonHeight, self.mainToTopic)
        self.topicButton.setText("Topic")
    
    def mainToUser():
        pass
    
    def mainToTopic():
        pass

    def userMenu(self, window):
        wWidth = 1080
        wHeight = 720
        fontSize = 10

        logoWidth = 400
        logoHeight = 90
        logoX = (wWidth - logoWidth) / 2
        logoY = (wHeight - logoHeight) / 8

        textBoxWidth = 800
        textBoxHeight = 40
        textX = (wWidth - textBoxWidth)/2
        textY = logoY + 100

        labelWidth = 75
        labelHeight = 40
        labelX = textX - 70
        labelY = textY

        buttonWidth = 150
        buttonHeight = 80
        buttonX = textX + (buttonWidth/2)
        buttonY = textY + 150

        self.logo = NewLabel(window, logoX, logoY, logoWidth, logoHeight)
        self.logo.setImage("GUIMainLogo.PNG")
        self.ytText = NewTextBox(window, textX, textY, textBoxWidth, textBoxHeight)
        self.ytText.setPlaceholderText("Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>")
        self.ytText.setFont("Ariel", fontSize)
        self.userM.setTextbox(textX, textY, textBoxWidth, textBoxHeight, "Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>", "Ariel", fontSize)
        self.userM.setTextbox(textX, textY+50, textBoxWidth, textBoxHeight, "Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>", "Ariel", fontSize)
        self.userM.setLabel(labelX, labelY, labelWidth, labelHeight, "YouTube:", "", "Ariel", fontSize)
        self.userM.setLabel(labelX, labelY+50, labelWidth, labelHeight, "Twitter:", "", "Ariel", fontSize)
        self.userM.setPush(buttonX, buttonY, buttonWidth, buttonHeight, self.userCrawlClicked, "Crawl!", "Ariel", fontSize)
        self.userM.setPush(buttonX+500, buttonY, buttonWidth, buttonHeight, self.userBackClicked, "Back", "Ariel", fontSize)
        self.userM.setLabel(labelX+55, labelY+75, labelWidth+200, labelHeight, "Note: Leave fields empty for random crawl", "", "Ariel", fontSize)

app = StartApp()
UI = UI()
UI.window.QWin.show()
sys.exit(app.QApp.exec_())