from GUIWidgets import * #contain class from GUI.py and GUIwidgets.py.

def emptyFn():
    pass

class windowGen(NewWindow):
    totalNLabel = 0
    totalNText = 0
    totalNPush = 0
    totalNGraph = 0

    labelList = []
    textList = []
    pushList = []
    graphList = []


    def __init__(self, name, width, height, nLabel=0,nText=0,nPush=0, nGraph=0):
        super().__init__(name, width, height)

        #to keep track of what i've set, all widgets unset are at 0,0,0,0
        self.nLabel = 0
        self.nText = 0
        self.nPush = 0
        self.nGraph = 0

        #total number of widgets that this window owns
        self.totalNLabel = nLabel
        self.totalNText = nText
        self.totalNPush = nPush
        self.totalNGraph = nGraph
        
        for x in range(nLabel):
            self.labelList.append(NewLabel(self.QWin,0,0,0,0))
        for x in range(nText):
            self.textList.append(NewTextBox(self.QWin,0,0,0,0))
        for x in range(nPush):
            self.pushList.append(NewPushButton(self.QWin,0,0,0,0,emptyFn))
        for x in range(nGraph):
            self.graphList.append(NewGraph(self.QWin, 0, 0, 800, 800))

    def addNewGraph(self):
        self.graphList.append(NewGraph(self.QWin, 0, 0, 800, 800))
        self.totalNGraph+=1

    def setGraph(self,posX, posY, lenX, lenY,
    axisX, axisY, lineColor, points,
    bgColor,
    title, titleColor, titleSize,
    position, label, labelColor, labelSize,
    axisLabel="left", axis=[]):
        if self.nGraph >= self.totalNGraph:
            self.addNewGraph()
        Graph = self.graphList[self.nGraph].Graph
        Graph.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Enables graph to show grid
        Graph.showGrid(x = True, y = True)
        Graph.plotGraph(axisX, axisY, lineColor, points)
        Graph.setBackGroundColor(bgColor)
        Graph.setGraphTitle(title, titleColor, titleSize)
        Graph.setAxisLabel(position, label, labelColor, labelSize)
        if axis:
            Graph.setAxisIntervalTo1(axisLabel, axis)

    def addNewLabel(self):
        self.labelList.append(NewLabel(self.QWin,0,0,0,0))
        self.totalNLabel+=1

    def setLabel(self, posX, posY, lenX, lenY, text="", image="", fontStyle="", fontSize=""):
        if self.nLabel >= self.totalNLabel:
            self.addNewLabel()
        label = self.labelList[self.nLabel].label
        #Set Label x & y position and size
        label.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Set alignment of Label text to align center
        label.setAlignment(QtCore.Qt.AlignCenter)
        if text:
            label.setText(text)
        if image:
            #Set display image in parameter in Label
            label.setPixmap(QtGui.QPixmap(image))
            #Enable image scaling to fit Label size
            label.setScaledContents(True)
        if fontStyle and fontSize:
            label.setFont(QFont(fontStyle, fontSize))

        self.nLabel+=1

    def addNewTextbox(self):
        self.textList.append(NewTextBox(self.QWin,0,0,0,0))
        self.totalNText+=1

    def setTextbox(self, posX, posY, lenX, lenY, text="", fontStyle="", fontSize=""):
        if self.nText >= self.totalNText:
            self.addNewTextbox()
        textbox = self.textList[self.nText].textbox
        #Initialize new instance of TextBox UI
        textbox = QLineEdit(self.QWin)
        #Set TextBox x & y position and size
        textbox.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        if text:
            textbox.setPlaceholderText(text)
        if fontStyle and fontSize:
            textbox.setFont(QFont(fontStyle,int(fontSize)))
        self.nText+=1

    def addNewPush(self):
        self.pushList.append(NewPushButton(self.QWin,0,0,0,0,emptyFn))
        self.totalNPush+=1

    def setPush(self, posX, posY, lenX, lenY, functionName, text="", fontStyle="", fontSize=""):
        if self.nPush >= self.totalNPush:
            self.addNewPush()
        pushButton = self.pushList[self.nPush].PushButton
        #Initialize new instance of PushButton UI
        pushButton = QPushButton(self.QWin)
        #Set PushButton x & y position and size
        pushButton.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Calls function when PushButton is clicked
        pushButton.clicked.connect(functionName)
        if text:
            pushButton.setText(text)
        if fontStyle and fontSize:
            pushButton.setFont(QFont(fontStyle,int(fontSize)))
        self.nPush+=1

    def show(self):
        self.QWin.show()

    def hide(self):
        self.QWin.hide()