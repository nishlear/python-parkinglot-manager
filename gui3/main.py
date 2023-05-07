import mysql.connector
import numpy as np
import cv2
from datetime import datetime
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread,QDateTime, QCoreApplication, Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.uic import loadUi
from PIL.ImageQt import ImageQt
from mainGUI import Ui_Dialog

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import connect
import detect
import ticketcode
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('gui3/Login_Form.ui', self)
        self.login_btn.clicked.connect(self.loginn)

    def loginn(self):
        un = self.username_line.text()
        pwd = self.pass_line.text()
        data = connect.login(un, pwd)
        if data:
            QMessageBox.information(self, "Login ouput", "Login succsess")
            widget.setFixedWidth(850)
            widget.setCurrentIndex(1)
        else:
            QMessageBox.warning(self, "Login ouput", "Login failure")

class ThanhVien(QMainWindow):
    def __init__(self):
        super(ThanhVien, self).__init__()
        uic.loadUi('gui3/ThanhVien.ui', self)
        # mydb = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="1234",
        #     database="parking"
        # )
        # con = mydb.cursor()
        # con.execute('Select * from member')
        # data = con.fetchall()

        data = connect.showMember()
        self.tableWidget.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i, j, item)
                
        self.Nhan.clicked.connect(self.Them)
        self.pushButton_2.clicked.connect(self.Xoa)
        self.pushButton_5.clicked.connect(self.TimKiem)
        self.tableWidget.cellChanged.connect(self.handle_cell_changed)
        self.pushButton_4.clicked.connect(self.Thoat)
        self.check = 0

    def handle_cell_changed(self, row, column):
        # TODO: change this 
        item = self.tableWidget.item(row, column)
        if self.check == 0:
            column = item.column()
            bd = connect.showMember()
            if item is not None and item.text().strip() != "":
                new_value = item.text()
                if column == 0:
                    for i in range(self.tableWidget.rowCount()):
                        if i != row and self.tableWidget.item(i, 0).text() == new_value:
                            QMessageBox.warning(
                                self, "Lỗi", "ID đã tồn tại, vui lòng nhập ID khác.")
                            item.setText(str(bd[row][0]))
                            return
                if column == 1:
                    try:
                        connect.updateMember(bd[row][0], name=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
                if column == 2:
                    try:
                        connect.updateMember(bd[row][0], plate=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
            else:
                old_value = bd[row][column]
                item.setText(str(old_value))
        
                # if self.check == 0:
                #     column_name = self.tableWidget.horizontalHeaderItem(column).text()
                #     con.execute(f"SELECT {column_name} FROM member")
        #     bd = con.fetchall()
        #     if item is not None and item.text().strip() != "":
        #         new_value = item.text()
        #         if column_name == "ID":
        #             for i in range(self.tableWidget.rowCount()):
        #                 if i != row and self.tableWidget.item(i, 0).text() == new_value:
        #                     QMessageBox.warning(
        #                         self, "Lỗi", "ID đã tồn tại, vui lòng nhập ID khác.")
        #                     item.setText(str(bd[row][0]))
        #                     return
        #         try:
        #             sql = f"UPDATE member SET {column_name} = %s WHERE {column_name} = %s"
        #             val = (new_value, bd[row][0])
        #             con.execute(sql, val)
        #             mydb.commit()
        #         except mysql.connector.Error as error:
        #             QMessageBox.warning(self, "Thông Báo",
        #                                 "Không thể sửa thông tin")
        #             old_value = bd[row][0]
        #             item.setText(str(old_value))
        #     else:
        #         old_value = bd[row][0]
        #         item.setText(str(old_value))

    def Them(self):
        them_dialog = QDialog(self)
        uic.loadUi('gui3/ThemTV.ui', them_dialog)
        result = them_dialog.exec_()
        if result == QDialog.Accepted:
            #   ID = them_dialog.lineEdit_4.text().strip() (ID là AUTO_INCREMENT nên không cần nhập)
            HoTen = them_dialog.lineEdit_2.text().strip()
            Plate = them_dialog.lineEdit_3.text().strip()
            if not HoTen or not Plate:
                QMessageBox.warning(self, "Thông Báo",
                                    "Vui lòng nhập đầy đủ thông tin")
                return
            self.check = 1

    #   con.execute("SELECT * FROM member WHERE plate = %s", (Plate,))
    #   data = con.fetchall()
            data = connect.findMember("plate", Plate)
            if len(data) > 0:
                QMessageBox.warning(self, "Thông Báo",
                                    "ID đã tồn tại, vui lòng chọn ID khác")
                return

            connect.addMember(HoTen, Plate)
    #   sql = "INSERT INTO member (memberID,name,plate) VALUES (%s,%s,%s)"
    #   val = (ID,HoTen,Plate)
    #   con.execute(sql,val)
    #   mydb.commit()
            data = connect.showMember()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.tableWidget.setItem(i, j, item)
    #         currentRowCount = self.tableWidget.rowCount()
    #         self.tableWidget.setRowCount(currentRowCount + 1)
    # #   self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(ID))
    #         self.tableWidget.setItem(
    #             currentRowCount, 1, QTableWidgetItem(HoTen))
    #         self.tableWidget.setItem(
    #             currentRowCount, 2, QTableWidgetItem(Plate))
    #         QMessageBox.information(
    #             self, "Thông Báo", "Thêm thành viên thành công")
            self.check = 0
        else:
            QMessageBox.warning(self, "Thông Báo", "Thêm thành viên thất bại")

    def Xoa(self):
        xoa_dialog = QDialog(self)
        uic.loadUi('gui3/XoaTV.ui', xoa_dialog)
        result = xoa_dialog.exec_()
        if result == QDialog.Accepted:
            ID = xoa_dialog.lineEdit.text().strip()
            # con.execute("SELECT * FROM member WHERE memberID = %s", (ID,))
            # data = con.fetchone()
            data = connect.findMember('memberID', ID)
            if not data:
                QMessageBox.warning(self, "Thông Báo",
                                    "Thông tin không chính xác")
                return
            try:
                #   con.execute("DELETE FROM member WHERE memberID = %s", (ID,))
                #   mydb.commit()
                connect.removeMember(ID)
            except mysql.connector.Error as error:
                QMessageBox.warning(self, "Thông Báo",
                                    "Xóa thành viên thất bại")
                return
            for i in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(i, 0).text() == ID:
                    self.tableWidget.removeRow(i)
                    break
            QMessageBox.information(
                self, "Thông Báo", "Xóa thành viên thành công")

    def Thoat(self):
        widget.setFixedWidth(850)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(1)

    def TimKiem(self):
        ID = self.lineEdit.text().strip()
        self.check = 1
        if input:
            con.execute("SELECT * FROM member WHERE memberID = %s", (ID,))
            data = con.fetchall()
            if data:
                self.tableWidget.setRowCount(0)
                self.tableWidget.setRowCount(len(data))
                for i, row in enumerate(data):
                    for j, col in enumerate(row):
                        item = QTableWidgetItem(str(col))
                        self.tableWidget.setItem(i, j, item)
        else:
            con.execute('Select * from member')
            data = con.fetchall()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.tableWidget.setItem(i, j, item)

            
        self.check = 0

class NhanVien(QMainWindow):
    def __init__(self):
        super(NhanVien, self).__init__()
        uic.loadUi('gui3/NhanVien.ui', self)
        # mydb = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="1234",
        #     database="parking"
        # )
        # con = mydb.cursor()
        # con.execute('Select * from staff')
        # data = con.fetchall()
        data = connect.showStaffwithAccount()
        self.tableWidget.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i, j, item)
        self.Nhan.clicked.connect(self.Them)
        self.pushButton_2.clicked.connect(self.Xoa)
        self.pushButton_5.clicked.connect(self.TimKiem)
        self.tableWidget.cellChanged.connect(self.handle_cell_changed)
        self.pushButton_4.clicked.connect(self.Thoat)
        self.check = 0

    def handle_cell_changed(self, row, column):
        item = self.tableWidget.item(row, column)
        if self.check == 0:
            column = item.column()
            bd = connect.showStaffwithAccount()
            if item is not None and item.text().strip() != "":
                new_value = item.text()
                if column == 0:
                    for i in range(self.tableWidget.rowCount()):
                        if i != row and self.tableWidget.item(i, 0).text() == new_value:
                            QMessageBox.warning(
                                self, "Lỗi", "ID đã tồn tại, vui lòng nhập ID khác.")
                            item.setText(str(bd[row][0]))
                            return
                if column == 1:
                    try:
                        connect.updateStaff(bd[row][0], name=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
                if column == 2:
                    try:
                        connect.updateStaff(bd[row][0], phone=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
                if column == 3:
                    try:
                        connect.updateAccount(bd[row][0], username=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
                if column == 4:
                    try:
                        connect.updateAccount(bd[row][0], password=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
            else:
                old_value = bd[row][column]
                item.setText(str(old_value))
        
        # item = self.tableWidget.item(row, column)
        # if self.check == 0:
        #     column_name = self.tableWidget.horizontalHeaderItem(column).text()
        #     con.execute(f"SELECT {column_name} FROM staff")
        #     bd = con.fetchall()
        #     if item is not None and item.text().strip() != "":
        #         new_value = item.text()
        #         if column_name == "workerID":
        #             for i in range(self.tableWidget.rowCount()):
        #                 if i != row and self.tableWidget.item(i, 0).text() == new_value:
        #                     QMessageBox.warning(
        #                         self, "Lỗi", "ID đã tồn tại, vui lòng nhập ID khác.")
        #                     item.setText(str(bd[row][0]))
        #                     return
        #         try:
        #             sql = f"UPDATE member SET {column_name} = %s WHERE {column_name} = %s"
        #             val = (new_value, bd[row][0])
        #             con.execute(sql, val)
        #             mydb.commit()
        #         except mysql.connector.Error as error:
        #             QMessageBox.warning(self, "Thông Báo",
        #                                 "Không thể sửa thông tin")
        #             old_value = bd[row][0]
        #             item.setText(str(old_value))
        #     else:
        #         old_value = bd[row][0]
        #         item.setText(str(old_value))

    def Them(self):
        them_dialog = QDialog(self)
        uic.loadUi('gui3/ThemNV.ui', them_dialog)
        result = them_dialog.exec_()
        if result == QDialog.Accepted:
            #   ID = them_dialog.lineEdit_10.text().strip()
            HoTen = them_dialog.lineEdit_2.text().strip()
            SDT = them_dialog.lineEdit_3.text().strip()
            # TK = them_dialog.lineEdit_4.text().strip()
            # MK = them_dialog.lineEdit_5.text().strip()
            if not HoTen or not SDT:
                QMessageBox.warning(self, "Thông Báo",
                                    "Vui lòng nhập đầy đủ thông tin")
                return

    #   con.execute("SELECT * FROM staff WHERE staffID = %s", (ID,))
    #   data = con.fetchall()
    # Kiểm tra sử dụng SDT và tên TK
            phonedata = connect.findStaff('phone', SDT)
            if len(phonedata) > 0:
                # QMessageBox.warning(self, "Thông Báo", "ID đã tồn tại, vui lòng chọn ID khác")
                QMessageBox.warning(self, "Thông Báo", "Nhân viên đã tồn tại.")
                return
            self.check = 1

            data = connect.showStaffwithAccount()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.tableWidget.setItem(i, j, item)
        
            try:
                connect.addStaffwithAccount(HoTen, SDT)
            except mysql.connector.Error as error:
                QMessageBox.warning(self, "Thông Báo",
                                    "Không thể thêm khi TK đã trùng lặp")
                self.check = 0
                return
            QMessageBox.information(
                self, "Thông Báo", "Thêm nhân viên thành công")
            self.check = 0
        else:
            QMessageBox.warning(self, "Thông Báo", "Thêm nhân viên thất bại")

    def Xoa(self):
        xoa_dialog = QDialog(self)
        uic.loadUi('gui3/XoaNV.ui', xoa_dialog)
        result = xoa_dialog.exec_()
        if result == QDialog.Accepted:
            ID = xoa_dialog.lineEdit.text().strip()
            # con.execute("SELECT * FROM staff WHERE staffID = %s", (ID,))
            # data = con.fetchone()
            data = connect.findStaff('staffID', ID)
            if not data:
                QMessageBox.warning(self, "Thông Báo",
                                    "Thông tin không chính xác")
                return
            try:
                # con.execute("DELETE FROM staff WHERE staffID = %s", (ID,))
                # mydb.commit()
                connect.removeStaff(ID)
            except mysql.connector.Error as error:
                QMessageBox.warning(self, "Thông Báo",
                                    "Xóa nhân viên thất bại")
                return
            for i in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(i, 0).text() == ID:
                    self.tableWidget.removeRow(i)
                    break
            QMessageBox.information(
                self, "Thông Báo", "Xóa nhân viên thành công")

    def Thoat(self):
        widget.setFixedWidth(850)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(1)

    def TimKiem(self):
        ID = self.lineEdit.text().strip()
        self.check = 1
        if ID:
            con.execute("SELECT * FROM staff WHERE staffID = %s", (ID,))
            data = con.fetchall()
            if data:
                self.tableWidget.setRowCount(0)
                self.tableWidget.setRowCount(len(data))
                for i, row in enumerate(data):
                    for j, col in enumerate(row):
                        item = QTableWidgetItem(str(col))
                        self.tableWidget.setItem(i, j, item)
        else:
            # con.execute('Select * from staff')
            # data = con.fetchall()
            data = connect.showStaffwithAccount()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.tableWidget.setItem(i, j, item)
        self.check = 0

class VeXe(QMainWindow):
    def __init__(self):
        super(VeXe, self).__init__()
        uic.loadUi('gui3/VeXe.ui', self)
        # mydb = mysql.connector.connect(
        #       host="localhost",
        #       user="root",
        #       password="1234",
        #       database="parking"
        # )
        # con = mydb.cursor()
        # con.execute('Select * from ticket')
        # data = con.fetchall()
        data = connect.showTicket()
        self.tableWidget.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i, j, item)
        self.vehicleType = ""
        self.cash = 0
        # self.pushButton_2.clicked.connect(self.Them)
        self.pushButton_4.clicked.connect(self.Xoa)
        self.pushButton.clicked.connect(self.TimKiem)
        self.tableWidget.cellChanged.connect(self.handle_cell_changed)
        self.pushButton_3.clicked.connect(self.Thoat)
        self.check = 0

    def handle_cell_changed(self, row, column):
        item = self.tableWidget.item(row, column)
        if self.check == 0:
            column = item.column()
            bd = connect.showTicket()
            if item is not None and item.text().strip() != "":
                new_value = item.text()
                if column == 0:
                    for i in range(self.tableWidget.rowCount()):
                        if i != row and self.tableWidget.item(i, 0).text() == new_value:
                            QMessageBox.warning(
                                self, "Lỗi", "ID đã tồn tại, vui lòng nhập ID khác.")
                            item.setText(str(bd[row][0]))
                            return
                if column == 1:
                    try:
                        connect.updateTicket(bd[row][0], staffID=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
                if column == 2:
                    try:
                        connect.updateTicket(bd[row][0], memberID=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
                if column == 3:
                    try:
                        connect.updateTicket(bd[row][0], cash=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
                if column == 4:
                    try:
                        connect.updateTicket(bd[row][0], plate=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
                if column == 5:
                    try:
                        connect.updateTicket(bd[row][0], vehicletype=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
                if column == 6:
                    try:
                        connect.updateTicket(bd[row][0], time_in=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
                if column == 7:
                    try:
                        connect.updateMember(bd[row][0], time_out=new_value)
                    except mysql.connector.Error as error:
                        QMessageBox.warning(self, "Thông Báo", "Không thể sửa thông tin")
                        old_value = bd[row][column]
                        item.setText(str(old_value))
            else:
                old_value = bd[row][column]
                item.setText(str(old_value))

        # item = self.tableWidget.item(row, column)
        # if self.check == 0:
        #     column_name = self.tableWidget.horizontalHeaderItem(column).text()
        #     con.execute(f"SELECT {column_name} FROM ticket")
        #     bd = con.fetchall()
        #     if item is not None and item.text().strip() != "":
        #         new_value = item.text()
        #         if column_name == "ID":
        #             for i in range(self.tableWidget.rowCount()):
        #                 if i != row and self.tableWidget.item(i, 0).text() == new_value:
        #                     QMessageBox.warning(
        #                         self, "Lỗi", "ID đã tồn tại, vui lòng nhập ID khác.")
        #                     item.setText(str(bd[row][0]))
        #                     return
        #         try:
        #             sql = f"UPDATE ticket SET {column_name} = %s WHERE {column_name} = %s"
        #             val = (new_value, bd[row][0])
        #             con.execute(sql, val)
        #             mydb.commit()
        #         except mysql.connector.Error as error:
        #             QMessageBox.warning(self, "Thông Báo",
        #                                 "Không thể sửa thông tin")
        #             old_value = bd[row][0]
        #             item.setText(str(old_value))
        #     else:
        #         old_value = bd[row][0]
        #         item.setText(str(old_value))

    # def Them(self):
    #     them_dialog = QDialog(self)
    #     uic.loadUi('gui3/ThemVX.ui', them_dialog)
    #     self.check = 1
    #     vehicleType = ""
    #     cash = 0

    #     def on_radio_button_toggled():
    #         nonlocal vehicleType, cash
    #         if them_dialog.radioButton.isChecked():
    #             vehicleType = them_dialog.radioButton.text()
    #             cash = 3000
    #             them_dialog.label_9.setText(str(cash)+" VNĐ")
    #         elif them_dialog.radioButton_2.isChecked():
    #             vehicleType = them_dialog.radioButton_2.text()
    #             cash = 4000
    #             them_dialog.label_9.setText(str(cash)+" VNĐ")

    #     def on_combobox_activated(index):
    #         item_text = them_dialog.comboBox.itemText(index)
    #         con.execute("SELECT Plate FROM member WHERE ID = %s", (item_text,))
    #         data = con.fetchall()
    #         them_dialog.label_16.setText(str(data[0][0]))
    #     them_dialog.radioButton.toggled.connect(on_radio_button_toggled)
    #     them_dialog.radioButton_2.toggled.connect(on_radio_button_toggled)
    #     con.execute("SELECT memberID FROM member")
    #     data = con.fetchall()
    #     for i in range(0, len(data)):
    #         them_dialog.comboBox.addItem(str(data[i][0]))
    #     them_dialog.comboBox.activated.connect(on_combobox_activated)
    #     result = them_dialog.exec_()
    #     if result == QDialog.Accepted:
    #         datetime_obj = them_dialog.dateTimeEdit.dateTime()
    #         datetime_str = datetime_obj.toString('yyyy-MM-dd hh:mm:ss')
    #         datetime_obj2 = them_dialog.dateTimeEdit_2.dateTime()
    #         datetime_str2 = datetime_obj2.toString('yyyy-MM-dd hh:mm:ss')
    #         ID = them_dialog.lineEdit_2.text().strip()
    #         MaNV = them_dialog.lineEdit_3.text().strip()
    #         Plate = them_dialog.label_16.text()
    #         MaTV = them_dialog.comboBox.currentText()
    #         if not MaTV or not Plate or not ID or not MaNV or (not them_dialog.radioButton.isChecked() and not them_dialog.radioButton_2.isChecked()):
    #             QMessageBox.warning(self, "Thông Báo",
    #                                 "Vui lòng nhập đầy đủ thông tin")
    #             return
    #         try:
    #             #  sql = "INSERT INTO ticket (ticketID, memberID, Plate, vehicleType, staffID,cash,NgayVao,NgayRa) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
    #             sql = "INSERT INTO ticket VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    #             val = (ID, MaNV, MaTV, cash, Plate,
    #                    vehicleType, datetime_str, datetime_str2)
    #             con.execute(sql, val)
    #             # mydb.commit()
    #         except mysql.connector.Error as err:
    #             QMessageBox.warning(self, "Thông Báo", "Không thể thêm")
    #             return
    #         currentRowCount = self.tableWidget.rowCount()
    #         self.tableWidget.setRowCount(currentRowCount + 1)
    #         self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(ID))
    #         self.tableWidget.setItem(
    #             currentRowCount, 1, QTableWidgetItem(MaTV))
    #         self.tableWidget.setItem(
    #             currentRowCount, 2, QTableWidgetItem(Plate))
    #         self.tableWidget.setItem(
    #             currentRowCount, 3, QTableWidgetItem(vehicleType))
    #         self.tableWidget.setItem(
    #             currentRowCount, 4, QTableWidgetItem(MaNV))
    #         self.tableWidget.setItem(
    #             currentRowCount, 5, QTableWidgetItem(str(cash)))
    #         self.tableWidget.setItem(
    #             currentRowCount, 6, QTableWidgetItem(datetime_str))
    #         self.tableWidget.setItem(
    #             currentRowCount, 7, QTableWidgetItem(datetime_str2))
    #         QMessageBox.information(self, "Thông Báo", "Thêm vé xe thành công")
    #     else:
    #         QMessageBox.warning(self, "Thông Báo", "Thêm vé xe thất bại")
    #     self.check = 0

    def Xoa(self):
        xoa_dialog = QDialog(self)
        uic.loadUi('gui3/XoaVX.ui', xoa_dialog)
        result = xoa_dialog.exec_()
        if result == QDialog.Accepted:
            ID = xoa_dialog.lineEdit.text().strip()
            # con.execute("SELECT * FROM ticket WHERE ticketID = %s", (ID,))
            # data = con.fetchone()
            data = connect.findTicket("ticketID", ID)
            if not data:
                QMessageBox.warning(self, "Thông Báo",
                                    "Thông tin không chính xác")
                return
            try:
                # con.execute("DELETE FROM ticket WHERE ticketID = %s", (ID,))
                # mydb.commit()
                connect.removeTicket(ID)
            except mysql.connector.Error as error:
                QMessageBox.warning(self, "Thông Báo", "Xóa vé xe thất bại")
                return
            for i in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(i, 0).text() == ID:
                    self.tableWidget.removeRow(i)
                    break
            QMessageBox.information(self, "Thông Báo", "Xóa vé xe thành công")

    def TimKiem(self):
        ID = self.lineEdit.text().strip()
        self.check = 1
        if ID:
            # con.execute("SELECT * FROM ticket WHERE plate = %s", (ID,))
            # data = con.fetchall()
            data = connect.findTicket("ticketID", ID)
            if data:
                self.tableWidget.setRowCount(0)
                self.tableWidget.setRowCount(len(data))
                for i, row in enumerate(data):
                    for j, col in enumerate(row):
                        item = QTableWidgetItem(str(col))
                        self.tableWidget.setItem(i, j, item)
        else:
            con.execute('Select * from ticket')
            data = con.fetchall()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.tableWidget.setItem(i, j, item)
        self.check = 0

    def Thoat(self):
        widget.setFixedWidth(850)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(1)

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        uic.loadUi('gui3/Menu.ui', self)
        self.pushButton_5.clicked.connect(self.EXIT)
        self.pushButton.clicked.connect(self.EnterDSNNV)
        self.pushButton_3.clicked.connect(self.EnterDSVX)
        self.pushButton_4.clicked.connect(self.EnterDSTV)
        self.pushButton_6.clicked.connect(self.EnterCAM)

    def EXIT(self):
        widget.setFixedWidth(408)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(0)

    def EnterDSNNV(self):
        widget.setFixedWidth(1100)
        widget.setFixedHeight(700)
        widget.setCurrentIndex(2)

    def EnterDSVX(self):
        widget.setFixedWidth(1500)
        widget.setFixedHeight(800)
        widget.setCurrentIndex(3)

    def EnterDSTV(self):
        widget.setFixedWidth(950)
        widget.setFixedHeight(700)
        widget.setCurrentIndex(4)

    def EnterCAM(self):
        widget.setFixedWidth(1021)
        widget.setFixedHeight(771)
        widget.setCurrentIndex(5)

class CameraThread(QThread):
    signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super(CameraThread, self).__init__()
        self.cap = cv2.VideoCapture(0)
        self.capture_frame = None

    def run(self):
        while True:
            ret, cv_img = self.cap.read()
            if ret:
                self.capture_frame = cv_img
                self.signal.emit(cv_img)

    def get_capture_frame(self):
        return self.capture_frame
    
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.uic = Ui_Dialog()
        self.uic.setupUi(self)
        
        self.selected_staff_id = None

        data = connect.showStaff()
        for i, name in enumerate(data):
            self.uic.comboBox.addItem(str(name[1]))

        self.uic.comboBox.currentIndexChanged.connect(self.getStaffName)

        self.thread = CameraThread()
        self.thread.signal.connect(self.showCamera)
        self.thread.start()

        self.uic.CAPTURE_BTN.clicked.connect(self.capture_xehoi)
        self.uic.CAPTURE_BTN_2.clicked.connect(self.capture_xemay)
        self.uic.CAPTURE_BTN_3.clicked.connect(self.capture_xedap)
        self.uic.PASS_BTN.clicked.connect(self.checkout)

        self.pushButton = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.pushButton.clicked.connect(self.EXIT)
        
    def display_qr(self, qr_image):
        qimage = ImageQt(qr_image)
        pixmap = QPixmap.fromImage(QImage(qimage))
        scaled_pixmap = pixmap.scaled(self.uic.prt_sc.size(), aspectRatioMode = Qt.KeepAspectRatio)
        self.uic.prt_sc.setPixmap(scaled_pixmap)

    def checkout(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        frame = self.thread.get_capture_frame()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        plate = ticketcode.scanqrcode(image)
        self.uic.label_biensoxe.setText(plate)
        self.uic.label_ngaygio.setText(current_time)
        connect.saveTicket(plate)

    def getStaffName(self, index):
        name = self.uic.comboBox.itemText(index)
        staffID = connect.findStaff("name", name)[0]
        self.selected_staff_id = staffID

    def EXIT(self):
        widget.setFixedWidth(850)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(1)

    def capture_xehoi(self):
        vehicletype = 2
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.uic.label_ngaygio.setText(current_time)
        QCoreApplication.processEvents()
        frame = self.thread.get_capture_frame()
        plate = str(detect.detection_result(frame))
        self.uic.label_biensoxe.setText(plate)
        connect.addTicket(self.selected_staff_id, plate, vehicletype)

        qr = ticketcode.generate_qrcode(plate)
        self.display_qr(qr)

    def capture_xemay(self):
        vehicletype = 1
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.uic.label_ngaygio.setText(current_time)
        QCoreApplication.processEvents()
        frame = self.thread.get_capture_frame()
        plate = str(detect.detection_result(frame))
        self.uic.label_biensoxe.setText(plate)
        connect.addTicket(self.selected_staff_id, plate, vehicletype)

    def capture_xedap(self):
        vehicletype = 0
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.uic.label_ngaygio.setText(current_time)
        QCoreApplication.processEvents()
        frame = self.thread.get_capture_frame()
        plate = str(detect.detection_result(frame))
        self.uic.label_biensoxe.setText(plate)
        connect.addTicket(self.selected_staff_id, plate, vehicletype)
        # qrcode.generate_qrcode()

    # def capture_frame(self):
    #     # Get the current date and time
    #     current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
    #     self.uic.label_ngaygio.setText(current_time)

    #     #save data to file
    #     f = open('test.txt', 'a')
    #     f.write(current_time + '\n')
    #     #Get frame from camera
    #     frame = self.thread.get_capture_frame()
    #     #thuat toan cua tac gia tren mang
    #     if frame is not None:
    #         img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #frame lay duoc se duoc chuyen sang dang anh co mau
    #         h, w, ch = img.shape #h la chieu cao, w la chieu rong, ch la color channel
    #         bytes_per_line = ch * w
    #         q_img = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888)
    #         #display the capture to prt_sc label
    #         # self.uic.prt_sc.setPixmap(QPixmap.fromImage(q_img))


    @pyqtSlot(np.ndarray) #help catch errors at runtime
    def showCamera(self, cv_img):
        img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = img.shape
        bytes_per_line = ch * w
        q_img = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.uic.camera.setPixmap(QPixmap.fromImage(q_img))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    con = connect.mydb
    Login_f = Login()
    NV_f = NhanVien()
    Menu_f = Menu()
    VeXe_f = VeXe()
    ThanhVien_f = ThanhVien()
    Cam_f = MainWindow()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database='parking'
    )
    con = mydb.cursor()
    widget.addWidget(Login_f)
    widget.setFixedWidth(408)
    widget.setFixedHeight(500)
    widget.addWidget(Menu_f)
    widget.addWidget(NV_f)
    widget.addWidget(VeXe_f)
    widget.addWidget(ThanhVien_f)
    widget.addWidget(Cam_f)
    widget.setCurrentIndex(0)
    widget.show()
    sys.exit(app.exec_())
