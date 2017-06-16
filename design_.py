from PyQt4 import QtCore, QtGui
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
leftbutton = 16 
rightbutton = 18

GPIO.setup(leftbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName(_fromUtf8("main"))
        main.resize(800, 502)
        self.centralwidget = QtGui.QWidget(main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.vscomputerlabel = QtGui.QLabel(self.centralwidget)
        self.vscomputerlabel.setGeometry(QtCore.QRect(440, 80, 291, 291))
        self.vscomputerlabel.setText(_fromUtf8(""))
        self.vscomputerlabel.setPixmap(QtGui.QPixmap(_fromUtf8("computer.png")))
        self.vscomputerlabel.setScaledContents(True)
        self.vscomputerlabel.setObjectName(_fromUtf8("vscomputerlabel"))
        self.pvplabel = QtGui.QLabel(self.centralwidget)
        self.pvplabel.setGeometry(QtCore.QRect(40, 80, 311, 311))
        self.pvplabel.setText(_fromUtf8(""))
        self.pvplabel.setPixmap(QtGui.QPixmap(_fromUtf8("playerb.png")))
        self.pvplabel.setScaledContents(True)
        self.pvplabel.setObjectName(_fromUtf8("pvplabel"))
        self.vscomputerblacklabel = QtGui.QLabel(self.centralwidget)
        self.vscomputerblacklabel.setGeometry(QtCore.QRect(440, 80, 291, 291))
        self.vscomputerblacklabel.setText(_fromUtf8(""))
        self.vscomputerblacklabel.setPixmap(QtGui.QPixmap(_fromUtf8("computerbl.png")))
        self.vscomputerblacklabel.setScaledContents(True)
        self.vscomputerblacklabel.setObjectName(_fromUtf8("vscomputerblacklabel"))
        self.pvpblacklabel = QtGui.QLabel(self.centralwidget)
        self.pvpblacklabel.setGeometry(QtCore.QRect(40, 80, 311, 311))
        self.pvpblacklabel.setText(_fromUtf8(""))
        self.pvpblacklabel.setPixmap(QtGui.QPixmap(_fromUtf8("playerbl.png")))
        self.pvpblacklabel.setScaledContents(True)
        self.pvpblacklabel.setObjectName(_fromUtf8("pvpblacklabel"))
        self.vscomputerblacklabel.raise_()
        self.vscomputerlabel.raise_()
        self.pvplabel.raise_()
        self.pvpblacklabel.raise_()
        self.vscomputerblacklabel.setVisible(True)
        self.vscomputerlabel.setVisible(False)
        self.pvplabel.setVisible(True)
        self.pvpblacklabel.setVisible(False)
        main.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(main)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)
   
     while(1):
        if GPIO.input(rightbutton) == 0:
            self.pvpblacklabel.setVisible(True)
            self.vscomputerlabel.setVisible(True)
            self.pvplabel.setVisible(False)
            self.vscomputerblacklabel.setVisible(False)

    def retranslateUi(self, main):
        main.setWindowTitle(_translate("main", "MainWindow", None))
