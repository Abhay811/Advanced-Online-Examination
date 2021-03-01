import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        print("Successfully logged in with email: ", email, "and password:", password)
        updates=CompProfile()
        widget.addWidget(updates)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.back_login.clicked.connect(self.goto_login)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            print("Successfully created acc with email: ", email, "and password: ", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_login(self):
        login=Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


class CompProfile(QDialog):
    def __init__(self):
        super(CompProfile,self).__init__()
        loadUi("profile.ui",self)
        self.saveprofile.clicked.connect(self.createprofilefunction)
        

    def createprofilefunction(self):
        fullname = self.fname.text()
        mob = self.mobile.text()
        designation = self.post.text()
        dep = self.department.text()
        bday = self.birthday.text()
        add = self.address.text()
        print("profile updated with fullname: ", fullname, ", mobile number: ", mob ,", address: ",add, ", bday: ", bday, ", department: ",dep, ", post: ",designation)





app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(800)
widget.show()
app.exec_()