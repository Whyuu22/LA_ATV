from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets

app = QApplication([])
window2 = QWidget()
window2.setGeometry(440,135,500,500)
window2.setFixedSize(500,500)
window2.setWindowTitle('LA.ATV')
logo = QtGui.QIcon()
logo.addPixmap(QtGui.QPixmap("R:/Foto/Image/quad.png"))
window2.setWindowIcon(logo)
window2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")

def kembali():
    from masuk import window1
    window2.hide()
    window1.show()

def tambah():
    n = input_nama.text()
    w = input_wa.text()
    color = warna1.currentText()
    lama = waktu1.currentText()
    total1 = "Rp100.000"
    total2 = "Rp200.000"
    total3 = "Rp300.000"
    file = open("data.txt", "a")

    if not(len(n)) or not(len(w)):
        msg = QMessageBox()
        msg.setWindowIcon(logo)
        msg.setWindowTitle('Peringatan!')
        msg.setText('Masukkan Biodata Anda')
        msg.exec()
        return

    if lama == "30 Menit":
        baris = tabel.rowCount()
        tabel.insertRow(baris)
        tabel.setItem(baris, 3, QTableWidgetItem(total1))
        file.write(f"{n}={w}={color}={total1}\n")

    if lama == "1 Jam":
        baris = tabel.rowCount()
        tabel.insertRow(baris)
        tabel.setItem(baris, 3, QTableWidgetItem(total2))
        file.write(f"{n}={w}={color}={total2}\n")

    if lama == "1 Jam 30 Menit":
        baris = tabel.rowCount()
        tabel.insertRow(baris)
        tabel.setItem(baris, 3, QTableWidgetItem(total3))
        file.write(f"{n}={w}={color}={total3}\n")

    tabel.setItem(baris, 2, QTableWidgetItem(color))
    tabel.setItem(baris, 0, QTableWidgetItem(n))
    tabel.setItem(baris, 1, QTableWidgetItem(w))

    file.close()

def hapus():
    tabel.removeRow(tabel.rowCount() - 1)
    with open("data.txt") as file:
        line = file.readlines()
        jml = len(line)
        del line[jml-1]
        with open("data.txt", "w") as file:
            for jml in line:
                file.write(jml)

def cetak():
    n = input_nama.text()
    w = input_wa.text()
    color = warna1.currentText()
    lama = waktu1.currentText()

    if not(len(n)) or not(len(w)):
        msg = QMessageBox()
        msg.setWindowIcon(logo)
        msg.setWindowTitle('Peringatan!')
        msg.setText('Masukkan Biodata Anda')
        msg.exec()
        return

    from cetak_data import window3
    window3.show()
    window2.setGeometry(150, 135, 500, 500)

nama = QLabel('Nama : ')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
nama.setFont(font)
ukuran_nama = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
nama.setSizePolicy(ukuran_nama)

input_nama = QLineEdit()
input_nama.setPlaceholderText('Nama')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
font.setBold(True)
input_nama.setFont(font)
ukuran_nama = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
input_nama.setSizePolicy(ukuran_nama)
input_nama.setStyleSheet("QLineEdit\n"
"{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(255, 255, 255);\n"
"\n"
"}")

wa = QLabel('No WhatsApp : ')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
wa.setFont(font)
ukuran_wa = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
wa.setSizePolicy(ukuran_wa)

input_wa = QLineEdit()
input_wa.setPlaceholderText('WhatsApp')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
font.setBold(True)
input_wa.setFont(font)
ukuran_wa = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
input_wa.setSizePolicy(ukuran_wa)
input_wa.setStyleSheet("QLineEdit\n"
"{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(255, 255, 255);\n"
"\n"
"}")

frame_nama = QHBoxLayout()
frame_nama.addWidget(nama)
frame_nama.addWidget(input_nama)

frame_wa = QHBoxLayout()
frame_wa.addWidget(wa)
frame_wa.addWidget(input_wa)

frame11 = QVBoxLayout()
frame11.addLayout(frame_nama)
frame11.addLayout(frame_wa)

