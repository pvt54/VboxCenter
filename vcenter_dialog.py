# -*- coding: utf8 -*-
__author__ = '54'
import sys,os
sys.path.append('forms')
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from forms.test import Ui_MainWindow
from socket_processor import Socket_processor

class VCenter_test(QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent=None)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_disconn.setEnabled(False)
        self.ui.btn_send.setEnabled(False)
        self.ui.le_command.setEnabled(False)
        self.isConn_flag=False
        self.ui.le_IPaddr.setText('127.0.0.1')
        self.ui.le_pwd.setText('123')
        self.conn_thread=Socket_processor()
        #定义信号
        self.connect(self,SIGNAL('disconn()'),self.conn_thread.disconn)
        self.connect(self.conn_thread,SIGNAL('set_flag(int)'),self.set_flag)
        self.ui.le_command.setText('GET_HOST_OSVERSION')

    #信号对应处理方法
    def set_flag(self,flag):
        if flag==1: #成功连接信号
            self.isConn_flag==True
            self.ui.btn_conn.setEnabled(False)
            self.ui.le_IPaddr.setEnabled(False)
            self.ui.le_pwd.setEnabled(False)
            self.ui.btn_disconn.setEnabled(True)
            self.ui.btn_send.setEnabled(True)
            self.ui.le_command.setEnabled(True)
        if flag==2: #成功断开信号
            self.isConn_flag==False
            self.ui.btn_conn.setEnabled(True)
            self.ui.le_IPaddr.setEnabled(True)
            self.ui.le_pwd.setEnabled(True)
            self.ui.btn_disconn.setEnabled(False)
            self.ui.btn_send.setEnabled(False)
            self.ui.le_command.setEnabled(False)
        if flag==3: #命令成功执行信号
            #预留为向上发送成功信号
            pass
        if flag==4: #命令执行失败信号
            #预留
            failure=self.conn_thread.failure
            self.conn_thread.failure=None
        if flag==5 : #操作失败信号
            #预留
            pass
    #连接按钮对应方法
    def btn_conn(self):
        self.conn_thread.reset()
        self.conn_thread.set_conn(self.ui.le_IPaddr.text(),self.ui.le_pwd.text(),self.ui)
        self.conn_thread.start()

    #断开按钮对应方法
    def btn_disconn(self):
        self.conn_thread.disconn()

    #发送按钮对应方法
    def btn_send(self):
        if self.ui.le_command.text()!='':
            self.conn_thread.append_command(self.ui.le_command.text())
            self.ui.le_command.setText('')
            print('ispassed')
        else:
            QMessageBox.question(self,u'提示',u'命令不能为空')


if __name__ == "__main__":
    app=QApplication(sys.argv)
    myapp=VCenter_test()
    myapp.show()
    sys.exit(app.exec_())