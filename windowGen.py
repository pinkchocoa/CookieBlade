from GUIWidgets import * #contain class from GUI.py and GUIwidgets.py.

def emptyFn():
    pass

class windowGen(NewWindow):
    totalNLabel = 1
    totalNText = 1
    totalNPush = 1

    labelList = []
    textList = []
    pushList = []


    def __init__(self, name, width, height, nLabel,nText,nPush):
        super().__init__(name, width, height)

        #to keep track of what i've set, all widgets unset are at 0,0,0,0
        self.nLabel = 0
        self.nText = 0
        self.nPush = 0

        #total number of widgets that this window owns
        self.totalNLabel = nLabel
        self.totalNText = nText
        self.totalNPush = nPush
        
        for x in range(nLabel):
            self.labelList.append(NewLabel(self.QWin,0,0,0,0))
        for x in range(nText):
            self.textList.append(NewTextBox(self.QWin,0,0,0,0))
        for x in range(nPush):
            self.pushList.append(NewPushButton(self.QWin,0,0,0,0,emptyFn))

    def addNewLabel(self):
        self.labelList.append(NewLabel(self.QWin,0,0,0,0))
        self.totalNLabel+=1

    def setLabel(self, posX, posY, lenX, lenY, text="", image=""):
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
        self.nLabel+=1

    def addNewTextbox(self):
        self.textList.append(NewTextBox(self.QWin,0,0,0,0))
        self.totalNText+=1

    def setTextbox(self, posX, posY, lenX, lenY, text=""):
        if self.nText >= self.totalNText:
            self.addNewTextbox()
        textbox = self.textList[self.nText].textbox
        #Initialize new instance of TextBox UI
        textbox = QLineEdit(self.QWin)
        #Set TextBox x & y position and size
        textbox.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        if text:
            textbox.setPlaceholderText(text)
        self.nText+=1

    def addNewPush(self):
        self.pushList.append(NewPushButton(self.QWin,0,0,0,0,emptyFn))
        self.totalNPush+=1

    def setPush(self, posX, posY, lenX, lenY, functionName, text=""):
        if self.nPush >= self.totalNPush:
            self.addNewPush()
        PushButton = self.pushList[self.nPush].PushButton
        #Initialize new instance of PushButton UI
        PushButton = QPushButton(self.QWin)
        #Set PushButton x & y position and size
        PushButton.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Calls function when PushButton is clicked
        PushButton.clicked.connect(functionName)
        if text:
            PushButton.setText(text)
        self.nPush+=1

    def show(self):
        self.QWin.show()

    def hide(self):
        self.QWin.hide()