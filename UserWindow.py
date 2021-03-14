from windowGen import *

def crawlClicked():
    testUserwindow.setBrowser(1080, 720, "https://www.google.com/")


def backClicked():
    pass

def labelClicked(event):
    testUserwindow.setBrowser(1080, 720, "https://www.google.com/")

buttonX = 310
buttonY = 250

wWidth = 1080
wHeight = 720

bWidth = 150
bHeight = 80

tWidth = 591
tHeight = 31

lWidth = 61
lHeight = 31

buttonXSpace = 300
buttonYSpace = 100

textX = 150
textY = 160

labelX = 70
labelY = 160

textXSpace = 0
textYSpace = 45

labelXSpace = 70
labelYSpace = 50

App = StartApp()
testUserwindow = windowGen("User Crawler", 1080, 720, 4, 2, 2)
# piechart = newPieChart()
# piechart.addData("Python", 100)
# piechart.addData("C++", 100)
# piechart.addData("Dog", 100)
# piechart.setSeries(piechart.series)
# piechart.viewChart(testUserwindow.QWin)
testUserwindow.setLabel(labelX+50, 50, 800, 81, "Leave fields empty for random crawl", "", "Ariel", 20)
testUserwindow.setLabel(labelX+50, 450, 800, 81, "www.google.com", "", "Ariel", 20, labelClicked)
testUserwindow.setTextbox(textX, textY, 800, 40, "Enter Youtube Channel URL: E.g., <https://www.youtube.com/channel>", "Ariel", 10)
testUserwindow.setTextbox(textX, textY + textYSpace, 800, 40, "Enter Twitter User URL: E.g., <https://twitter.com/leehsienloong>", "Ariel", 10)
testUserwindow.setPush(buttonX, buttonY, 150, 80, crawlClicked, "Crawl!", "Ariel", 10)
testUserwindow.setPush(buttonX + buttonXSpace, buttonY, 150, 80, backClicked, "Back", "Ariel", 10)
testUserwindow.setLabel(labelX, labelY, 75, 31, "Enter link:", "", "Ariel", 10)
testUserwindow.setLabel(labelX, labelY + labelYSpace, 75, 31, "Enter link:", "", "Ariel", 10)
testUserwindow.show()
sys.exit(App.QApp.exec_())