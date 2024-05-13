from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5 import QtCore

app = QApplication([])
window3 = QWidget()
window3.setGeometry(720,135,500,500)
window3.setFixedSize(500,500)
window3.setWindowTitle('LA.ATV')
window3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
logo = QtGui.QIcon()
logo.addPixmap(QtGui.QPixmap("R:/Foto/Image/quad.png"))
window3.setWindowIcon(logo)

def cetak():
    data = input_data.text()

    if not len(data):
        msg = QMessageBox()
        msg.setWindowIcon(logo)
        msg.setWindowTitle('Peringatan!')
        msg.setText('Masukkan Data Yang Benar')
        msg.setStyleSheet("color: rgb(255, 255, 255);\n"
                          "background-color: rgb(0, 0, 0);")
        msg.exec()
        return

    data = int(data)
    file = open("data.txt", "r")
    read = file.readlines()
    x = read[data - 1]
    list = x.split('=')
    nama = list[0]
    wa = list[1]
    warna = list[2]
    total = list[3]

    h = QMessageBox()
    h.setWindowIcon(logo)
    h.setStyleSheet("color: rgb(255, 255, 255);\n"
                      "background-color: rgb(0, 0, 0);")
    h.setWindowTitle('Data Penyewaan')
    h.setText(f"Nama : {nama}\nNo WhatsApp : {wa}\nWarna ATV : {warna}\nTotal Biaya : {total}")
    font = QtGui.QFont()
    font.setFamily("Times New Roman")
    font.setPointSize(20)
    font.setBold(True)
    h.setFont(font)
    h.exec()

def clear():
    input_data.clear()

def selesai():
    file = open("data.txt", "w")
    file.write("")
    file.close()
    window3.close()
    window3.close()

biodata = QLabel('Masukkan Data Ke Berapa\nYang Ingin Dicetak')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(20)
font.setBold(True)
biodata.setFont(font)
biodata.setAlignment(QtCore.Qt.AlignCenter)
ukuran1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
biodata.setSizePolicy(ukuran1)

frame1 = QVBoxLayout()
frame1.addWidget(biodata)

input_data = QLineEdit()
input_data.setPlaceholderText(' Data Baris ke')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(14)
font.setBold(True)
input_data.setFont(font)
ukuran_data = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
input_data.setSizePolicy(ukuran_data)
input_data.setStyleSheet("QLineEdit\n"
"{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(255, 255, 255);\n"
"\n"
"}")

frame2 = QVBoxLayout()
frame2.addWidget(input_data)
frame2.setSpacing(10)

btn_clear = QPushButton(' Clear ')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(13)
font.setBold(True)
btn_clear.setFont(font)
ukuran_clear = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
btn_clear.setSizePolicy(ukuran_clear)
btn_clear.setStyleSheet("QPushButton\n"
"{\n"
"background-color:black;\n"
"color: white;\n"
"border-radius:2px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:white;\n"
"color:black;\n"
"border-radius:3px;\n"
"}")

btn_cetak = QPushButton(' Cetak ')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(13)
font.setBold(True)
btn_cetak.setFont(font)
ukuran_cetak = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
btn_cetak.setSizePolicy(ukuran_cetak)
btn_cetak.setStyleSheet("QPushButton\n"
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

btn_selesai = QPushButton(' Selesai ')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(13)
font.setBold(True)
btn_selesai.setFont(font)
ukuran_selesai = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
btn_selesai.setSizePolicy(ukuran_selesai)
btn_selesai.setStyleSheet("QPushButton\n"
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

frame3 = QHBoxLayout()
frame3.setContentsMargins(50,20,50,10)
frame2.addWidget(btn_clear)
frame3.addWidget(btn_cetak)
frame3.addWidget(btn_selesai)

frame3.setSpacing(3)
layout = QVBoxLayout()
layout.addLayout(frame1)
layout.addLayout(frame2)
layout.addLayout(frame3)
window3.setLayout(layout)

btn_clear.clicked.connect(clear)
btn_cetak.clicked.connect(cetak)
btn_selesai.clicked.connect(selesai)