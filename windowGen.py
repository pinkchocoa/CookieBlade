## @file windowGen.py
#
# @brief this file contain windowGen class
#
# @author JiaJun(5%)
# @author Jodie(95%)
#
# @section libraries_main Libraries/Modules
# - GUIWidgets (local)
#   - access to classes from GUIWidgets.py

# Imports
from GUIWidgets import * #contain class from GUIwidgets.py.

## Documentation for windowGen.py
# Contains windowGen class which allows creation of widgets with only a single call for each widget
# We can reuse classes to make different widgets for diffferent purpose

def emptyFn():
    """! this function is used to initlised push buttons
    """
    pass

class windowGen():
    """! windowGen class
    Defines the windowGen object which will perform the creation of widgets
    """
    def __init__(self):
        """! windowGen class initializer
        Initialize new widget page, variable and lists to keep track of number of widgets
        """
        self.window = newWidgetPage()
        #to keep track of what i've set, all widgets unset are at 0,0,0,0
        self.nLabel = 0
        self.nText = 0
        self.nPush = 0
        self.nLGraph = 0
        self.nPieChart = 0
        self.nBarChart = 0

        self.totalNLabel = 0
        self.totalNText = 0
        self.totalNPush = 0
        self.totalnLGraph = 0
        self.totalNPieChart = 0
        self.totalNBarChart = 0

        self.labelList = []
        self.textList = []
        self.pushList = []
        self.lineGraphList = []
        self.pieChartList = []
        self.barChartList = []

    def addNewLineGraph(self):
        """! initialize a new graph widget
        """
        self.lineGraphList.append(newGraph(self.window.page, 0, 0, 800, 800))
        self.totalnLGraph+=1

    def setLineGraph(self,posX, posY, lenX, lenY,
    axisX, axisY, lineColor, points,
    bgColor,
    title, titleColor, titleSize,
    position, label, labelColor, labelSize,
    position2, label2, labelColor2, labelSize2,
    axisLabel="left", axis=[]):
        """! set properties of line graph
        @param posX determines the X coordinate of the line graph
        @param posY determines the Y coordinate of the line graph
        @param lenX determines the width of the line graph
        @param lenY determines the height of the line graph
        @param axisX contains the values for X axis
        @param axisY contains the vlaues for Y axis
        @param lineColor determines the color of line in the line graph
        @param points determines the symbol used to mark points
        @param title determines the title name of the line graph
        @param titleColor determines the color for title name
        @param titleSize determines the size of title name
        @param position determines the position of axis labels
        @param label determines the axis label text
        @param labelColor determines the color of axis label text
        @param labelSize determines the size of axis label text
        @param position2 determines the position of the second axis label
        @param label2 determines the second axis label text
        @param labelColor2 determines the color of the second axis label text
        @param labelSize2 determines the size of the second axis label text
        @param axisLabel used to determine which axis label to re-set interval
        @param axis used to determine the range of values to set for axis
        """
        if self.nLGraph >= self.totalnLGraph:
            self.addNewLineGraph()
        Graph = self.lineGraphList[self.nLGraph]
        Graph.Graph.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Enables graph to show grid
        Graph.Graph.showGrid(x = True, y = True)
        Graph.Graph.setFixedSize(lenX, lenY)
        Graph.plotGraph(axisX, axisY, lineColor, points)
        Graph.setBackGroundColor(bgColor)
        Graph.setGraphTitle(title, titleColor, titleSize)
        Graph.setAxisLabel(position, label, labelColor, labelSize)
        Graph.setAxisLabel(position2, label2, labelColor2, labelSize2)
        if axis:
            Graph.setAxisIntervalTo1(axisLabel, axis)
        self.nLGraph+=1
        return Graph

    def addnewLabel(self):
        """! initialize a new label widget
        """
        self.labelList.append(newLabel(self.window.page,0,0,0,0))
        self.totalNLabel+=1

    def setLabel(self, posX, posY, lenX, lenY, text="", image="", fontStyle="", fontSize="", functionName="", scaled = True):
        """! set properties of label widget
        @param posX determines the X coordinate of the label
        @param posY determines the Y coordinate of the label
        @param lenX determines the width of the label
        @param lenY determines the height of the label
        @param text determines the text to be displayed by the label widget
        @paran image determiens image to be displayed
        @param fontStyle determines the front style of text displayed by the label widget
        @param fontSize determines the front size of text displayed by the label widget
        @param functionName determines which function to call when a mouse click is detected
        @param scaled set image displayed in label to scale
        """
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
        return self.labelList[self.nLabel-1]

    def addnewTextBox(self):
        """! initialize a new textbox widget
        """
        self.textList.append(newTextBox(self.window.page,0,0,0,0))
        self.totalNText+=1

    def setTextbox(self, posX, posY, lenX, lenY, text="", fontStyle="", fontSize=""):
        """! set properties of textbox widget
        @param posX determines the X coordinate of the textbox
        @param posY determines the Y coordinate of the textbox
        @param lenX determines the width of the textbox
        @param lenY determines the height of the textbox
        @param text determines the text to be displayed by the textbox widget
        @param fontStyle determines the front style of text displayed by the textbox widget
        @param fontSize determines the front size of text displayed by the textbox widget
        """
        if self.nText >= self.totalNText:
            self.addnewTextBox()
        textbox = self.textList[self.nText].textbox
        #Set TextBox x & y position and size
        textbox.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        if text:
            textbox.setPlaceholderText(text)
        if fontStyle and fontSize:
            textbox.setFont(QtGui.QFont(fontStyle,int(fontSize)))
        self.nText+=1
        return self.textList[self.nText-1]

    def addNewPush(self):
        """! initialize a new pushbutton widget
        """
        self.pushList.append(newPushButton(self.window.page,0,0,0,0,emptyFn))
        self.totalNPush+=1

    def setPush(self, posX, posY, lenX, lenY, functionName, text="", fontStyle="", fontSize=""):
        """! set properties of pushbutton widget
        @param posX determines the X coordinate of the pushbutton
        @param posY determines the Y coordinate of the pushbutton
        @param lenX determines the width of the pushbutton
        @param lenY determines the height of the pushbutton
        @param functionName determines which function to call when a mouse click is detected
        @param text determines what text to be displayed on the button
        @param fontStyle determines the front style of text displayed by the pushbutton widget
        @param fontSize determines the front size of text displayed by the pushbutton widget
        """
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
        return self.pushList[self.nPush-1]
    
    def addNewBrowser(self):
        """! initialize a new webbrowser widget
        """
        self.browserList.append(newWebBrowser(0, 0,))
        self.totalNBrowser+=1

    def addNewPieChart(self):
        """! initialize a new piechart widget
        """
        self.pieChartList.append(newPieChart())
        self.totalNPieChart+=1

    #data is a dictionary
    def setPieChart(self, data, title="", posX=0, posY=0, width=300, height=300):
        """! set properties of the piechart widget
        @param data a dictionary of values
        @param title determines the title name of the piechart
        @param posX determines the X coordinate of the piechart
        @param posY determines the Y coordinate of the piechart
        @param width determines the width of the piechart
        @param height determines the height of the piechart
        """
        if self.nPieChart >= self.totalNPieChart:
            self.addNewPieChart()
        pieChart = self.pieChartList[self.nPieChart]
        pieChart.viewChart(self.window.page)
        pieChart.setwindowGenObj(self)
        pieChart.setPos(posX,posY,width,height)
        pieChart.addData(data)
        pieChart.setTitle(title)
        
        self.nPieChart+=1
        return pieChart

    def addNewBarChart(self):
        """! initialize a new barchart widget
        """
        self.barChartList.append(newBarChart(self.window.page))
        self.totalNBarChart+=1

    #data is a list of list
    #categories is a list
    def setBarChart(self, data, categories, posX=0,posY=0,sizex=500,sizey=500,title=""):
        """! set properties of the barchart widget
        @param data
        @param categories
        @param posX determines the X coordinate of the barchart
        @param posY determines the Y coordinate of the barchart
        @param sizex determines the horizontal size of the barchart
        @param sizey determines the vertical size of the barchart
        @param title determines the title name of the barchart
        """
        #missing set x, y
        #  posX, posY
        if self.nBarChart >= self.totalNBarChart:
            self.addNewBarChart()
        barChart = self.barChartList[self.nBarChart]
        barChart.addData(data, categories)
        barChart.setSize(posX,posY,sizex, sizey)
        self.nBarChart+=1
        return barChart

    def show(self):
        """! set widget page to be visible
        """
        self.window.page.show()

    def hide(self):
        """! set widget page to be non visible
        """
        self.window.page.hide()

    def isVisible(self):
        """! check if a widget page is visible
        """
        return self.window.page.isVisible()