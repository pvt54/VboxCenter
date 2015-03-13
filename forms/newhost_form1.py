# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newhost_form.ui'
#
# Created: Fri Mar 13 19:11:22 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_newhost(object):
    def setupUi(self, newhost):
        newhost.setObjectName(_fromUtf8("newhost"))
        newhost.resize(316, 191)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(newhost.sizePolicy().hasHeightForWidth())
        newhost.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(newhost)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.le_hostIPAddr = QtGui.QLineEdit(self.centralwidget)
        self.le_hostIPAddr.setGeometry(QtCore.QRect(150, 40, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(11)
        self.le_hostIPAddr.setFont(font)
        self.le_hostIPAddr.setObjectName(_fromUtf8("le_hostIPAddr"))
        self.le_hostPWD = QtGui.QLineEdit(self.centralwidget)
        self.le_hostPWD.setGeometry(QtCore.QRect(150, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(11)
        self.le_hostPWD.setFont(font)
        self.le_hostPWD.setText(_fromUtf8(""))
        self.le_hostPWD.setEchoMode(QtGui.QLineEdit.Password)
        self.le_hostPWD.setObjectName(_fromUtf8("le_hostPWD"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btn_connect = QtGui.QPushButton(self.centralwidget)
        self.btn_connect.setGeometry(QtCore.QRect(60, 130, 71, 31))
        self.btn_connect.setObjectName(_fromUtf8("btn_connect"))
        self.btn_cancel = QtGui.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(180, 130, 71, 31))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        newhost.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(newhost)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        newhost.setStatusBar(self.statusbar)

        self.retranslateUi(newhost)
        QtCore.QObject.connect(self.btn_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), newhost.close)
        QtCore.QMetaObject.connectSlotsByName(newhost)

    def retranslateUi(self, newhost):
        newhost.setWindowTitle(_translate("newhost", "连接新服务端", None))
        self.label.setText(_translate("newhost", "服务端IP地址:", None))
        self.label_2.setText(_translate("newhost", "服务端连接密码:", None))
        self.btn_connect.setText(_translate("newhost", "连接", None))
        self.btn_cancel.setText(_translate("newhost", "取消", None))

