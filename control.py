

from departmentprint import Ui_PrintingDep
from PyQt5 import QtCore, QtGui, QtWidgets
import controlsrc
import pyodbc


class Control_window(object):


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1279, 720)
        Form.setStyleSheet("background-image: url(:/images/controlsrc.jpg);")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(170, 440, 471, 51))
        self.comboBox.setStyleSheet("background-color: rgb(241, 235, 221);")
        self.comboBox.setStyleSheet("font: 75 20pt \"Simplified Arabic\";\n"
"background-color: rgb(241, 235, 221);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        # self.comboBox.currentIndexChanged.connect(self.comboChanged)

        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 540, 471, 51))
        self.comboBox_2.setStyleSheet("background-color: rgb(241, 235, 221);")
        self.comboBox_2.setStyleSheet("font: 75 20pt \"Simplified Arabic\";\n"
"background-color: rgb(241, 235, 221);")
        self.comboBox_2.setObjectName("comboBox_2")
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
        self.ProffName2 = QtWidgets.QLabel(Form)
        self.ProffName2.setGeometry(QtCore.QRect(480, 260, 191, 41))
        self.ProffName2.setFont(font)
        self.ProffName2.setStyleSheet("background-color: rgb(241, 235, 221);")
        self.ProffName2.setObjectName("ProffName")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
       
        self.comboBox.setItemText(0, _translate("Form", "الفرقة الأولي"))
        self.comboBox.setItemText(1, _translate("Form", "الفرقة الثانية"))
        self.comboBox.setItemText(2, _translate("Form", "الفرقة الثالثة"))
        self.comboBox.setItemText(3, _translate("Form", "الفرقة الرابعة"))
        self.pushButton.setText(_translate("Form", "تأكيد"))
        self.pushButton.clicked.connect(self.TablePrint)


    def TablePrint(self):
        self.window2 = QtWidgets.QMainWindow()
        self.uiPrinting = Ui_PrintingDep()
        self.uiPrinting.setupUi(self.window2)
        self.coursesName = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')
        self.course = self.coursesName.cursor()
        self.course.execute(f"SELECT CourseFaculty,CourseDepartment,Year FROM Course WHERE CourseName='{self.comboBox_2.currentText()}'")
        coursesNames12=self.course.fetchall()
        print(f"{coursesNames12}")
            # -=-=-=-
        self.DataName = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

        self.course = self.DataName.cursor()
        self.course.execute(f""" select FacultyName ,DepartmentName ,DepartmentID from Faculty inner join Department on Faculty.FacultyID= Department.DepartmentFaculty
where FacultyID={coursesNames12[0][0]}""")
        Data=self.course.fetchall()
        print(f"{Data}")
        self.uiPrinting.ReqireData(self.comboBox.currentIndex()+1,self.comboBox_2.currentText())

        self.uiPrinting.label_3.setText(Data[0][0])
        self.uiPrinting.label_7.setText(Data[0][1])
        self.uiPrinting.label_5.setText(str(coursesNames12[0][2]))
        self.window2.show()
        # Form.hide()
        pass



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Control_window()
#     ui.setupUi(Form)
#     Form.setWindowIcon(QtGui.QIcon("logo.png"))
#     Form.show()
#     sys.exit(app.exec_())
