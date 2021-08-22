

from PyQt5 import QtCore, QtGui, QtWidgets
import proffsrc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1279, 720)
        Form.setStyleSheet("background-image: url(:/Image/proff4.jpg);")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(170, 440, 471, 51))
        self.comboBox.setStyleSheet("background-color: rgb(241, 235, 221);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 540, 471, 51))
        self.comboBox_2.setStyleSheet("font: 75 20pt \"Simplified Arabic\";\n"
"background-color: rgb(241, 235, 221);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 630, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(241, 235, 221);")
        self.pushButton.setObjectName("pushButton")
        self.ProffName = QtWidgets.QLabel(Form)
        self.ProffName.setGeometry(QtCore.QRect(390, 230, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ProffName.setFont(font)
        self.ProffName.setStyleSheet("background-color: rgb(241, 235, 221);")
        self.ProffName.setText("")
        self.ProffName.setObjectName("ProffName")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox_2.setItemText(0, _translate("Form", "رصد درجات أعمال السنه"))
        self.comboBox_2.setItemText(1, _translate("Form", "تعديل الدرجة النهائية"))
        self.pushButton.setText(_translate("Form", "تأكيد"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
