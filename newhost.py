# -*- coding: utf8 -*-
__author__ = '54'
import sys
import re
import time
sys.path.append('forms')
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from forms.newhost_form import Ui_newhost
from socket_processor import Socket_processor

class Newhost(QMainWindow):
     def __init__(self,parent=None):
        QWidget.__init__(self,parent=None)
        self.ui=Ui_newhost()
        self.ui.setupUi(self)
        #新宿主机IP地址和密码
        self.IPAddr=None
        self.Password=None
        self.sp=Socket_processor()
        #通过Vcenter实例化Hewhost对象后将Vcenter的HostList引用过来进行本地的操作
        self.Vcenter_HostList=[]

     #连接按钮对应函数
     def connectHost(self):
         if self.ui.le_hostIPAddr.text()!='' and self.ui.le_hostPWD.text()!='':
            p = re.compile("^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$")
            if p.search(self.ui.le_hostIPAddr.text()):
                self.IPAddr=self.ui.le_hostIPAddr.text()
            else:
                QMessageBox.question(self, u'提示', u'IP地址有误')
            self.sp.set_conn(self.IPAddr,self.Password)
            self.sp.start()
            time.sleep(1)
            if self.sp.loginflag==1:
                self.Vcenter_HostList.append(self.sp)
                self.close()
            elif self.sp.loginflag==-1:
                QMessageBox.question(self, u'提示', u'连接密码错误')
            elif self.sp.loginflag==-2:
                QMessageBox.question(self, u'提示',u'网络连接错误,请重试')
         else:
             QMessageBox.question(self, u'提示', u'IP地址与密码不能为空')

     #用于将vcenter中的hostcallVcenter函数传递给Socket_processor对象
     def passit(self,hostcallVcenter):
        self.sp.callVcenter=hostcallVcenter