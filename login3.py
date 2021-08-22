

from ProffCTL import LevelCTLWin
from DepHeadUI import DepHead_window
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pyodbc

import loginsrc
from Proff2 import Proff_window
from control import Control_window


class createConnection():

    def __init__(self):
        self.conn = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')



        self.c=self.conn.cursor() 

    def auth(self,username, password):
       
        self.c.execute("SELECT * FROM Login WHERE UserName=? and Password=? ",username,password)
        self.data=self.c.fetchone()

        if not self.data:
            QMessageBox.warning(QMessageBox(), 'Error', 'User Not found')
            sys.exit()


    def role(self, username):
        self.conn2 = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                            r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')



        self.x=self.conn2.cursor() 
        self.x.execute("SELECT Administration FROM Professor WHERE Professor.ProfessorUsername=? ",username)
        
        self.data2=self.x.fetchone()
        global roleID
        roleID = self.data2[0]
        print (roleID)
        
        

class Ui_Form(object):
    

    def OpenProffWin(self):
        self.window = QtWidgets.QMainWindow()
        self.uiProff = Proff_window()
        self.uiProff.setupUi(self.window)
        self.uiProff.ProffName.setText(self.ProName[0])
        self.window.show()
        Form.hide()

    def OpenControlWin(self):
        self.window2 = QtWidgets.QMainWindow()
        self.uiControl = Control_window()
        self.uiControl.setupUi(self.window2)
        self.uiControl.ProffName2.setText(self.ProName[0])
        self.window2.show()
        Form.hide()
    def OpendepHead(self):
        self.window2 = QtWidgets.QMainWindow()
        self.uiDepHead = DepHead_window()
        self.uiDepHead.setupUi(self.window2)
        self.uiDepHead.label.setText(self.ProName[0])
        self.uiDepHead.name=self.ProName[0]
        self.window2.show()
        Form.hide()
    def OpendepHead2(self):
        self.window2 = QtWidgets.QMainWindow()
        self.HeadLevel = LevelCTLWin()
        self.HeadLevel.setupUi(self.window2)
        self.HeadLevel.label.setText(self.ProName[0])
        self.window2.show()
        Form.hide()
   
    

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1280, 690)
        Form.setStyleSheet("background-image: url(:/images/Design-2.jpg);")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(590, 540, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.search)
        
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(460, 300, 361, 81))
        self.lineEdit.setStyleSheet("font: 18pt \"Dubai\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 440, 361, 81))
        self.lineEdit_2.setStyleSheet("font: 18pt \"Dubai\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.returnPressed.connect(self.commandLinkButton.click)
        self.lineEdit.returnPressed.connect(self.commandLinkButton.click)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # # موقف التقديرات
        # self.updatedb()

    def search(self):
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()

        self.NameConn= pyodbc.connect(
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                 r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')


        self.cur=self.NameConn.cursor() 
        self.cur.execute(f"SELECT ProfessorName from Professor WHERE ProfessorUsername=?;",self.username)
        
        self.ProName=self.cur.fetchone()
        print (self.ProName)

        connection = createConnection()
        connection.auth(self.username, self.password)
        connection.role(self.username)

        if roleID == "Professor":
            self.OpenProffWin()
            self.conn3= pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
             r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')


            self.y=self.conn3.cursor() 
            self.y.execute(f"SELECT CourseName FROM Course where Course.CourseProfessor.value in (SELECT Professor.ProfessorID from Professor  where ProfessorUsername='{self.username}')")
            self.Items=self.y.fetchall()
            for i in self.Items:
                self.uiProff.comboBox.addItem(i[0])
                print(i[0])
            
        elif roleID == "Head-Control":
            self.OpenControlWin()
            self.uiControl.comboBox.currentIndexChanged[int].connect(self.combochanged)   
            
        elif roleID =="Head-Department":
            self.OpendepHead()

        elif roleID =="Head-Control2":
            self.ControlLevels=[]
            self.OpendepHead2()
            # SELECT ProfessorName from Professor WHERE ProfessorUsername=?;
            self.control= pyodbc.connect(
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                 r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

            self.RoleControl=self.control.cursor() 
            self.RoleControl.execute(f"SELECT ProfessorSsn from Professor where ProfessorUsername='{self.username}';")
            for i in self.RoleControl:
                print(i[0])
                self.ControlLevels.append(i)
                print(self.ControlLevels)
            
            self.HeadLevel.comboBox.clear()
            subjectLevel1=[]
            self.subject= pyodbc.connect(
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                 r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

            self.subject1=self.subject.cursor() 
            self.subject1.execute(f"SELECT CourseName from Course inner join Professor on Course.CourseProfessor.value=Professor.ProfessorID where  CourseLevel={self.ControlLevels[0][0]} and CourseDepartment=1 ;")
            for i in self.subject1:
                    print(i)
                    subjectLevel1.append(i[0])
            self.HeadLevel.comboBox.addItems(subjectLevel1)
        elif roleID =="Head-Faculty":
            pass
        elif roleID =="admin":
            pass
                

                      
        else: 
            return

    def combochanged(self):
        self.uiControl.comboBox_2.clear()
        output = self.uiControl.comboBox.currentIndex()
        print (output)
        self.conn4= pyodbc.connect(
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                 r'DBQ=E:\project\المشروع\team\instances\Upgrad.accdb;')

        self.z=self.conn4.cursor() 
        self.z.execute(f"SELECT CourseName FROM Course WHERE CourseLevel =? and CourseDepartment=1",output)
        self.Items=self.z.fetchall()
        for n in self.Items:
            self.uiControl.comboBox_2.addItem(n[0])
    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "الازهر"))
        Form.setWindowIcon(QtGui.QIcon("logo.png"))
        self.commandLinkButton.setText(_translate("Form", "تأكيد"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.setWindowIcon(QtGui.QIcon("logo.png"))
    Form.show()
    sys.exit(app.exec_())
