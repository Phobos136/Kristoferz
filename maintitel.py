import sys
from PyQt4 import QtGui, QtCore

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
        elif event.key() == QtCore.Qt.Key_Right:
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
        elif event.key() == QtCore.Qt.Key_Left:
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
