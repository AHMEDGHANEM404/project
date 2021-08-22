
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc


class Ui_grads(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1142, 753)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 1101, 601))
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        delegate = Delegate(self.tableWidget)
        self.tableWidget.setItemDelegate(delegate)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 710, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.UpdateAll)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 40, 201, 16))
        self.label.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 40, 47, 13))
        self.label_2.setStyleSheet("font: 75 11pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def editlabelsName(self, subname):
        self.label_2.setText(subname)

    def dataReqired(self, subjectname):
        list1=[]
        self.coursesName = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')


        self.course = self.coursesName.cursor()
        self.course.execute(
            f"SELECT CourseID FROM Course WHERE CourseName='{subjectname}'")
        subname = self.course.fetchall()
        print(subname[0][0])
        self.conn4 = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

        self.z = self.conn4.cursor()
        self.z.execute(f"""SELECT Student.StudentName, Course.CourseName,DepartmentLevel.StudentID, DepartmentLevel.Mark1
                            FROM Course INNER JOIN (Student INNER JOIN DepartmentLevel ON Student.StudentID = DepartmentLevel.StudentID) 
                            ON (Course.CourseID = Student.CourseID.Value) AND (Course.CourseID = DepartmentLevel.CourseID) 
                            WHERE Course.CourseID={int(subname[0][0])}""")
        self.Items = self.z.fetchall()
        for n in self.Items:
            list1.append(n)
            print(n)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(len(list1))
        self.tableWidget.setHorizontalHeaderLabels(
            ["الاسم", "المادة", "رقم الجلوس", "درجة اعمال السنة"])

        for row in range(len(list1)):
            for col in range(4):
                for i in self.Items:
                    item = QtWidgets.QTableWidgetItem(str(list1[row][col]))
                    self.tableWidget.setItem(row, col, item)
    def UpdateAll(self, data):
        edit = []
        
        for row in range(self.tableWidget.rowCount()):
                for col in range(self.tableWidget.columnCount()):
                    print(row, col, self.tableWidget.item(row, col).text())
                    edit.append(self.tableWidget.item(row, col).text())
        print(edit)
        start = 0
        end = 4
        x = edit[start:end]
        self.courses = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')
        self.course1= self.courses.cursor()
        self.course1.execute(f"SELECT CourseID FROM Course WHERE CourseName='{x[1]}'")
        course=self.course1.fetchall()
        for item in course:
                print(item[0])

        while(end <= len(edit)):
                x = edit[start:end]
                self.connections = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')


                self.update = self.connections.cursor()
                # and CourseID={}
                if int(x[3])<=50 and int(x[3])>=0:
                    sql = f'UPDATE DepartmentLevel SET  DepartmentLevel.Mark1 ={int(x[3])} where StudentID={x[2]} and   CourseID={course[0][0]} '
                    self.update.execute(sql)
                    self.update.commit()
                    start += 4
                    end += 4
                else:
                    QtWidgets.QMessageBox.about(QtWidgets.QMessageBox(), 'خطا', 'راجع الدرجات المدخلة مره اخرى')
                    break
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "درجات اعمال السنة"))
        self.pushButton.setText(_translate("MainWindow", "تم"))
        MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
        self.label.setText(_translate("MainWindow", "اعمال السنة لمادة"))
        self.label_2.setText(_translate("MainWindow", "كذا"))
class Delegate(QtWidgets.QStyledItemDelegate):
    
    def createEditor(self, parent, option, index):
        # تعديل علي حسب role
        if index.column() != 0 and index.column() != 1 and index.column() != 2 :
            return super(Delegate, self).createEditor(parent, option, index)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_grads()
    ui.setupUi(Form)
    Form.setWindowIcon(QtGui.QIcon("logo.png"))
    Form.show()
    sys.exit(app.exec_())
