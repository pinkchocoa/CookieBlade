## @file GUIWidgets.py
#
# @brief this file contains GUI Widget Classes
#
# @section libraries_main Libraries/Modules
# - sys standard library (https://docs.python.org/3/library/sys.html)
#   - access to sys.argv and sys.exit functions
# - PyQt5 external library (pip install PyQt5)
#   - access to PyQt5 GUI functions
# - PyQt5.QtWidgets external library
#   - access to PyQt5 UI Widgets
# - PyQt5.QtChart external library (pip inststall PyQtChart)
#   - access to PyQt5 bar and pie chart plotting fuctions
# - pyqtgraph external library (pip install pyqtgraph)
#   - access to graph plotting functions
# - functools standard library
#   - tools to work with high order functions

# Imports
import sys
from PyQt5 import QtCore, QtGui, QtWidgets #pip3 install pyqt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import * #pip3 install PyQtWebEngine
from PyQt5.QtChart import * #pip3 install PyQtChart
from pyqtgraph import PlotWidget, plot, exporters #pip3 install pyqtgraph
import functools
from singleSpider import spidey
from twitter import Twitter

## Documentation for GUIWidgets.py
# Contains all UI Widget classes
# We can reuse classes to make different widgets for diffferent purpose

#Class to initialize a new instance of QApplication module which is required to run PyQt5
class startApp:
    """! startApp class
    Defines the QApplication object which allows the creation of all QtWidgets
    """
    def __init__(self):
        self.QApp = QApplication(sys.argv)

#Class to create a new Window
class newWindow:
    """! newWindow class
    Defines the window object used to display widgets
    """
    def __init__(self, name, lenX, lenY):
        """! newWindow class initializer
        @param name used to name the window title
        @param lenX used to set the horizontal length of the window
        @param lenY used to set the veritical height of the window
        """
        #Initialize new instance of Window UI
        self.QWin = QMainWindow()
        #Set Window Title
        self.QWin.setWindowTitle(name)
        #Set Window Size
        self.QWin.resize(lenX,lenY)

    #Method to set Window icon image
    def setWindowIcon(self,image):
        """! set the window icon to the image from input parameter
        @param image image to be used as Window Icon
        """
        self.QWin.setWindowIcon(QtGui.QIcon(image))
    
    def show(self):
        """! set window to be visible
        """
        #Display window
        self.QWin.show()

#Class to create a stack widget
class newStackWidget:
    """! newStackWidget class
    Defines the stack widget object used to store and load widget pages
    """
    def __init__(self, window, posX, posY, lenX, lenY):
        """! newStackWidget class initializer
        @param window used to determine which window for the stack widget to appear on
        @param posX used to set the X coordinate of where the stack widget will appear
        @param posY used to set the Y coordinate of where the stack widget will appear
        @param lenX used to set the horizontal length of the stack widget
        @param lenY used to set the vertical height of the stack widget
        """
        self.sWidget = QtWidgets.QStackedWidget(window)
        #Set the position and size of the stack widget
        self.sWidget.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Set the stack widget index to point to the first widget page
        self.sWidget.setCurrentIndex(0)
    
    def addWidget(self, widget):
        """! used to add a widget page into the stack widget
        @param widget to be added to stack widget
        """
        self.sWidget.addWidget(widget)
    
    def setCurrentWidget(self, widget):
        """! used to set selected page of widgets to be displayed
        @param widget to be set as the current page
        """
        self.sWidget.setCurrentWidget(widget.page)

#Class to create a new widget page
class newWidgetPage:
    """! newWidgetPage class
    Defines the widget page object used to store multiple widgets to be loaded by stack widget
    """
    def __init__(self):
        """! newStackWidget class initializer used to create a new widget page
        """
        self.page = QtWidgets.QWidget()

#Class to create a new Label
class newLabel:
    """! newLabel class
    Defines the label object used to display text label to guide users
    """
    def __init__(self, window, posX, posY, lenX, lenY):
        """! newLabel class initializer
        @param window used to determine which window for the widget to appear on
        @param posX used to set the X coordinate of where the label will appear
        @param posY used to set the Y coordinate of where the label will appear
        @param lenX used to set the horizontal length of the label
        @param lenY used to set the vertical height of the label
        """
        #Initialize new instance of Label UI
        self.label = QLabel(window)
        #Set Label x & y position and size
        self.label.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Set alignment of Label text to align center
        self.label.setAlignment(QtCore.Qt.AlignCenter)

    #Method to set Label Text
    def setText(self, text):
        """! used to set the text that will be displayed by the label widget
        @param text string of text to be displayed
        """
        self.label.setText(text)
        #Automatically update the length of label to fit text
        self.label.update()

    def setFont(self, fontStyle, fontSize):
        """! sets the font style and size of the label widget
        @param fontStyle used to set the font style of label text
        @param fontSize used to set the font size of label text
        """
        self.label.setFont(QFont(fontStyle, fontSize))
    
    #Method to display image in Label
    def setImage(self, image):
        """! set label to display image
        @param image used to determine what image to be displayed in label
        """
        #Set display image in parameter in Label
        self.label.setPixmap(QtGui.QPixmap(image))
        #Enable image scaling to fit Label size
        self.label.setScaledContents(True)

