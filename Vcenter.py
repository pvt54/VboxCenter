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
from socket_processor import Socket_processor
from newhost import Newhost

class Vcenter(QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent=None)
        self.ui=Ui_Vcenter_form()
        self.ui.setupUi(self)
        self.ui.widget_host.hide()
        self.ui.widget_vm.hide()
        #放置宿主机对象的列表
        self.Hostlist=[]
        #-----测试-----
        self.Hostlist.append(HostInfo())
        self.Hostlist[0].Name='127'
        self.Hostlist[0].isOnline=False
        self.Hostlist[0].VMList.append(VirtualMachineInfo())
        self.Hostlist[0].VMList[0].Name='test1'
        self.Hostlist[0].VMList[0].PowerState=1
        #--------------
        self.treeReflash()

    #QTreeWidget数据刷新宿主机对象列表
    def treeReflash(self):
        if self.Hostlist != []:
            for i in self.Hostlist:
                root=QTreeWidgetItem(self.ui.treeWidget)
                root.setText(0,i.Name)
                if i.isOnline:
                    root.setText(1,u'已连接')
                else:
                    root.setText(1,u'未连接')
                if i.VMList != []:
                    for ii in i.VMList:
                        child=QTreeWidgetItem(root)
                        child.setText(0,ii.Name)
                        if ii.PowerState == 1:
                            child.setText(1,u'已停止')
                        elif ii.PowerState == 5:
                            child.setText((1,u'正在运行'))
            #差一个默认选中第一个host项目的功能

    #QTreeWidget的项目选中后操作
    def tree_selected(self):
        item=self.ui.treeWidget.selectedItems()
        print(item[0].text(0)+' is selected !')
        if item[0].parent() is None:
            self.ui.widget_vm.show()
            self.ui.widget_host.hide()
        else:
            self.ui.widget_host.show()
            self.ui.widget_vm.hide()
        return (item[0].text(0),item[0].text(1),item[0].parent() is None)

    #treeWidget右键菜单,自适应右键对象为Host项目与Vm项目
    def treeWidget_contextmenu(self):
        print ('1')
        item_name,item_state,isHost=self.tree_selected()
        popMenu = QMenu()
        if isHost:#如果右键的项目为一个host
            if item_state=='已连接':#判断host状态 (已连接/离线)
                disconn_action=QAction(u'断开', self)
                self.connect(disconn_action,SIGNAL('triggered()'),self.fun1)#信号设置:使用self的connect函数进行设定,信号发送者为对应的QAction对象,信号名称为triggered
                popMenu.addAction(disconn_action)
            else:
                conn_action=QAction(u'连接', self)
                self.connect(conn_action,SIGNAL('triggered()'),self.fun1)
                popMenu.addAction((conn_action))
            new_action=QAction(u'新建虚拟机', self)
            self.connect(new_action,SIGNAL('triggered()'),self.fun1)
            popMenu.addAction(new_action)
            rename_action=QAction(u'重命名', self)
            self.connect(rename_action,SIGNAL('triggered()'),self.fun1)
            popMenu.addAction(rename_action)
            del_action=QAction(u'删除', self)
            self.connect(del_action,SIGNAL('triggered()'),self.fun1)
            popMenu.addAction(del_action)
        else:#如果右键的项目为一个Vm
            if item_name=='已停止':#判断虚拟机状态(通电/断电)
                poweron_action=QAction(u'启动', self)
                self.connect(poweron_action,SIGNAL('triggered()'),self.fun1)
                popMenu.addAction(poweron_action)
            else:
                poweroff_action=QAction(u'停止', self)
                self.connect(poweroff_action,SIGNAL('triggered()'),self.fun1)
                popMenu.addAction((poweroff_action))
            rename_action=QAction(u'重命名', self)
            self.connect(rename_action,SIGNAL('triggered()'),self.fun1)
            popMenu.addAction(rename_action)
            del_action=QAction(u'删除', self)
            self.connect(del_action,SIGNAL('triggered()'),self.fun1)
            popMenu.addAction(del_action)
        popMenu.exec_(QCursor.pos())

    def fun1(self):
        item_name=self.Tree_selected()[0]
        print(str(item_name))

    #连接新的宿主机
    def connecthost(self):
        sp=Socket_processor()
        host=Newhost()
        host.Vcenter_HostList=self.Hostlist
        host.passit(self.hostcallVcenter)
        host.show()
        host.exec_()

    #传递给宿主机对象使用的函数,用于通知vcenter与当前连接的宿主机发生的连接状态改变(如已连接/已断开)
    def hostcallVcenter(self,IPAddr,state):
        for i in self.Hostlist:
            if i.IPAddr==IPAddr:
                if state==1:
                    i.isOnline=True
                else:
                    i.isOnline=False





if __name__ == "__main__":
    app=QApplication(sys.argv)
    myapp=Vcenter()
    myapp.show()
    sys.exit(app.exec_())