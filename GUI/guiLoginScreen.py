# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiLoginScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 514)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginLabel = QtWidgets.QLabel(self.centralwidget)
        self.loginLabel.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.loginLabel.setScaledContents(False)
        self.loginLabel.setWordWrap(False)

        # login label form and btn
        self.loginLabel.setObjectName("loginLabel")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 151, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.loginForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.loginForm.setContentsMargins(0, 0, 0, 0)
        self.loginForm.setObjectName("loginForm")
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.loginForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.loginForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.loginForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.loginForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(10, 90, 151, 23))
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.clicked.connect(lambda: self.click())

        # sign-in as guest btn
        self.guestBtn = QtWidgets.QPushButton(self.centralwidget)
        self.guestBtn.setGeometry(QtCore.QRect(370, 460, 131, 23))
        self.guestBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.guestBtn.setObjectName("guestBtn")

        # register label form and btn
        self.registerLabel = QtWidgets.QLabel(self.centralwidget)
        self.registerLabel.setGeometry(QtCore.QRect(310, 10, 91, 31))
        self.registerLabel.setObjectName("registerLabel")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(310, 40, 161, 101))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.registerForm = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.registerForm.setContentsMargins(0, 0, 0, 0)
        self.registerForm.setObjectName("registerForm")
        self.usernameLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.usernameLabel_2.setObjectName("usernameLabel_2")
        self.registerForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel_2)
        self.usernameLineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.usernameLineEdit_2.setObjectName("usernameLineEdit_2")
        self.registerForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit_2)
        self.passwordLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.passwordLabel_2.setObjectName("passwordLabel_2")
        self.registerForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel_2)
        self.passwordLineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.passwordLineEdit_2.setObjectName("passwordLineEdit_2")
        self.registerForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit_2)
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.nameLabel.setObjectName("nameLabel")
        self.registerForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.registerForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.birthDateLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.birthDateLabel.setObjectName("birthDateLabel")
        self.registerForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.birthDateLabel)
        self.birthDateLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.birthDateLineEdit.setObjectName("birthDateLineEdit")
        self.registerForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.birthDateLineEdit)
        self.registerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.registerBtn.setGeometry(QtCore.QRect(310, 150, 161, 23))
        self.registerBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerBtn.setObjectName("registerBtn")

        # window styling
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(240, 0, 20, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(7, 290, 501, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 511, 491))
        self.backgroundLabel.setText("")
        self.backgroundLabel.setPixmap(QtGui.QPixmap("football federation.png"))
        self.backgroundLabel.setScaledContents(True)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.backgroundLabel.raise_()
        self.loginLabel.raise_()
        self.formLayoutWidget.raise_()
        self.loginBtn.raise_()
        self.guestBtn.raise_()
        self.registerLabel.raise_()
        self.formLayoutWidget_2.raise_()
        self.registerBtn.raise_()
        self.line.raise_()
        self.line_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Login</span></p></body></html>"))
        self.usernameLabel.setText(_translate("MainWindow", "username"))
        self.passwordLabel.setText(_translate("MainWindow", "password"))
        self.loginBtn.setText(_translate("MainWindow", "Login"))
        self.guestBtn.setText(_translate("MainWindow", "SignIn as a guest"))
        self.registerLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Register</span></p></body></html>"))
        self.usernameLabel_2.setText(_translate("MainWindow", "username"))
        self.passwordLabel_2.setText(_translate("MainWindow", "password"))
        self.nameLabel.setText(_translate("MainWindow", "name"))
        self.birthDateLabel.setText(_translate("MainWindow", "birth date"))
        self.registerBtn.setText(_translate("MainWindow", "Register"))

    def click(self):
        print('click')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