#Class to create new TextBox
class newTextBox:
    """! newTextBox class
    Defines the textbox object used to retrieve user input
    """
    def __init__(self, window, posX, posY, lenX, lenY):
        """! newTextBox class initializer
        @param window used to determine which window for the widget to appear on
        @param posX used to set the X coordinate of where the textbox will appear
        @param posY used to set the Y coordinate of where the textbox will appear
        @param lenX used to set the horizontal length of the textbox
        @param lenY used to set the vertical height of the textbox
        @return user input stored in textbox
        """
        #Initialize new instance of TextBox UI
        self.textbox = QtWidgets.QLineEdit(window)
        #Set TextBox x & y position and size
        self.textbox.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))

    #Method to set palceholder text
    def setText(self, text):
        """! set placeholder text to be displayed by the textbox
        @param text used to set the text to be displayed by the textbox
        """
        self.textbox.setPlaceholderText(text)
    
    def setFont(self, fontStyle, fontSize):
        """! set the font style and font size of textboxes
        @param fontStyle used to set the font style of textbox placeholder text
        @param fontSize used to set the font size of textbox placeholder text
        """
        self.textbox.setFont(QFont(fontStyle,int(fontSize)))

    def returnText(self):
        """! used to retrieve the user input from textboxes
        """
        return self.textbox.text()

#Class to create new PushButton
class newPushButton:
    """! newPushButton class
    Defines the PushButton object to recieve button click input
    """
    def __init__(self, window, posX, posY, lenX, lenY, functionName):
        """! newPushButton class initializer
        @param window used to determine which window for the widget to appear on
        @param posX used to set the X coordinate of where the push button will appear
        @param posY used to set the Y coordinate of where the push button will appear
        @param lenX used to set the horizontal length of the push button
        @param lenY used to set the vertical height of the push button
        @param functionname used to determine which function to call when button is clicked
        """
        #Initialize new instance of PushButton UI
        self.PushButton = QPushButton(window)
        #Set PushButton x & y position and size
        self.PushButton.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Calls function when PushButton is clicked
        self.PushButton.clicked.connect(functionName)

    #Set PushButton text
    def setText(self, text):
        """! set the text to be displayed on the push button
        @param text used to set the text to be displayed by the push button
        """
        self.PushButton.setText(text)
    
    def setFont(self, fontStyle, fontSize):
        """! set the font style and font size of text displayed on the push button
        @param fontStyle used to set the font style of push button text
        @param fontSize used to set the font size of push button text
        """
        self.PushButton.setFont(QFont(fontStyle,int(fontSize)))

#Class to create new messagebox object
class messageBox:
    """! messageBox class
    Defines the message box object to display error messages
    """
    def __init__(self, winTitle="", text="", winIcon="" ,show=True,icon="Critical"):
        """! messageBox class initializer
        @param winTitle used to set the messagebox window title
        @param text string value will be displayed in message box
        @param winIcon contains the image name used to set the window icon of message box
        @param show value set to true to show message box, false to hide message box
        @param icon used to determine which icon to be displayed with message box text
        """
        #Initialized a new instance of message box UI
        self.msgBox = QMessageBox()
        msgBox = self.msgBox
        if winTitle:
            msgBox.setWindowTitle(winTitle)
        if winIcon:
            msgBox.setWindowIcon(QtGui.QIcon(winIcon))
        if text:
            msgBox.setText(text)
        if icon == "Critical":
            msgBox.setIcon(QMessageBox.Critical)
        if show:
            self.show()

    def show(self):
        """! set the messagebox to be visible
        """
        msgBox = self.msgBox
        msgBox.exec_()

