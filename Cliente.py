import sys, time
import socket
from datetime import *
from threading import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 304)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 341, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 100, 341, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 47, 13))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 140, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(self.tarefa)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.label_2.setText(_translate("MainWindow", "Tarefa:"))
        self.label_3.setText(_translate("MainWindow", "Status:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1"))
        self.pushButton.setText(_translate("MainWindow", "Enviar"))

    def tarefa(self):
        a = str(self.lineEdit.text())
        b = str(self.lineEdit_2.text())
        st = str(self.comboBox.currentText())
        hora = datetime.now()
        c = hora.strftime("%H:%M:%S")  ##%H:%M:%S
        r = "Nome: " + a + "\tTarefa:" + b + "\n" + st + "\nTempo:" + c
        ts(s,r)

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.0.15"
    port = 8000
    s.connect((host, port))

    def ts(str, r):
        s.send(r.encode())
        data = ''
        data = s.recv(1024).decode()
        print (data)

    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())

    app = QtWidgets.QApplication(system.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Principal)
    Principal.show()
    system.exit(app.exec_())
