# -*- coding: utf8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Thu Dec 25 09:23:08 2014
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(361, 699)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.le_pwd = QtGui.QLineEdit(self.centralwidget)
        self.le_pwd.setGeometry(QtCore.QRect(120, 60, 171, 21))
        self.le_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.le_pwd.setObjectName(_fromUtf8("le_pwd"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 60, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_conn = QtGui.QPushButton(self.centralwidget)
        self.btn_conn.setGeometry(QtCore.QRect(60, 100, 75, 23))
        self.btn_conn.setObjectName(_fromUtf8("btn_conn"))
        self.btn_disconn = QtGui.QPushButton(self.centralwidget)
        self.btn_disconn.setGeometry(QtCore.QRect(230, 100, 75, 23))
        self.btn_disconn.setObjectName(_fromUtf8("btn_disconn"))
        self.le_IPaddr = QtGui.QLineEdit(self.centralwidget)
        self.le_IPaddr.setGeometry(QtCore.QRect(120, 30, 171, 20))
        self.le_IPaddr.setObjectName(_fromUtf8("le_IPaddr"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 51, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tb_sock = QtGui.QTextBrowser(self.centralwidget)
        self.tb_sock.setGeometry(QtCore.QRect(10, 240, 341, 401))
        self.tb_sock.setObjectName(_fromUtf8("tb_sock"))
        self.le_command = QtGui.QLineEdit(self.centralwidget)
        self.le_command.setGeometry(QtCore.QRect(20, 170, 321, 21))
        self.le_command.setObjectName(_fromUtf8("le_command"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 321, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btn_send = QtGui.QPushButton(self.centralwidget)
        self.btn_send.setGeometry(QtCore.QRect(140, 200, 81, 21))
        self.btn_send.setObjectName(_fromUtf8("btn_send"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btn_conn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.btn_conn)
        QtCore.QObject.connect(self.btn_disconn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.btn_disconn)
        QtCore.QObject.connect(self.btn_send, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.btn_send)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "center", None))
        self.label.setText(_translate("MainWindow", "密码:", None))
        self.btn_conn.setText(_translate("MainWindow", "连接", None))
        self.btn_disconn.setText(_translate("MainWindow", "断开", None))
        self.label_2.setText(_translate("MainWindow", "IP地址:", None))
        self.label_3.setText(_translate("MainWindow", "命令框", None))
        self.btn_send.setText(_translate("MainWindow", "发送", None))

