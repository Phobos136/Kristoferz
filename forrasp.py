import sys
from PyQt4 import QtGui, QtCore
import RPi.GPIO as GPIO
import time
import virtkey
v = virtkey.virtkey()
buttonleft=12
buttonright=16
buttondown=27
buttonup=3
buttonSelect=21
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonleft, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttondown, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonright, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonup, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonSelect, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:

    while True:
        time.sleep(0.15)
        #left
        if (GPIO.input(buttonleft) == 0):
            v.press_unicode(ord('A'))
            v.release_unicode(ord('A'))
        #down            
        elif (GPIO.input(buttondown) == 0):
            v.press_unicode(ord('S'))
            v.release_unicode(ord('S'))
        #right
        elif (GPIO.input(buttonright) == 0):
            v.press_unicode(ord('D'))
            v.release_unicode(ord('D'))
        #up
        elif (GPIO.input(buttonup) == 0):
            v.press_unicode(ord('W'))
            v.release_unicode(ord('W'))
        #select     
        elif (GPIO.input(buttonSelect) == 0):
            v.press_unicode(ord(' '))
            v.release_unicode(ord(' '))
            time.sleep(0.3)
            
except KeyboardInterrupt:
    pass

    
GPIO.cleanup()
class Experiment(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowTitle('Experiment')
        self.resize(800, 480)
        self.connect(self, QtCore.SIGNAL('closeEmitApp()'), QtCore.SLOT('close()') )


        pvplabelbegin = QtGui.QLabel(self)
        pvplabelbegin.setGeometry(QtCore.QRect(40, 80, 311, 311))
        pvplabelbegin.setPixmap(QtGui.QPixmap("playerb.png"))
        pvplabelbegin.setScaledContents(True)
        pvplabelbegin.setVisible(True)

        vscomputerblacklabelbegin = QtGui.QLabel(self)
        vscomputerblacklabelbegin.setGeometry(QtCore.QRect(440, 80, 291, 291))
        vscomputerblacklabelbegin.setPixmap(QtGui.QPixmap("computerbl.png"))
        vscomputerblacklabelbegin.setScaledContents(True)
        vscomputerblacklabelbegin.setVisible(True)

        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif event.key() == QtCore.Qt.Key_D:
            pvplabelbegin = QtGui.QLabel(self)
            pvplabelbegin.setGeometry(QtCore.QRect(40, 80, 311, 311))
            pvplabelbegin.setPixmap(QtGui.QPixmap("playerb.png"))
            pvplabelbegin.setScaledContents(True)
            pvplabelbegin.setVisible(False)

            vscomputerblacklabelbegin = QtGui.QLabel(self)
            vscomputerblacklabelbegin.setGeometry(QtCore.QRect(440, 80, 291, 291))
            vscomputerblacklabelbegin.setPixmap(QtGui.QPixmap("computerbl.png"))
            vscomputerblacklabelbegin.setScaledContents(True)
            vscomputerblacklabelbegin.setVisible(False)

            vscomputerlabel = QtGui.QLabel(self)
            vscomputerlabel.setGeometry(QtCore.QRect(440, 80, 291, 291))
            vscomputerlabel.setPixmap(QtGui.QPixmap("computer.png"))
            vscomputerlabel.setScaledContents(True)
            vscomputerlabel.setVisible(True)

            pvplabel = QtGui.QLabel(self)
            pvplabel.setGeometry(QtCore.QRect(40, 80, 311, 311))
            pvplabel.setPixmap(QtGui.QPixmap("playerb.png"))
            pvplabel.setScaledContents(True)
            pvplabel.setVisible(False)

            vscomputerblacklabel = QtGui.QLabel(self)
            vscomputerblacklabel.setGeometry(QtCore.QRect(440, 80, 291, 291))
            vscomputerblacklabel.setPixmap(QtGui.QPixmap("computerbl.png"))
            vscomputerblacklabel.setScaledContents(True)
            vscomputerblacklabel.setVisible(False)

            pvpblacklabel = QtGui.QLabel(self)
            pvpblacklabel.setGeometry(QtCore.QRect(40, 80, 311, 311))
            pvpblacklabel.setPixmap(QtGui.QPixmap("playerbl.png"))
            pvpblacklabel.setScaledContents(True)
            pvpblacklabel.setVisible(True)
        elif event.key() == QtCore.Qt.Key_A:
            pvplabelbegin = QtGui.QLabel(self)
            pvplabelbegin.setGeometry(QtCore.QRect(40, 80, 311, 311))
            pvplabelbegin.setPixmap(QtGui.QPixmap("playerb.png"))
            pvplabelbegin.setScaledContents(True)
            pvplabelbegin.setVisible(False)

            vscomputerblacklabelbegin = QtGui.QLabel(self)
            vscomputerblacklabelbegin.setGeometry(QtCore.QRect(440, 80, 291, 291))
            vscomputerblacklabelbegin.setPixmap(QtGui.QPixmap("computerbl.png"))
            vscomputerblacklabelbegin.setScaledContents(True)
            vscomputerblacklabelbegin.setVisible(False)

            vscomputerlabel = QtGui.QLabel(self)
            vscomputerlabel.setGeometry(QtCore.QRect(440, 80, 291, 291))
            vscomputerlabel.setPixmap(QtGui.QPixmap("computer.png"))
            vscomputerlabel.setScaledContents(True)
            vscomputerlabel.setVisible(False)

            pvplabel = QtGui.QLabel(self)
            pvplabel.setGeometry(QtCore.QRect(40, 80, 311, 311))
            pvplabel.setPixmap(QtGui.QPixmap("playerb.png"))
            pvplabel.setScaledContents(True)
            pvplabel.setVisible(True)

            vscomputerblacklabel = QtGui.QLabel(self)
            vscomputerblacklabel.setGeometry(QtCore.QRect(440, 80, 291, 291))
            vscomputerblacklabel.setPixmap(QtGui.QPixmap("computerbl.png"))
            vscomputerblacklabel.setScaledContents(True)
            vscomputerblacklabel.setVisible(True)

            pvpblacklabel = QtGui.QLabel(self)
            pvpblacklabel.setGeometry(QtCore.QRect(40, 80, 311, 311))
            pvpblacklabel.setPixmap(QtGui.QPixmap("playerbl.png"))
            pvpblacklabel.setScaledContents(True)
            pvpblacklabel.setVisible(False)
            
    
app = QtGui.QApplication(sys.argv)
ui = Experiment()
ui.show()
sys.exit(app.exec_())
