
from PyQt5 import QtCore, QtGui, QtPrintSupport, QtWidgets
import pyodbc


class Ui_headControll(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("")
        MainWindow.resize(1345, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))

        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(1070, 10, 141, 91))
        self.widget_2.setStyleSheet("QWidget{\n"
                                    "border-image: url(WhatsApp Image 2021-07-04 at 6.35.44 PM.jpeg);\n"
                                    " border: 2px solid black;\n"
                                    "  border-radius: 8px;\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "\n"
                                    "}\n"
                                    "")
        self.widget_2.setObjectName("widget_2")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(790, 50, 111, 20))
        self.label_10.setStyleSheet(" border: none;\n"
                                    "font: 87 12pt \"Arial\";")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        # self.tableWidget.selectionModel().selectionChanged.connect(self.changeItemsTabel)
        delegate = Delegate(self.tableWidget)
        self.tableWidget.setItemDelegate(delegate)

        self.tableWidget.setGeometry(QtCore.QRect(40, 120, 1261, 561))
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border: 2px solid;\n"
                                       "color: rgb(85, 170, 255);\n"
                                       "font: 75 10pt  bold;\n"
                                       "font: 75 12pt \"Times New Roman\";\n")
        self.tableWidget.setLocale(QtCore.QLocale(
            QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 700, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.handlePrint)
        # self.pushButton.clicked.connect(self.UpdateAll)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 10, 981, 91))
        self.widget.setStyleSheet("QWidget{\n"
                                  " border: 2px solid black;\n"
                                  "  border-radius: 8px;\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "\n"
                                  "}\n"
                                  "")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(836, 10, 121, 20))
        self.label.setStyleSheet(" border: none;\n"
                                 "font: 87 12pt \"Arial\";\n"
                                 "")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(910, 50, 47, 21))
        self.label_2.setStyleSheet(" border: none;\n"
                                   "font: 87 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(790, 50, 111, 20))
        self.label_3.setStyleSheet(" border: none;\n"
                                   "font: 87 12pt \"Arial\";")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(290, 10, 101, 20))
        self.label_4.setStyleSheet(" border: none;\n"
                                   "font: 87 12pt \"Arial\";\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(160, 10, 141, 16))
        self.label_5.setStyleSheet(" border: none;\n"
                                   "font: 87 12pt \"Arial\";\n"
                                   "")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(340, 53, 47, 20))
        self.label_6.setStyleSheet(" border: none;\n"
                                   "font: 87 12pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(210, 60, 131, 16))
        self.label_7.setStyleSheet(" border: none;\n"
                                   "font: 87 12pt \"Arial\";")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "النتيجة"))
        MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
        self.pushButton.setText(_translate("MainWindow", "طباعة"))
        self.label.setText(_translate("MainWindow", "جامعة الازهر "))
        self.label_2.setText(_translate("MainWindow", "كلية"))
        self.label_4.setText(_translate("MainWindow", "العام الدراسي"))
        self.label_6.setText(_translate("MainWindow", "قسم"))
        # self.ReqireData()
        # self.ReqireData(0,"احياء")
   
    


    def ReqireData(self,level,department):
      

        self.Resultsconn = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')
        self.Result = self.Resultsconn.cursor()
        
        self.Result.execute(f"""Select Student.StudentName, DepartmentLevel.StudentID,  Course.CourseName,DepartmentLevel.Grad FROM Course INNER JOIN (Student INNER JOIN DepartmentLevel ON Student.StudentID = DepartmentLevel.StudentID) ON (Course.CourseID = Student.CourseID.Value) AND (Course.CourseID = DepartmentLevel.CourseID) 
        WHERE DepartmentLevel.DepartmentID={department} and DepartmentLevel.LevelID={level+1}""")
        list1 = []
        namestudent=[]
        ids=[]
        grads=[]
        self.dataResult = self.Result.fetchall()
        for i in self.dataResult:
            list1.append(i)
            if i[0] not in namestudent:
                namestudent.append(i[0])
            if i[1] not in ids:
                ids.append(i[1])
            grads.append(i[3])
            print(list1)
            print(namestudent)
            print(ids)
            print(grads)

        subjectTotal=[]
        self.Subjects = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

        self.Subject = self.Subjects.cursor()
        
        self.Subject.execute(f"""SELECT Course.CourseName, Course.Total FROM Course Where CourseDepartment={department} and CourseLevel={level+1}""")
      
        self.subjects2 = self.Subject.fetchall()
        for i in self.subjects2:
            subjectTotal.append(i)
            print(i)
        # --=-=
        
        # -==-=-
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(len(namestudent))
        header1=[
            "الاسم"
            , "رقم الجلوس"
            ,"تخلفات"
            ,"التفدير"]
        for i in range (8):
            if i<len(subjectTotal):
                header1.insert(2,subjectTotal[i][0])
            else:
                header1.insert(header1.index(header1[-2]),"")

        self.tableWidget.setHorizontalHeaderLabels(header1)


        colgrads=header1.index("")
        
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                if col==0:
                    item = QtWidgets.QTableWidgetItem(str(namestudent[row]))
                    self.tableWidget.setItem(row, 0, item)
                
                if col==1:
                    item = QtWidgets.QTableWidgetItem(str(ids[row]))
                    self.tableWidget.setItem(row, 1, item)
                if col <colgrads:
                    if col ==2 :
                            start=0
                            end=len(namestudent)
                            grad=grads[start:end]
                            item = QtWidgets.QTableWidgetItem(str(grad[row]))
                            self.tableWidget.setItem(row, 2, item)
                    if col ==3:
                            start=len(namestudent)
                            end=len(namestudent)+len(namestudent)
                            grad=grads[start:end]
                            item = QtWidgets.QTableWidgetItem(str(grad[row]))
                            self.tableWidget.setItem(row, 3, item)
                    if col ==4:
                            start=2*len(namestudent)
                            end=3*len(namestudent)
                            grad=grads[start:end]
                            item = QtWidgets.QTableWidgetItem(str(grad[row]))
                            self.tableWidget.setItem(row, 4, item)
                    if col ==5:
                            start=3*len(namestudent)
                            end=4*len(namestudent)
                            grad=grads[start:end]
                            item = QtWidgets.QTableWidgetItem(str(grad[row]))
                            self.tableWidget.setItem(row, 5, item)
                    if col ==6:
                            start=4*len(namestudent)
                            end=5*len(namestudent)
                            grad=grads[start:end]
                            item = QtWidgets.QTableWidgetItem(str(grad[row]))
                            self.tableWidget.setItem(row, 6, item)
                    if col ==7:
                            start=5*len(namestudent)
                            end=6*len(namestudent)
                            grad=grads[start:end]
                            item = QtWidgets.QTableWidgetItem(str(grad[row]))
                            self.tableWidget.setItem(row, 7, item)
                    if col ==8:
                            start=6*len(namestudent)
                            end=7*len(namestudent)
                            grad=grads[start:end]
                            item = QtWidgets.QTableWidgetItem(str(grad[row]))
                            self.tableWidget.setItem(row, 8, item)
                    if col ==9:
                            start=7*len(namestudent)
                            end=8*len(namestudent)
                            grad=grads[start:end]
                            item = QtWidgets.QTableWidgetItem(str(grad[row]))
                            self.tableWidget.setItem(row, 9, item)
                    
                    
                else:
                    # التقدير العام
                    if col==10:
                        pass

                    # مواد التخلف
                    if col==11:
                        pass


                
                
    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())

                

    
class Delegate(QtWidgets.QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        # تعديل علي حسب role
        if index.column() != 0 and index.column() != 1 and index.column() != 2 and index.column() != 3 and index.column() != 4 and index.column() != 5 and index.column() != 6 and index.column() != 7and index.column() != 8 and index.column() != 10 and index.column() != 11:
            return super(Delegate, self).createEditor(parent, option, index)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_headControll()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
    MainWindow.show()
    sys.exit(app.exec_())