#Class to create new Graph
class newGraph:
    """! newGraph class
    Defines the Graph object to take in input and display graph
    """
    def __init__(self, window, posX, posY, lenX, lenY):
        """! NewGraph class initializer
        @param window used to determine which window for the graph to appear on
        @param posX used to set the X coordinate of where the graph will appear
        @param posY used to set the Y coordinate of where the graph will appear
        @param lenX used to set the horizontal length of the graph
        @param lenY used to set the vertical height of the graph
        """
        self.Graph = PlotWidget(window)
        self.Graph.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Enables graph to show grid
        self.Graph.showGrid(x = True, y = True)

    def plotGraph(self, axisX, axisY, color, points):
        """! take in values for X and Y axis, line color and points to plot graph
        @param axisX takes in list to plot the X axis of graph
        @param axisY takes in list to plot the Y axis of graph
        @param color used to determine the line color of graph
        @param points used to determine symbol used to mark points
        """
        self.Graph.plot(axisX, axisY, pen = color, symbol = points)
        
    def setBackGroundColor(self, color):
        """! sets the background color of the graph
        @param color used to set the background color of graph
        """
        self.Graph.setBackground(color)
    
    def setGraphTitle(self, title, titleColor, titleSize):
        """! sets the title of the graph
        @param title used to set the graph title label
        @param titleColor used to set the graph title color
        @param titleSize used to set the font size of graph title
        """
        self.Graph.setTitle(title, color = titleColor, size = titleSize)

    def setAxisLabel(self, position, label, labelColor, labelSize):
        """! sets the axis label of the graph
        @param position used to determine the position of axis
        @param label used to determine what to display for axis
        @param labelcolor used to determine the color for axis
        @param labelSize used to determine the font size of axis
        """
        fontstyle = {"color":labelColor, "font-size":labelSize}
        self.Graph.setLabel(position, label, **fontstyle)
    
    def setAxisIntervalTo1(self, axisLabel, axis):
        """! sets the axis to be in intervals of 1
        @param axisLabel used to determine which axis label to re-set interval
        @param axis used to determine the range of values to set for axis
        """
        storeAxis = self.Graph.getAxis(axisLabel)
        getValues = [(value, str(value)) for value in (range(int(min(axis)), int(max(axis)+1)))]
        storeAxis.setTicks([getValues, []])
    
#Class to create new pie chart
class newPieChart():
    """! newPieChart class
    Defines the pie chart object to display pie charts
    """
    def __init__(self):
        """! newPieChart class initializer
        """
        self.chart = QChart()
        #Set chart animation
        self.chart.setAnimationOptions(QChart.AllAnimations)
        
        #self.chart.legend().setAlignment(QtCore.Qt.AlignLeft)
        #self.chart.mapToPosition(QtCore.QPointF(500,500))
        self.chart.setBackgroundVisible(True)
        self.series = QPieSeries()
        #Set pie chart legend to be non visible
        self.chart.legend().setVisible(False)
        #self.chart.legend().setAlignment(QtCore.Qt.AlignBottom)
        

    def setPos(self, posX, posY, width, height):
        """! set the position and size of pie chart
        @param posX used to determine the X coordinate of pie chart
        @param posY used to determine the Y coordinate of pie chart
        @param width used to set the width of pie chart
        @param height used to set the height of pie chart
        """
        pos = QtCore.QRectF()
        pos.setHeight(width)
        pos.setWidth(height)
        pos.moveTo(posX,posY)#This move the pi chart without the label.
        self.chart.setPlotArea(pos)

    def setSize(self, width, height):
        """! sets the area where the pie chart can be displayed
        @param width used to determine the width of the area
        @param height used to determine the height of the area
        """
        self.chartview.setFixedSize(width,height)

    def setTitle(self, title):
        """! sets the title of pie chart
        @param title input to be set as pie chart title
        """
        self.chart.setTitle(title)

    def setSeries(self, series):
        """! used to add a series of values to be displayed on the pie chart
        @param series a list of values to be displayed on the pie chart
        """
        self.chart.addSeries(series)

    def setwindowGenObj(self, window):
        self.windowGen = window

    #data is a dictionary
    def addData(self, data):
        """! used to split series of data into seperate slices on the pie chart
        @param data a dictionary of values
        """
        minSize = 0.1
        maxSize = 0.9
        donut = QPieSeries()
        sliceCount = len(data)
        j=0
        for x,y in data.items():
            slice_ = QPieSlice(x,y)
            slice_.setLabelVisible(True)
            slice_.setLabelColor(Qt.white)
            slice_.setLabelPosition(QPieSlice.LabelInsideTangential)
            #Set pie slices to detect mouse hover
            slice_.hovered[bool].connect(functools.partial(self.explodeSlice, slice_=slice_))
            #Set pie slices to detect mouse double click input
            slice_.doubleClicked.connect(functools.partial(self.doubleClickSlice, slice_=slice_))
            donut.append(slice_)
            donut.setHoleSize(minSize)
            donut.setPieSize(minSize + (1) * (maxSize - minSize) )
            j+=1

        self.setSeries(donut)
    
    def viewChart(self, window):
        """! used to set the pie chart to be visible
        @param window used to determine which window for the pie chart to be displayed
        """
        self.chartview = QChartView(self.chart, window)
        self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)

    def explodeSlice(self, exploded, slice_):
        """! called when mouse hover is detected to perform pie slice movement
        @param exploded used to set slice movement
        @param slice_ used to determine which slice to move
        """
        if exploded:
            text = str(slice_.label())
            text += ": "
            text += str(int(slice_.value()))
            text += " tweets"
            self.chart.setToolTip(text)
        else:
            self.chart.setToolTip("")
        slice_.setExploded(exploded)

    def doubleClickSlice(self, slice_):
        """! called when mouse double click input is detected
        @param slice_ used to determine which slice to perform action on
        """
        index = 3
        text = str(slice_.label())
        links = spidey(['articles'],text,3)
        #links = {'https://news.google.com/articles/CAIiEFSOiYliYGuKi2zIiuYHCwsqGAgEKg8IACoHCAowqKTyCTDY83IwpLrsBQ?hl=en-SG&gl=SG&ceid=SG%3Aen', 'https://news.google.com/articles/CBMiVmh0dHBzOi8vNDExbWFuaWEuY29tL3dyZXN0bGluZy92YXJpb3VzLW5ld3MtbGFuYS1nZXRzLWEtY2hpcm9wcmFjdGljLWFkanVzdG1lbnQtdmlkZW8v0gEA?hl=en-SG&gl=SG&ceid=SG%3Aen', 'https://news.google.com/articles/CAIiEE5ROMPJsH4t5RDqxWMjYvIqGQgEKhAIACoHCAow8KiRCzCh9qUDMI2c1gY?hl=en-SG&gl=SG&ceid=SG%3Aen'}
        #how to display these links?
        for idx, x in enumerate(links):
            text = "Link " + str(idx+1) + " Generated!"
            self.windowGen.labelList[self.windowGen.totalNLabel-index+idx].label.setText(text)
        #i want to search tweets too
        search = Twitter()
        tweets = search.searchKeyword(text)
        print(tweets)

        


