# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(705, 555)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 60, 251, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 271, 41))
        self.label_2.setObjectName("label_2")
        self.lineEditFirstNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirstNumber.setGeometry(QtCore.QRect(350, 70, 251, 20))
        self.lineEditFirstNumber.setObjectName("lineEditFirstNumber")
        self.lineEditSecondNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecondNumber.setGeometry(QtCore.QRect(350, 150, 251, 21))
        self.lineEditSecondNumber.setObjectName("lineEditSecondNumber")
        self.pushButtonPlus = QtWidgets.QPushButton(Dialog)
        self.pushButtonPlus.setGeometry(QtCore.QRect(70, 270, 75, 23))
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.pushButtonSubtract = QtWidgets.QPushButton(Dialog)
        self.pushButtonSubtract.setGeometry(QtCore.QRect(190, 270, 75, 21))
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.pushButtonDivide = QtWidgets.QPushButton(Dialog)
        self.pushButtonDivide.setGeometry(QtCore.QRect(310, 270, 75, 23))
        self.pushButtonDivide.setObjectName("pushButtonDivide")
        self.pushButtonMultiply = QtWidgets.QPushButton(Dialog)
        self.pushButtonMultiply.setGeometry(QtCore.QRect(450, 270, 75, 23))
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(80, 390, 521, 41))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ENTER THE FIRST NUMBER"))
        self.label_2.setText(_translate("Dialog", "ENTER THE SECOND NUMBER"))
        self.pushButtonPlus.setText(_translate("Dialog", "+"))
        self.pushButtonSubtract.setText(_translate("Dialog", "-"))
        self.pushButtonDivide.setText(_translate("Dialog", "/"))
        self.pushButtonMultiply.setText(_translate("Dialog", "*"))
