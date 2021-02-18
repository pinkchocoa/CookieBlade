from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class GUIWindow(QMainWindow):
    def __init__(self):
        super(GUIWindow,self).__init__()
        self.setGeometry(0,0,500,500) #Set Window Location  & Size
        self.setWindowTitle("Cookie Crawler") #Set Window Name
        self.MainPage()
        self.setWindowIcon(QIcon('CookieIcon.jpg'))

    def MainPage(self):
        self.Mainlabel = QtWidgets.QLabel(self)
        self.Mainlabel.setText("Enter Channel Link")
        self.Mainlabel.move(200,100)
        self.Mainlabel.adjustSize()
        self.PicLabel = QtWidgets.QLabel(self)
        self.PicLabel.setText("")
        self.PicLabel.setGeometry(0,0,250,100)
        self.PicLabel.move(150,0)
        self.PicLabel.setPixmap(QPixmap('YTLogo.jpg'))
        self.PicLabel.setScaledContents(True)
        self.SearchButton = QtWidgets.QPushButton(self) #Assign Button Widget to Variable and set to appear in Main Window
        self.SearchButton.setText("Search") #Assign Text to Button Widget
        self.SearchButton.clicked.connect(self.ButtonOutput) #Link Button Output to SearchButton, function is called on button click
        self.SearchButton.move(200,300) #Set Location of Search Button
        
    def ButtonOutput(self):
        self.Mainlabel.setText("Best Youtube Video")
        self.Mainlabel.adjustSize();

def window():
    app = QApplication(sys.argv)
    Mainwin = GUIWindow() #Assign Main Window to variable
    Mainwin.show() #Make Window Appear
    sys.exit(app.exec_())

window()