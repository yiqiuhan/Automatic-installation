
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,time,threading,os
import automaticinstallationwithcmd
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QThread, pyqtSignal

global sec
sec = 7200000

#This class is additional
class verCompare(QThread):
    trigger = pyqtSignal(str, str)
    def __init__(self, netdisk):
        self.netdisk = netdisk
    def run(self):
        time.sleep(2)
        self.trigger.emit('10', '11')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 330, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 60, 581, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 170, 241, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 300, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.launchcampare)
        self.pushButton.clicked.connect(self.timing)
        self.pushButton.clicked.connect(self.countdown)
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(340, 200, 251, 91))
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 170, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        #self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        #self.checkBox.setGeometry(QtCore.QRect(260, 340, 71, 16))
        #font = QtGui.QFont()
        #font.setPointSize(8)
        #self.checkBox.setFont(font)
        #self.checkBox.setObjectName("checkBox")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 581, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer=QTimer()
        

    def clickBox(self, state):
        x = 10
        if state == QtCore.Qt.Checked:
            x = 100
            print('Checked')
        else:
            x = 200
            print('Unchecked')

    def enableRunImmediate(self, bEnable):
        self.pushButton.setEnabled(bEnable)

    def timing(self):
        print('cc')        
        self.timer.timeout.connect(self.launchcampare)
        self.timer.start(sec)#count every seconds

    def stoptiming(self):
        self.timing.stop()
      
        
    def launchcampare (self):

        if not self.pushButton.isEnabled:
            return
        self.enableRunImmediate(False)
        netdisk = self.comboBox.currentText()
        self.c = automaticinstallationwithcmd.versioncampare(netdisk)
        self.c.updateRunImmediate.connect(self.enableRunImmediate)
        self.c.textone.connect(self.displaycampare)
        self.c.texttwo.connect(self.displayprocess)
        self.c.start()
        
        

    def displayprocess (self,message):
        self.textBrowser.append(message)
    def displaycampare (self,message):
        self.textBrowser_2.append(message)
    

    def countdown(self):
        self.time_left_int = sec/1000
        self.timer2=QTimer()
        self.timer2.timeout.connect(self.timeout)
        self.timer2.start(1000)
        
        
    def timeout(self):
        self.time_left_int-=1
        if self.time_left_int == 0:
           self.time_left_int = sec/1000
        
        self.updategui()
        
    def updategui(self):
        
        self.lcdNumber.display(self.time_left_int)
          

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inventor R24 automatic installation"))
        self.comboBox.setItemText(0, _translate("MainWindow", "//panda"))
        self.comboBox.setItemText(1, _translate("MainWindow", "//bobcat"))
        self.comboBox.setItemText(2, _translate("MainWindow", "//beaver"))
        self.comboBox.setItemText(3, _translate("MainWindow", "//bear"))
        self.comboBox.setItemText(4, _translate("MainWindow", "//hare"))
        self.comboBox.setItemText(5, _translate("MainWindow", "//lion"))
        self.comboBox.setItemText(6, _translate("MainWindow", "//bison"))
        self.comboBox.setItemText(7, _translate("MainWindow", "//deer"))
        self.label.setText(_translate("MainWindow", "Senna"))
        self.pushButton.setText(_translate("MainWindow", "Execute immediately"))
        self.label_2.setText(_translate("MainWindow", "Time before next execution"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "QA"))
        #self.comboBox_2.setItemText(1, _translate("MainWindow", "Dev"))
        #self.comboBox_2.setItemText(2, _translate("MainWindow", "Branch (Altrap)"))
        #self.checkBox.setText(_translate("MainWindow", "6xx builds"))

class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self,event):
        #self.uiWindow.timer.stop()
        #event.accept()
        reply = QtWidgets.QMessageBox.question(self,
                                               'This program',
                                               "Exit the program？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            
                self.uiWindow.timer.stop()
                event.accept()               
        else:
            event.ignore()
        
        
    def setUiWindow(self, uiWindow):
        self.uiWindow = uiWindow


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = MyWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setUiWindow(ui)

    MainWindow.show()
    
    sys.exit(app.exec_())
    
    
