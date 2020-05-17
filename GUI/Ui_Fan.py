# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Fan.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from GUI.Gui import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(567, 538)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 541, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.MainTab = QtWidgets.QWidget()
        self.MainTab.setObjectName("MainTab")
        self.tabWidget.addTab(self.MainTab, "")
        self.searchPageTab = QtWidgets.QWidget()
        self.searchPageTab.setObjectName("searchPageTab")
        self.tabWidget.addTab(self.searchPageTab, "")
        self.searchGameTab = QtWidgets.QWidget()
        self.searchGameTab.setObjectName("searchGameTab")
        self.tabWidget.addTab(self.searchGameTab, "")
        self.complainTab = QtWidgets.QWidget()
        self.complainTab.setObjectName("complainTab")
        self.tabWidget.addTab(self.complainTab, "")
        self.searchHistoryTab = QtWidgets.QWidget()
        self.searchHistoryTab.setObjectName("searchHistoryTab")
        self.tabWidget.addTab(self.searchHistoryTab, "")
        self.editInfoTab = QtWidgets.QWidget()
        self.editInfoTab.setObjectName("editInfoTab")
        self.formLayoutWidget = QtWidgets.QWidget(self.editInfoTab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 251, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.birthDateLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.birthDateLabel.setObjectName("birthDateLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.birthDateLabel)
        self.birthDateDateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.birthDateDateEdit.setObjectName("birthDateDateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.birthDateDateEdit)
        self.label = QtWidgets.QLabel(self.editInfoTab)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 41))
        self.label.setObjectName("label")
        self.saveInfoBtn = QtWidgets.QPushButton(self.editInfoTab)
        self.saveInfoBtn.setGeometry(QtCore.QRect(10, 190, 251, 23))
        self.saveInfoBtn.setObjectName("saveInfoBtn")
        self.tabWidget.addTab(self.editInfoTab, "")
        self.helloFanLabel = QtWidgets.QLabel(Form)
        self.helloFanLabel.setGeometry(QtCore.QRect(190, -20, 151, 61))
        self.helloFanLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.helloFanLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.helloFanLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.helloFanLabel.setObjectName("helloFanLabel")
        self.logoutBtn = QtWidgets.QPushButton(Form)
        self.logoutBtn.setGeometry(QtCore.QRect(414, 500, 131, 23))
        self.logoutBtn.setObjectName("logoutBtn")
        self.logoutBtn.clicked.connect(self.logOut)
        self.helloFanLabel.raise_()
        self.tabWidget.raise_()
        self.logoutBtn.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainTab), _translate("Form", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchPageTab), _translate("Form", "searchPage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchGameTab), _translate("Form", "searchGame"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.complainTab), _translate("Form", "complain"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchHistoryTab), _translate("Form", "searchHistory"))
        self.usernameLabel.setText(_translate("Form", "username:"))
        self.passwordLabel.setText(_translate("Form", "password:"))
        self.nameLabel.setText(_translate("Form", "name:"))
        self.birthDateLabel.setText(_translate("Form", "birth date:"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Edit your personal information</span></p></body></html>"))
        self.saveInfoBtn.setText(_translate("Form", "Save Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editInfoTab), _translate("Form", "editInfo"))
        self.helloFanLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hello Fan</span></p></body></html>"))
        self.logoutBtn.setText(_translate("Form", "Logout"))

    def logOut(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setName(self, name):
        self.helloFanLabel.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hello "+ name +"</span></p></body></html>")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
