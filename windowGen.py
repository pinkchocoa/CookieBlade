## @file windowGen.py
#
# @brief this file contain windowGen class
#
# @section libraries_main Libraries/Modules
# - GUIWidgets (local)
#   - access to classes from GUIWidgets.py

# Imports
from GUIWidgets import * #contain class from GUIwidgets.py.

def emptyFn(): #dun remove this.
    pass

class windowGen():
    

    def __init__(self):
        self.window = newWidgetPage()
        #to keep track of what i've set, all widgets unset are at 0,0,0,0
        self.nLabel = 0
        self.nText = 0
        self.nPush = 0
        self.nLGraph = 0
        self.nBrowser = 0
        self.nPieChart = 0
        self.nBarChart = 0

        self.totalNLabel = 0
        self.totalNText = 0
        self.totalNPush = 0
        self.totalnLGraph = 0
        self.totalNPieChart = 0
        self.totalNBrowser = 0
        self.totalNBarChart = 0

        self.labelList = []
        self.textList = []
        self.pushList = []
        self.lineGraphList = []
        self.pieChartList = []
        self.barChartList = []
        self.browserList = []


    def addNewLineGraph(self):
        self.lineGraphList.append(newGraph(self.window.page, 0, 0, 800, 800))
        self.totalnLGraph+=1

    def setLineGraph(self,posX, posY, lenX, lenY,
    axisX, axisY, lineColor, points,
    bgColor,
    title, titleColor, titleSize,
    position, label, labelColor, labelSize,
    position2, label2, labelColor2, labelSize2,
    axisLabel="left", axis=[]):
        if self.nLGraph >= self.totalnLGraph:
            self.addNewLineGraph()
        Graph = self.lineGraphList[self.nLGraph]
        Graph.Graph.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Enables graph to show grid
        Graph.Graph.showGrid(x = True, y = True)
        #Graph.plot(axisX, axisY, pen = lineColor, symbol = points)
        Graph.plotGraph(axisX, axisY, lineColor, points)
        Graph.setBackGroundColor(bgColor)
        Graph.setGraphTitle(title, titleColor, titleSize)
        Graph.setAxisLabel(position, label, labelColor, labelSize)
        Graph.setAxisLabel(position2, label2, labelColor2, labelSize2)
        if axis:
            Graph.setAxisIntervalTo1(axisLabel, axis)
        self.nLGraph+=1

    def addnewLabel(self):
        self.labelList.append(newLabel(self.window.page,0,0,0,0))
        self.totalNLabel+=1

    def setLabel(self, posX, posY, lenX, lenY, text="", image="", fontStyle="", fontSize="", functionName="", scaled = True):
        if self.nLabel >= self.totalNLabel:
            self.addnewLabel()
        label = self.labelList[self.nLabel].label
        #Set Label x & y position and size
        label.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Set alignment of Label text to align left and centered
        label.setAlignment(QtCore.Qt.AlignLeft)
        label.setAlignment(QtCore.Qt.AlignVCenter)
        if text:
            label.setText(text)
            label.update()
        if image:
            #Set display image in parameter in Label
            label.setPixmap(QtGui.QPixmap(image))
            #Enable image scaling to fit Label size
            label.setScaledContents(True)
        if fontStyle and fontSize:
            label.setFont(QtGui.QFont(fontStyle, fontSize))
        else:
            label.setFont(QtGui.QFont("Arial", 10))
        if functionName:
            label.mousePressEvent = functionName
        if scaled:
            label.setScaledContents(scaled)

        self.nLabel+=1

    def addnewTextBox(self):
        self.textList.append(newTextBox(self.window.page,0,0,0,0))
        self.totalNText+=1

    def setTextbox(self, posX, posY, lenX, lenY, text="", fontStyle="", fontSize=""):
        if self.nText >= self.totalNText:
            self.addnewTextBox()
        textbox = self.textList[self.nText].textbox
        #Initialize new instance of TextBox UI
        textbox = QLineEdit(self.window.page)
        #Set TextBox x & y position and size
        textbox.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        if text:
            textbox.setPlaceholderText(text)
        if fontStyle and fontSize:
            textbox.setFont(QtGui.QFont(fontStyle,int(fontSize)))
        self.nText+=1

    def addNewPush(self):
        self.pushList.append(newPushButton(self.window.page,0,0,0,0,emptyFn))
        self.totalNPush+=1

    def setPush(self, posX, posY, lenX, lenY, functionName, text="", fontStyle="", fontSize=""):
        if self.nPush >= self.totalNPush:
            self.addNewPush()
        pushButton = self.pushList[self.nPush].PushButton
        #Initialize new instance of PushButton UI
        pushButton = QPushButton(self.window.page)
        #Set PushButton x & y position and size
        pushButton.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Calls function when PushButton is clicked
        pushButton.clicked.connect(functionName)
        if text:
            pushButton.setText(text)
        if fontStyle and fontSize:
            pushButton.setFont(QtGui.QFont(fontStyle,int(fontSize)))
        else:
            pushButton.setFont(QtGui.QFont("Arial", 10))
        self.nPush+=1
    
    def addNewBrowser(self):
        self.browserList.append(newWebBrowser(0, 0,))
        self.totalNBrowser+=1

    def setBrowser(self, lenX, lenY, link):
        if self.nBrowser >= self.totalNBrowser:
            self.addNewBrowser()
        webBrowser = self.browserList[self.nBrowser].webEngine
        webBrowser = QWebEngineView(self.window.page)
        webBrowser.resize(lenX,lenY)
        webBrowser.setWindowTitle(link)
        webBrowser.load(QtCore.QUrl(link))
        webBrowser.show()
        self.nBrowser+=1


    def addNewPieChart(self):
        self.pieChartList.append(newPieChart())
        self.totalNPieChart+=1

    #data is a dictionary
    def setPieChart(self, data, title="", x=0, y=0, width=300, height=300):
        #missing set x, y
        #  posX, posY
        if self.nPieChart >= self.totalNPieChart:
            self.addNewPieChart()
        pieChart = self.pieChartList[self.nPieChart]
        #pieChart.setSize(width,height)
        pieChart.viewChart(self.window.page)
        pieChart.setPos(x,y,width,height)
        pieChart.addData(data)
        pieChart.setTitle(title)
        
        self.nPieChart+=1

    def addNewBarChart(self):
        self.barChartList.append(newBarChart())
        self.totalNBarChart+=1

    #data is a list of list
    #categories is a list
    def setBarChart(self, data, categories, x=0,y=0,size=500,title=""):
        #missing set x, y
        #  posX, posY
        if self.nBarChart >= self.totalNBarChart:
            self.addNewBarChart()
        barChart = self.barChartList[self.nBarChart]
        barChart.addData(data, categories)
        barChart.viewChart(self.window.page,x,y,size)
        barChart.setTitle(title)
        self.nBarChart+=1

    def show(self):
        self.window.page.show()

    def hide(self):
        self.window.page.hide()

    def isVisible(self):
        return self.window.page.isVisible()