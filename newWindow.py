from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newWindow(object):
    def setupUi(self, newWindow):
        newWindow.setObjectName("newWindow")
        newWindow.resize(800, 600)
        newWindow.setWindowIcon(QtGui.QIcon("CookieIcon.png"))
        self.centralwidget = QtWidgets.QWidget(newWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 230, 71, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 210, 91, 111))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 81, 51))
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 100, 81, 51))
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 140, 81, 51))
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        newWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(newWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        newWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(newWindow)
        self.statusbar.setObjectName("statusbar")
        newWindow.setStatusBar(self.statusbar)

        self.retranslateUi(newWindow)
        QtCore.QMetaObject.connectSlotsByName(newWindow)

    def retranslateUi(self, newWindow):
        _translate = QtCore.QCoreApplication.translate
        newWindow.setWindowTitle(_translate("newWindow", "newWindow"))
        self.label.setText(_translate("newWindow", "Subscriber Count:"))
        self.label_2.setText(_translate("newWindow", "URL"))
        self.label_3.setText(_translate("newWindow", "UID"))
        self.label_4.setText(_translate("newWindow", "PW"))