waktu = QLabel('Pilih Lama Waktu Penyewaan')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(9)
waktu.setFont(font)
waktu.setAlignment(QtCore.Qt.AlignCenter)
ukuran_waktu = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
waktu.setSizePolicy(ukuran_waktu)

harga = QLabel('RP 100.000 / 30 Menit')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(9)
harga.setFont(font)
harga.setAlignment(QtCore.Qt.AlignCenter)
harga.setSizePolicy(ukuran_waktu)

waktu1 = QComboBox()
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(11)
waktu1.setFont(font)
waktu1.addItems(["30 Menit", "1 Jam", "1 Jam 30 Menit", "2 Jam"])

frame_atas = QVBoxLayout()
frame_atas.addWidget(waktu)
frame_atas.addWidget(harga)

frame_waktu = QVBoxLayout()
frame_waktu.addWidget(waktu1)

frame12 = QVBoxLayout()
frame12.addLayout(frame_atas)
frame12.addLayout(frame_waktu)

warna = QLabel('Pilih Warna ATV')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(9)
warna.setFont(font)
warna.setAlignment(QtCore.Qt.AlignCenter)
ukuran_warna = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
warna.setSizePolicy(ukuran_warna)

warna1 = QComboBox()
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(11)
warna1.setFont(font)
warna1.addItems(["Hitam","Merah","Biru"])

frame_atas1 = QVBoxLayout()
frame_atas1.addWidget(warna)

frame_warna = QVBoxLayout()
frame_warna.addWidget(warna1)

frame13 = QVBoxLayout()
frame13.addLayout(frame_atas1)
frame13.addLayout(frame_warna)

frame1 = QHBoxLayout()
frame1.addLayout(frame11)
frame1.addLayout(frame12)
frame1.addLayout(frame13)

label_output = QLabel('Data Penyewa')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(15)
label_output.setFont(font)
label_output.setAlignment(QtCore.Qt.AlignCenter)

tabel = QTableWidget()
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
tabel.setFont(font)
tabel.setColumnCount(4)
tabel.setRowCount(0)
tabel.setHorizontalHeaderLabels(('Nama','Nomor','Warna','Total Biaya'))
tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
tabel.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);")

frame_label = QVBoxLayout()
frame_label.addWidget(label_output)

btn_kembali = QPushButton('Kembali')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(13)
btn_kembali.setFont(font)
btn_kembali.setStyleSheet("QPushButton\n"
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

btn_tambah = QPushButton('Tambah')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(13)
btn_tambah.setFont(font)
ukuran_tambah = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
btn_tambah.setSizePolicy(ukuran_tambah)
btn_tambah.setStyleSheet("QPushButton\n"
"{\n"
"background-color:black;\n"
"color: white;\n"
"border-radius:2px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:green;\n"
"color:black;\n"
"border-radius:3px;\n"
"}")

btn_hapus = QPushButton('Hapus')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(13)
btn_hapus.setFont(font)
ukuran_hapus = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
btn_hapus.setSizePolicy(ukuran_hapus)
btn_hapus.setStyleSheet("QPushButton\n"
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

btn_selesai = QPushButton('Cetak Data')
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(13)
btn_selesai.setFont(font)
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

frame_btn = QHBoxLayout()
frame_btn.setContentsMargins(80,20,80,10)
frame_btn.addWidget(btn_kembali)
frame_btn.addWidget(btn_selesai)

frame_th = QVBoxLayout()
frame_th.addWidget(btn_tambah)
frame_th.addWidget(btn_hapus)
frame_output = QHBoxLayout()
frame_output.addWidget(tabel)
frame_output.addLayout(frame_th)

frame2 = QVBoxLayout()
frame2.setContentsMargins(0,20,0,0)
frame2.addLayout(frame_label)
frame2.addLayout(frame_output)
frame2.addLayout(frame_btn)

frame = QVBoxLayout()
frame.addLayout(frame1)
frame.addLayout(frame_label)
frame.addLayout(frame2)
window2.setLayout(frame)

btn_kembali.clicked.connect(kembali)
btn_tambah.clicked.connect(tambah)
btn_hapus.clicked.connect(hapus)
btn_selesai.clicked.connect(cetak)