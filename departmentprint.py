
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc


class Ui_PrintingDep(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1345, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.pushButton.clicked.connect(self.UpdateAll)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "تعديل الدرجات"))
        self.pushButton.setText(_translate("MainWindow", "تم"))
        self.label.setText(_translate("MainWindow", "جامعة الازهر "))
        self.label_2.setText(_translate("MainWindow", "كلية"))
        MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
        self.label_4.setText(_translate("MainWindow", "العام الدراسي"))
        self.label_6.setText(_translate("MainWindow", "قسم"))

    def ReqireData(self, level, subject):
        print(subject)
        self.coursesName = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')
        
        self.course = self.coursesName.cursor()
        self.course.execute(f"SELECT CourseID FROM Course WHERE CourseName='{subject}'")
        coursesNames12=self.course.fetchall()
        for item in coursesNames12:
            
            print(item)

        self.Resultsconn = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

        self.Result = self.Resultsconn.cursor()
        self.Result.execute(f""" SELECT Student.StudentName, DepartmentLevel.StudentID,  Course.CourseName ,DepartmentLevel.Mark2
                        FROM Course INNER JOIN (Student INNER JOIN DepartmentLevel ON Student.StudentID = DepartmentLevel.StudentID) ON 
                        (Course.CourseID = Student.CourseID.Value) AND (Course.CourseID = DepartmentLevel.CourseID) WHERE CourseID={coursesNames12[0][0]}""")
        list1 = []
        self.dataResult = self.Result.fetchall()
        for i in self.dataResult:
            list1.append(i)
            print(i)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(len(list1))
        self.tableWidget.setHorizontalHeaderLabels(
            [
            "الاسم"
            , "رقم الجلوس"
            , "اسم لمادة"
            , "الدرجة"
            ])

        for row in range(len(list1)):
            for col in range(4):
                for i in self.dataResult:
                    item = QtWidgets.QTableWidgetItem(str(list1[row][col]))
                    self.tableWidget.setItem(row, col, item)

    def UpdateAll(self, data):
        edit = []
        for row in range(self.tableWidget.rowCount()):
                for col in range(self.tableWidget.columnCount()):
                    print(row, col, self.tableWidget.item(row, col).text())
                    edit.append(self.tableWidget.item(row, col).text())
        start = 0
        end = 4
        self.courses = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')
        self.course1= self.courses.cursor()
        self.course1.execute(f"SELECT CourseID FROM Course WHERE CourseName='{edit[2]}'")
        course=self.course1.fetchall()
        for i in course:
            print(i)
        while(end <= len(edit)):
            x = edit[start:end]
            self.connections = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')
            self.update = self.connections.cursor()
            print(x[3],x[2],course[0][0])
            if int(x[3])<=100 and int(x[3])>=0:
                sql = f'UPDATE DepartmentLevel SET  DepartmentLevel.Mark2 ={int(x[3])} where StudentID={x[1]} and CourseID={course[0][0]};'
                self.update.execute(sql)
                self.update.commit()                
                start += 4
                end += 4
            else:
                QtWidgets.QMessageBox.about(QtWidgets.QMessageBox(), 'خطا', 'راجع الدرجات المدخلة مره اخرى')
                break


class Delegate(QtWidgets.QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        # تعديل علي حسب role
        if index.column() != 0 and index.column() != 1 and index.column() != 2 and index.column() != 7:
            return super(Delegate, self).createEditor(parent, option, index)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_PrintingDep()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
    MainWindow.show()
    sys.exit(app.exec_())