class newBarChart():
    """! newBarChart class
    Defines the bar chart object to display bar charts
    """
    def __init__(self):
        """! newBarChart class initializer
        """
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        
        #self.chart.legend().setAlignment(QtCore.Qt.AlignLeft)
        #self.chart.mapToPosition(QtCore.QPointF(500,500))
        self.chart.setBackgroundVisible(False)
        self.series = QPercentBarSeries()
        
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignBottom)


    def setTitle(self, title):
        """! used to set bar chart title
        @param title used to set title name
        """
        self.chart.setTitle(title)

    #data is a list of list
    def addData(self, data, categories):
        """! used to input data into bar chart to be displayed
        @param data to be displayed as bar charts
        @param categories used to show what each bar chart represent
        """
        for a in data:
            tempset = QBarSet(a[0])
            for idx, x in enumerate(a):
                if idx == 0:
                    continue
                tempset << x
            self.series.append(tempset)

        axis = QBarCategoryAxis()
        axis.append(categories)
        self.chart.createDefaultAxes()
        #self.chart.setAxisX(axis, self.series)
        self.chart.addAxis(axis, Qt.AlignBottom)
        #self.chart.addAxis(self.series, Qt.AlignLeft)
        self.chart.addSeries(self.series)
        axisY = QValueAxis()
        self.chart.addAxis(axisY, Qt.AlignLeft)
        self.series.attachAxis(axisY)
        axisY.setRange(0,50)
    
    def viewChart(self, window, posX, posY,sizex, sizey):
        """! set bar chart as visible
        @param window used to determine which window the bar chart will appear on
        @param posX used to determine the X coordinate of bar chart
        @param posY used to determine the Y coordinate of bar chart
        @param size used to determine the size of the bar chart
        """
        self.chartview = QChartView(self.chart, window)
        self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)

        #need to find the equivalent of this in his stackwidget
        #window.setCentralWidget(self.chartview)
        test = QtCore.QRectF()
        test.setHeight(sizey)
        test.setWidth(sizex)
        test.moveTo(posX,posY)#This move the pi chart without the label.
        self.chart.setPlotArea(test)
        self.chartview.resize(1000,800)