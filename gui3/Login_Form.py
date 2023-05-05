# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file 'Login_Form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys
import res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        Form.setFont(font)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 411, 511))
        self.widget.setStyleSheet("QPushButton#dangnhap:pressed{\n"
"padding-left:5px;\n"
"pading-top:5px;\n"
"}\n"
"\n"
"\n"
"QPushButton#dangnhap:hover{\n"
"text-decoration: underline;\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 370, 470))
        self.label.setStyleSheet("border-image: url(:/image/gradient.jpg);\n"
"border-radius:25px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(103, 240, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:1.5px solid rgba(255,255,255,111);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.dangnhap = QtWidgets.QPushButton(self.widget)
        self.dangnhap.setEnabled(True)
        self.dangnhap.setGeometry(QtCore.QRect(103, 310, 200, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.dangnhap.setFont(font)
        self.dangnhap.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dangnhap.setMouseTracking(False)
        self.dangnhap.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0284091 rgba(255, 255, 255, 0));\n"
"color: rgba(255,255,255,255);\n"
"border:none;\n"
"")
        self.dangnhap.setObjectName("dangnhap")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(153, 110, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(103, 175, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:1.5px solid rgba(255,255,255,111);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def show_message_box(self):
        QMessageBox.information(self.dangnhap, 'Thông báo', 'Bạn đã nhấn vào Button!')
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", " Mật khẩu"))
        self.dangnhap.setText(_translate("Form", "Đăng nhập"))
        self.label_3.setText(_translate("Form", "ADMIN"))
        self.lineEdit.setPlaceholderText(_translate("Form", " Tên đăng nhập"))
        self.dangnhap.clicked.connect(self.show_message_box)

     
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())

