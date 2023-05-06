import sys
import numpy as np
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread,QDateTime
from PyQt5.QtWidgets import QDialog,QApplication,QPushButton,QLabel
from PyQt5.QtGui import QPixmap, QImage
from mainGUI import Ui_Dialog

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import detect
import connect
current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
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

        self.thread = CameraThread()
        self.thread.signal.connect(self.showCamera)
        self.thread.start()

        self.uic.CAPTURE_BTN.clicked.connect(self.capture_frame)
        self.uic.CAPTURE_BTN_2.clicked.connect(self.capture_xemay)
        self.uic.CAPTURE_BTN_3.clicked.connect(self.capture_xedap)

    def capture_xemay(self):
        vehicletype = 1
        self.uic.label_ngaygio.setText(current_time)
        frame = self.thread.get_capture_frame()

        if frame is not None:
            plate = detect.detection_result(frame)
            self.uic.label_biensoxe.setText(plate)
            connect.addTicket(plate, vehicletype)


    def capture_frame(self):
        self.uic.label_ngaygio.setText(current_time)

        #save data to file
        # f = open('test.txt', 'a')
        # f.write(current_time + '\n')
        #Get frame from camera
        frame = self.thread.get_capture_frame()

        #thuat toan cua tac gia tren mang
        if frame is not None:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #frame lay duoc se duoc chuyen sang dang anh co mau
            h, w, ch = img.shape #h la chieu cao, w la chieu rong, ch la color channel
            bytes_per_line = ch * w
            q_img = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Đặt biển số thu được vào ô biển số xe
            plate = detect.detection_result(frame)
            self.uic.label_biensoxe.setText(plate)
            
            #display the capture to prt_sc label
            self.uic.prt_sc.setPixmap(QPixmap.fromImage(q_img)) 


    @pyqtSlot(np.ndarray) #help catch errors at runtime
    def showCamera(self, cv_img):
        img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = img.shape
        bytes_per_line = ch * w
        q_img = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.uic.camera.setPixmap(QPixmap.fromImage(q_img))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
