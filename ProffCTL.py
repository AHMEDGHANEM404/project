
import ProffCtrlSRC

from PyQt5 import QtCore, QtGui, QtWidgets
from FinalLevelGrades import FinalLevel_grads

class LevelCTLWin(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1279, 720)
        Form.setStyleSheet("background-image: url(:/Images/ProffCtrl.jpg);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(480, 260, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(225, 480, 471, 51))
        self.comboBox.setStyleSheet("background-color: rgb(241, 235, 221);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("font: 75 20pt \"Simplified Arabic\";\n"
"background-color: rgb(241, 235, 221);")
        self.comboBox.clear()
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 580, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.level=0
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(241, 235, 221);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ShowFinal)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "كنترول الفرق"))
        Form.setWindowIcon(QtGui.QIcon("logo.png"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "تأكيد"))
    
    def ShowFinal(self):

        self.window3 = QtWidgets.QMainWindow()
        self.uiPrintingGrads = FinalLevel_grads()
        self.uiPrintingGrads.setupUi(self.window3)
        self.uiPrintingGrads.editlabelsName(self.comboBox.currentText())
        self.uiPrintingGrads.dataReqired(self.comboBox.currentText())
        self.window3.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LevelCTLWin()
    ui.setupUi(MainWindow)
    # MainWindow.addItemTable(1)
    MainWindow.show()
    sys.exit(app.exec_())


