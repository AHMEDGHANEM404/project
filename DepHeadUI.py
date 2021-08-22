
# from departmentprint import Ui_PrintingDep
from headcontrollRole import Ui_headControll
from PyQt5 import QtCore, QtGui, QtWidgets
import DepHeadSRC
from BarChart2 import ChartShow
import pyodbc

class DepHead_window(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1279, 720)
        Form.setStyleSheet("background-image: url(:/images/DepHead2.jpg);")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(260, 310, 481, 71))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("font: 75 20pt \"Simplified Arabic\";\n")
        self.comboBox.addItem("الفرقة الأولي")
        self.comboBox.addItem("الفرقة الثانية")
        self.comboBox.addItem("الفرقة الثالثة")
        self.comboBox.addItem("الفرقة الرابعة")
        self.name=''
        self.updatedb()
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(260, 560, 481, 71))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setStyleSheet("font: 75 20pt \"Simplified Arabic\";\n")
        self.comboBox_2.addItem("الفرقة الأولي")
        self.comboBox_2.addItem("الفرقة الثانية")
        self.comboBox_2.addItem("الفرقة الثالثة")
        self.comboBox_2.addItem("الفرقة الرابعة")
        # self.comboBox.currentIndexChanged.connect(self.changes)
        # self.comboBox_2.currentIndexChanged.connect(self.changes)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.PrintGrades)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 580, 101, 31))
        # self.pushButton_2.clicked.connect(self.ShowGraph)
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 86, 140, 21))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2.clicked.connect(self.New_instance)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def PrintGrades(self):
        self.window2 = QtWidgets.QMainWindow()
        self.uiPrinting = Ui_headControll()
        self.uiPrinting.setupUi(self.window2)
        # self.uiPrinting.ReqireData(self.comboBox.currentIndex())
        self.Resultsconn = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')


        self.Result = self.Resultsconn.cursor()
        list1=[]
        self.Result.execute(f"""select ProfessorFaculty ,ProfessorDepartment from Professor where ProfessorName='{self.name}'""")
        print(self.Result)
        for i in self.Result:
            print(i[0])
            list1.append(i)

        # insert labels
#         # faculty
        self.DataName = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

        self.course = self.DataName.cursor()
        self.course.execute(f""" select FacultyName  from Faculty inner join Department on Faculty.FacultyID= Department.DepartmentFaculty
where FacultyID={list1[0][0]}""")
        faculty=self.course.fetchall()
        print(f"{faculty}")
        # department
        self.Department = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

        self.Dep = self.Department.cursor()
        self.Dep.execute(f""" select DepartmentName  from Department inner join Professor on Professor.ProfessorDepartment= Department.DepartmentID where ProfessorDepartment={list1[0][1]}""")
        deparment=self.Dep.fetchall()
        print(f"{deparment}")
           # faculty
        self.uiPrinting.label_3.setText(faculty[0][0])
            # department
        self.uiPrinting.label_7.setText(deparment[0][0])
            # year
        self.uiPrinting.label_5.setText(str("2021"))
        # show student
        print(self.comboBox.currentIndex(),list1[0][1])
        self.uiPrinting.ReqireData(self.comboBox.currentIndex(),list1[0][1])
        self.window2.show()


    def updatedb(self):
        # get total each Subject
        totalGrads=[]
        totalGradSutdent=[]
        self.updateDbCells= pyodbc.connect(
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

        self.dataUpdated=self.updateDbCells.cursor() 
        self.dataUpdated.execute(f"SELECT DepartmentLevel.CourseID, Course.Total,  DepartmentLevel.Total  , DepartmentLevel.StudentID from DepartmentLevel inner join Course on DepartmentLevel.CourseID=Course.CourseID;")
        self.dataEnded=self.dataUpdated.fetchall()
        for i in self.dataEnded:
            # print (i)
            totalGradSutdent.append(i)
            grad=[
                "راسب"
                ,"مقبول"
                ,"جيد" 
                ,"جيد جدا"
                ,"امتياز"
            ]
        for j in totalGradSutdent:
            gradPercentage= ((j[2]/j[1])*100)
            # print(gradPercentage) 
            if gradPercentage >float(50.00) and gradPercentage <float(65):
                             totalGrads.append((grad[1],j[0],j[3]))
            if gradPercentage <float(75.00) and gradPercentage >float(65):
                             totalGrads.append((grad[2],j[0],j[3]))
            if gradPercentage <float(85.00) and gradPercentage >float( 75):
                          totalGrads.append((grad[3],j[0],j[3]))
            if gradPercentage > float(85.00) and gradPercentage <=float(100):
                             totalGrads.append((grad[4],j[0],j[3]))
            if gradPercentage ==float(65.00):
                             totalGrads.append((grad[2],j[0],j[3]))
            if gradPercentage ==float(75.00):
                             totalGrads.append((grad[4],j[0],j[3]))
            if gradPercentage ==float(85.00):
                             totalGrads.append((grad[5],j[0],j[3]))
            if gradPercentage ==float(50.00):
                            totalGrads.append((grad[1],j[0],j[3]))  
            if gradPercentage <float(50.00):
                            totalGrads.append((grad[0],j[0],j[3]))
            
            

        print(totalGrads)
        # update grads
        self.connections = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

        self.updateStudent = self.connections.cursor()
        for i in range(len(totalGrads)):
            self.updateStudent.execute(f"UPDATE DepartmentLevel  SET DepartmentLevel.Grad='{totalGrads[i][0]}' where DepartmentLevel.StudentID={totalGrads[i][2]} and DepartmentLevel.CourseID={totalGrads[i][1]}   ")
        
        self.connections.commit()
        self.connections.close()
        print("done")


        


    def changes(self,value):
        print(value)
        
    def New_instance(self):
        self.studentSubTotal = pyodbc.connect(
                            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                            r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')



        self.maxSub=self.studentSubTotal.cursor() 
        # and CourseFaculty={}
        subject=[]
        self.maxSub.execute(f"select CourseName from  Course where  Course.CourseLevel={self.comboBox_2.currentIndex()}+1 ")
        self.totalSub=self.maxSub.fetchall()
        for i in self.totalSub:
            print(i[0])
            subject.append(i[0])
        self.instance=ChartShow() 
        self.instance.input.clear()
               
        for item in subject:
            self.instance.input.addItem(item)
        self.instance.show()
     
        

        pass
        
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "مرحبا بكم رئيس القسم"))
        Form.setWindowIcon(QtGui.QIcon("logo.png"))
        self.pushButton.setText(_translate("Form", "عرض"))
        self.pushButton_2.setText(_translate("Form", "عرض"))
        self.label.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui =DepHead_window()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
    MainWindow.show()
    sys.exit(app.exec_())

