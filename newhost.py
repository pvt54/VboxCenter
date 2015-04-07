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
from Host_Class import HostInfo

class Newhost(QMainWindow):
     def __init__(self,parent=None):
        QWidget.__init__(self,parent=None)
        self.ui=Ui_newhost()
        self.ui.setupUi(self)
        #新宿主机IP地址和密码
        self.IPAddr=None
        self.Password=None
        self.host=HostInfo()
        #通过Vcenter实例化Hewhost对象后将Vcenter的HostList引用过来进行本地的操作
        self.Vcenter_HostList=[]

     #连接按钮对应函数
     def connectHost(self):
         try:
             if self.ui.le_hostIPAddr.text()!='' and self.ui.le_hostPWD.text()!='':
                p = re.compile("^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$")
                if p.search(self.ui.le_hostIPAddr.text()):
                    self.IPAddr=self.ui.le_hostIPAddr.text()
                    #通过查询IP验证此服务端是否已被连接
                    hostflag=False
                    for i in self.Vcenter_HostList:
                        if i.IPAddr==self.IPAddr:
                            hostflag=True
                    if hostflag:
                        QMessageBox.question(self,u'提示',u'已连接该服务端')
                    else:
                        self.Password=self.ui.le_hostPWD.text()
                        self.host.socket_processor.set_conn(self.IPAddr,self.Password)
                        self.host.socket_processor.start()
                        time.sleep(1)
                        if self.host.socket_processor.loginflag==1:
                            self.Vcenter_HostList.append(self.host)
                            #获取宿主机相关信息
                            self.host.command.get_host_cpu_usage()
                            self.host.command.get_host_cpuinfo()
                            self.host.command.get_host_mem_avail()
                            self.host.command.get_host_memsize()
                            self.host.command.get_host_networkadapters()
                            self.host.command.get_host_storageinfo()
                            self.host.command.get_host_osversion()
                            #宿主机默认名称为IP地址
                            self.host.Name=self.IPAddr
                            self.host.command.get_guest_list()
                            self.close()
                        elif self.host.socket_processor.loginflag==-1:
                            QMessageBox.question(self, u'提示', u'连接密码错误')
                        elif self.host.socket_processor.loginflag==-2:
                            QMessageBox.question(self, u'提示',u'网络连接错误,请重试')
                else:
                    QMessageBox.question(self, u'提示', u'IP地址有误')
             else:
                 QMessageBox.question(self, u'提示', u'IP地址与密码不能为空')
         except BaseException,e:
             self.host.reportfailure('connectHost error:'+str(e))
             print('connectHost error:'+str(e))
     #用于将vcenter中的hostcallVcenter函数传递给Socket_processor对象
     def passit(self,hostcallVcenter,reportfailure):
        self.host.reportfailure=reportfailure
        self.host.hostcallVcenter=hostcallVcenter
        self.host.socket_processor.callVcenter=hostcallVcenter