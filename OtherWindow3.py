# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow3.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Seat import Ui_Seat

class Ui_OtherWindow3(object):
    def openseat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Seat()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, OtherWindow3):
        OtherWindow3.setObjectName("OtherWindow3")
        OtherWindow3.resize(712, 296)
        self.centralwidget = QtWidgets.QWidget(OtherWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.S17 = QtWidgets.QPushButton(self.centralwidget)
        self.S17.setGeometry(QtCore.QRect(40, 170, 291, 51))
        self.S17.setObjectName("S17")
        self.S17.clicked.connect(self.openseat)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 120, 151, 41))
        self.label.setObjectName("label")
        self.S19 = QtWidgets.QPushButton(self.centralwidget)
        self.S19.setGeometry(QtCore.QRect(380, 170, 291, 51))
        self.S19.setObjectName("S19")
        self.S19.clicked.connect(self.openseat)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 711, 261))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("soul.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 251, 71))
        self.label_3.setObjectName("label_3")
        self.label_2.raise_()
        self.S17.raise_()
        self.label.raise_()
        self.S19.raise_()
        self.label_3.raise_()
        OtherWindow3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 26))
        self.menubar.setObjectName("menubar")
        OtherWindow3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow3)
        self.statusbar.setObjectName("statusbar")
        OtherWindow3.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow3)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow3)

    def retranslateUi(self, OtherWindow3):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow3.setWindowTitle(_translate("OtherWindow3", "MainWindow"))
        self.S17.setText(_translate("OtherWindow3", "17.30"))
        self.label.setText(_translate("OtherWindow3", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">16/12/2020</span></p></body></html>"))
        self.S19.setText(_translate("OtherWindow3", "19.30"))
        self.label_3.setText(_translate("OtherWindow3", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Soul</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow3 = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow3()
    ui.setupUi(OtherWindow3)
    OtherWindow3.show()
    sys.exit(app.exec_())
