# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Result(object):
    def setupUi(self, Result):
        Result.setObjectName("Result")
        Result.resize(701, 235)
        self.centralwidget = QtWidgets.QWidget(Result)
        self.centralwidget.setObjectName("centralwidget")
        self.Text = QtWidgets.QLabel(self.centralwidget)
        self.Text.setGeometry(QtCore.QRect(50, 0, 591, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Text.setFont(font)
        self.Text.setAutoFillBackground(False)
        self.Text.setObjectName("Text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 120, 71, 61))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("thank.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.Text.raise_()
        Result.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Result)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 26))
        self.menubar.setObjectName("menubar")
        Result.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Result)
        self.statusbar.setObjectName("statusbar")
        Result.setStatusBar(self.statusbar)

        self.retranslateUi(Result)
        QtCore.QMetaObject.connectSlotsByName(Result)

    def retranslateUi(self, Result):
        _translate = QtCore.QCoreApplication.translate
        Result.setWindowTitle(_translate("Result", "MainWindow"))
        self.Text.setText(_translate("Result", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">The booking is successful</span></p><p align=\"center\"><span style=\" font-size:24pt;\">Enjoy the movie</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Result = QtWidgets.QMainWindow()
    ui = Ui_Result()
    ui.setupUi(Result)
    Result.show()
    sys.exit(app.exec_())
