

from departmentprint import Ui_PrintingDep
from grads import Ui_grads
from PyQt5 import QtCore, QtGui, QtWidgets
import proffsrc
import pyodbc


class Proff_window(object):

    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1279, 720)
        Form.setStyleSheet("background-image: url(:/Image/proff4.jpg);")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(170, 440, 471, 51))
        self.comboBox.setStyleSheet("background-color: rgb(241, 235, 221);")
        self.comboBox.setStyleSheet("font: 75 20pt \"Simplified Arabic\";\n"
"background-color: rgb(241, 235, 221);")
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
        self.ProffName = QtWidgets.QLabel(Form)
        self.ProffName.setGeometry(QtCore.QRect(480, 230, 200, 31))
        self.ProffName.setFont(font)
        self.ProffName.setStyleSheet("background-color: rgb(241, 235, 221);")
        self.ProffName.setObjectName("ProffName")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(241, 235, 221);")
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.Selections)
    def Selections(self):
        if self.comboBox_2.currentIndex()==0:
            self.window3 = QtWidgets.QMainWindow()
            self.uiPrintingGrads = Ui_grads()
            self.uiPrintingGrads.setupUi(self.window3)
            self.uiPrintingGrads.editlabelsName(self.comboBox.currentText())
            self.uiPrintingGrads.dataReqired(self.comboBox.currentText())
            # ------------------------------------------------
            

            # --
            self.window3.show()
        elif(self.comboBox_2.currentIndex()==1):
            self.window2 = QtWidgets.QMainWindow()
            self.uiPrinting = Ui_PrintingDep()
            self.uiPrinting.setupUi(self.window2)
            self.coursesName = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

            self.course = self.coursesName.cursor()
            self.course.execute(f"SELECT CourseFaculty,CourseDepartment,Year FROM Course WHERE CourseName='{self.comboBox.currentText()}'")
            coursesNames12=self.course.fetchall()
            print(f"{coursesNames12}")
            # -=-=-=-
            self.DataName = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

            self.course = self.DataName.cursor()
            self.course.execute(f""" select FacultyName from Faculty inner join Department on Faculty.FacultyID= Department.DepartmentFaculty
where FacultyID={coursesNames12[0][0]}""")
            Data=self.course.fetchall()
            print(f"{Data}")
            # ---
            self.DepartmentName = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

            self.Deparment = self.DepartmentName.cursor()
            self.Deparment.execute(f""" select DepartmentName   from Course inner join Department on Department.DepartmentID= Course.CourseDepartment
where CourseDepartment={coursesNames12[0][1]}""")
            Data1=self.Deparment.fetchall()
            print(f"{Data1}")
            # faculty
            self.uiPrinting.label_3.setText(Data[0][0])
            # department
            self.uiPrinting.label_7.setText(Data1[0][0])
            # year
            self.uiPrinting.label_5.setText(str(coursesNames12[0][2]))


            self.uiPrinting.ReqireData("",self.comboBox.currentText())

            

            self.window2.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "السادة اعضاء هيئة التدريس"))
        Form.setWindowIcon(QtGui.QIcon("logo.png"))
        self.comboBox_2.setItemText(0, _translate("Form", "رصد درجات أعمال السنة"))
        self.comboBox_2.setItemText(1, _translate("Form", "تعديل الدرجة النهائية"))
        self.pushButton.setText(_translate("Form", "تأكيد"))



