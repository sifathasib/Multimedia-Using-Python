# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget3.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(784, 482)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 131, 51))
        self.label.setObjectName("label")
        self.lineEditFoodItem = QtWidgets.QLineEdit(Dialog)
        self.lineEditFoodItem.setGeometry(QtCore.QRect(200, 60, 271, 31))
        self.lineEditFoodItem.setObjectName("lineEditFoodItem")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(370, 160, 75, 23))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.listWidgetSelectedItem = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedItem.setGeometry(QtCore.QRect(500, 50, 256, 201))
        self.listWidgetSelectedItem.setObjectName("listWidgetSelectedItem")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your favourite food item"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add"))
