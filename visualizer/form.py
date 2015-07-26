# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.imageView = QtWidgets.QGraphicsView(Form)
        self.imageView.setGeometry(QtCore.QRect(10, 60, 621, 411))
        self.imageView.setObjectName("imageView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.fileEdit.setObjectName("fileEdit")
        self.horizontalLayout.addWidget(self.fileEdit)
        self.fileSelect = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.fileSelect.setObjectName("fileSelect")
        self.horizontalLayout.addWidget(self.fileSelect)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fileSelect.setText(_translate("Form", "file"))
