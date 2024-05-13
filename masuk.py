from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5 import QtCore

file = open("data.txt","w")
file.write("")
file.close()

app = QApplication([])
window1 = QWidget()
window1.setGeometry(440,135,500,500)
window1.setFixedSize(500,500)
window1.setWindowTitle('LA.ATV')
window1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
logo = QtGui.QIcon()
logo.addPixmap(QtGui.QPixmap("f:\KULIAH\SEMESTER 1 dan 2\Tubes\LA.ATV.png"))
window1.setWindowIcon(logo)

def keluar():
    window1.close()

def masuk():
    from sewa import window2
    window1.hide()
    window2.show()

welcome = QLabel('Welcome to')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(16)
font.setBold(True)
welcome.setFont(font)
welcome.setAlignment(QtCore.Qt.AlignCenter)
ukuran = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
welcome.setSizePolicy(ukuran)

welcome1 = QLabel('LA.ATV')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(20)
font.setBold(True)
welcome1.setFont(font)
welcome1.setAlignment(QtCore.Qt.AlignCenter)
ukuran1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
welcome1.setSizePolicy(ukuran1)

frame1 = QVBoxLayout()
frame1.addWidget(welcome)
frame1.addWidget(welcome1)

btn_masuk = QPushButton(' Masuk ')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(16)
font.setBold(True)
btn_masuk.setFont(font)
ukuran_masuk = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
btn_masuk.setSizePolicy(ukuran_masuk)
btn_masuk.setStyleSheet("QPushButton\n"
"{\n"
"background-color:black;\n"
"color: white;\n"
"border-radius:2px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:cyan;\n"
"color:black;\n"
"border-radius:3px;\n"
"}")

btn_keluar = QPushButton(' Keluar ')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(15)
font.setBold(True)
btn_keluar.setFont(font)
ukuran_keluar = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
btn_keluar.setSizePolicy(ukuran_keluar)
btn_keluar.setStyleSheet("QPushButton\n"
"{\n"
"background-color:black;\n"
"color: white;\n"
"border-radius:2px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:red;\n"
"color:black;\n"
"border-radius:3px;\n"
"}")

frame2 = QVBoxLayout()
frame2.addWidget(btn_masuk)
frame2.addWidget(btn_keluar)

layout = QVBoxLayout()
layout.addLayout(frame1)
layout.addLayout(frame2)
window1.setLayout(layout)

btn_keluar.clicked.connect(keluar)
btn_masuk.clicked.connect(masuk)

window1.show()
app.exec_()