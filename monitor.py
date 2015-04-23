# -*- coding: utf8 -*-
__author__ = '54'
import time
from PyQt4.QtCore import *
class Monitor(QThread):
    def __init__(self,Vcenter,parent=None):
        QThread.__init__(self, parent)#添加QThread初始化方法
        self.Vcenter=Vcenter
        self.connect(self,SIGNAL('vmrefresh(QString,QString)'),self.Vcenter.widgetvmReflash)
        self.connect(self,SIGNAL('hostrefresh(QString,QString)'),self.Vcenter.widgethostReflash)
        self.flag=False
        self.host=None
        self.vm=None

    def stop(self):
        self.flag=False
        self.host=None
        self.vm=None

    def run(self):
        self.flag=True
        while self.flag:
            if self.vm is not None and self.vm.PowerState == '5' and self.host.isOnline:
                self.host.socket_processor.vb.get_guest_performance(self.vm.Name)
                time.sleep(1)
                self.emit(SIGNAL('vmrefresh(QString,QString)'),self.host.Name,self.vm.Name)
            elif self.host.isOnline:
                self.host.socket_processor.vb.get_host_cpu_usage()
                self.host.socket_processor.vb.get_host_mem_avail()
                self.host.socket_processor.vb.get_host_storageinfo()
                time.sleep(1)
                self.emit(SIGNAL('hostrefresh(QString,QString)'),self.host.Name,self.host.Name)