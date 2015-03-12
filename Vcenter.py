# -*- coding: utf8 -*-
__author__ = '54'
import sys,os
sys.path.append('forms')
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from forms.Vcenter_Form import Ui_Vcenter_form
from Host_Class import HostInfo
from Vm_Class import VirtualMachineInfo

class Vcenter(QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent=None)
        self.ui=Ui_Vcenter_form()
        self.ui.setupUi(self)
        self.ui.widget_host.hide()
        self.ui.widget_vm.hide()
        #放置宿主机对象的列表
        self.Host_list=[]



if __name__ == "__main__":
    app=QApplication(sys.argv)
    myapp=Vcenter()
    myapp.show()
    sys.exit(app.exec_())