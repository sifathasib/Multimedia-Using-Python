# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(668, 431)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 50, 181, 41))
        self.label.setObjectName("label")
        self.labeltest = QtWidgets.QLabel(Dialog)
        self.labeltest.setGeometry(QtCore.QRect(70, 370, 531, 41))
        self.labeltest.setText("")
        self.labeltest.setObjectName("labeltest")
        self.listWidgetDiagnosis = QtWidgets.QListWidget(Dialog)
        self.listWidgetDiagnosis.setGeometry(QtCore.QRect(290, 70, 256, 192))
        self.listWidgetDiagnosis.setObjectName("listWidgetDiagnosis")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose the diagnosis tests"))
        __sortingEnabled = self.listWidgetDiagnosis.isSortingEnabled()
        self.listWidgetDiagnosis.setSortingEnabled(False)
        item = self.listWidgetDiagnosis.item(0)
        item.setText(_translate("Dialog", "Chest Exray 100$"))
        item = self.listWidgetDiagnosis.item(1)
        item.setText(_translate("Dialog", "Suger lebel Test &3"))
        item = self.listWidgetDiagnosis.item(2)
        item.setText(_translate("Dialog", "Urine analysis $2"))
        item = self.listWidgetDiagnosis.item(3)
        item.setText(_translate("Dialog", "Homoglobin Test $7"))
        item = self.listWidgetDiagnosis.item(4)
        item.setText(_translate("Dialog", "Thyroid Hormone Test $10"))
        self.listWidgetDiagnosis.setSortingEnabled(__sortingEnabled)