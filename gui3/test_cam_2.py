import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import cv2

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Tạo label để chứa hình ảnh camera
        self.label = QLabel(self)
        self.label.resize(640, 480)
        self.label.setGeometry(QtCore.QRect(200, 20, 640, 480))
        
        
        self.label_danhsach = QLabel(self)
        self.label_danhsach.setText('Danh Sách camera')
        font_danhsach = QFont()
        font_danhsach.setBold(True)
        font_danhsach.setPointSize(9)
        self.label_danhsach.setFont(font_danhsach)
        self.label_danhsach.setGeometry(QtCore.QRect(20, 14, 201, 31))
        
        self.label_showcam = QLabel(self)
        self.label_showcam.setGeometry(QtCore.QRect(200, 520, 55, 16))
        
        # Tạo button
        # self.button = QPushButton('Quit', self)
        # self.button.clicked.connect(self.close)
        self.btncam1 = QPushButton('Camera 1', self)
        self.btncam1.setGeometry(QtCore.QRect(20, 80, 93, 28))
        self.btncam1.clicked.connect(self.open_cam1)
        self.btncam2 = QPushButton('Camera 2',self)
        self.btncam2.clicked.connect(self.open_cam2)
        self.btncam2.setGeometry(QtCore.QRect(20, 140, 93, 28))
        self.btncam3 = QPushButton('Camera 3', self)
        self.btncam3.clicked.connect(self.open_cam3)
        self.btncam3.setGeometry(QtCore.QRect(20, 200, 93, 28))

    def open_cam1(self):
        # Khởi tạo camera
        self.cap = cv2.VideoCapture(0)
        self.label_showcam.setText('Camera 1')

        # Tạo timer để cập nhật hình ảnh camera
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)
        
    def open_cam2(self):
            # Khởi tạo camera
            self.cap = cv2.VideoCapture(1)
            self.label_showcam.setText('Camera 2')

            # Tạo timer để cập nhật hình ảnh camera
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(1)
            
    def open_cam3(self):
        # Khởi tạo camera
        self.cap = cv2.VideoCapture(2)
        self.label_showcam.setText('Camera 3')

        # Tạo timer để cập nhật hình ảnh camera
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

    def update_frame(self):
        # Lấy khung hình từ camera
        ret, frame = self.cap.read()

        # Nếu không lấy được khung hình, kết thúc
        if not ret:
            return

        # Chuyển đổi khung hình sang dạng QImage
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = image.shape
        bytes_per_line = ch * w
        qimage = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)

        # Hiển thị hình ảnh trên label
        self.label.setPixmap(QPixmap.fromImage(qimage))

    def closeEvent(self, event):
        # Khi đóng chương trình, giải phóng camera
        self.cap.release()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(859, 589)
    window.show()
    sys.exit(app.exec_())