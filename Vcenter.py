# -*- coding: utf8 -*-
__author__ = '54'
import sys,os,time
sys.path.append('forms')
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from forms.Vcenter_Form import Ui_Vcenter_form
from vm_setting import setting
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
        # self.Hostlist.append(HostInfo(self))
        # self.Hostlist[0].Name='127'
        # self.Hostlist[0].isOnline=False
        # self.Hostlist[0].VMList.append(VirtualMachineInfo())
        # self.Hostlist[0].VMList[0].Name='test1'
        # self.Hostlist[0].VMList[0].PowerState=1
        #--------------
        self.treeRefrash()

    #QTreeWidget数据刷新宿主机对象列表函数
    def treeRefrash(self):
        #清除现有数据
        ItemCount=self.ui.treeWidget.topLevelItemCount()
        if ItemCount>0:
            for i in range(0,ItemCount):
                # item=self.ui.treeWidget.topLevelItem(i)
                # childlist=item.takeChildren()
                # for childitem in childlist:
                #     del childitem
                self.ui.treeWidget.takeTopLevelItem(i)
                # del item
        #重新添加数据
        if self.Hostlist != []:
            for i in self.Hostlist:
                root=QTreeWidgetItem(self.ui.treeWidget)
                root.setText(0,i.Name)
                if i.isOnline:
                    root.setText(1,u'已连接')
                else:
                    root.setText(1,u'未连接')
                    root.childCount()
                if i.VMList != []:
                    for ii in i.VMList:
                        child=QTreeWidgetItem(root)
                        child.setText(0,ii.Name)
                        if ii.PowerState == '1':
                            child.setText(1,u'停止')
                        elif ii.PowerState == '5':
                            child.setText(1,u'运行中')
        else:
            self.ui.widget_host.hide()
            self.ui.widget_vm.hide()
        if (self.ui.treeWidget.topLevelItemCount())>0:
            (self.ui.treeWidget.topLevelItem(0)).setSelected(True)
            print('setSelected')
            self.tree_selected()
            #默认选中第一个host项目

    #刷新Widght_显示数据函数
    def widgetvmReflash(self,hostname,vmname):
        print('*-*-*-*-*-*-*-*-vm')
        print(vmname,hostname)
        for h in self.Hostlist:
            if h.Name==hostname:
                for vm in h.VMList:
                    if vm.Name==vmname:
                        if vm.PowerState == '1':
                            self.ui.lab_vmpowerstate.setText(u'状态:停止')
                            self.ui.btn_vmpowerstate.setText(u'启动')
                            self.ui.pgbar_vmcpuusage.setValue(0)
                            self.ui.pgbar_vmcpuusage.setEnabled(False)
                            self.ui.pgbar_vmmemusage.setValue(0)
                            self.ui.pgbar_vmmemusage.setEnabled(False)
                        elif vm.PowerState == '5':
                            self.ui.lab_vmpowerstate.setText(u'状态:运行中')
                            self.ui.btn_vmpowerstate.setText(u'停止')
                            self.ui.pgbar_vmcpuusage.setEnabled(True)
                            self.ui.pgbar_vmcpuusage.setValue(int(vm.CPUUsage))
                            self.ui.pgbar_vmmemusage.setEnabled(True)
                            self.ui.pgbar_vmmemusage.setValue(int(vm.MemoryUsage))
                        self.ui.lab_vmname.setText(str(unicode(vm.Name)))
                        self.ui.lab_vmcpucount.setText(str(vm.CPUCount))
                        self.ui.lab_cpuexecutioncap.setText(str(vm.CPUExecutionCap)+u'%')
                        self.ui.lab_vmmemsize.setText(str(vm.MemorySize)+'MB')
                        self.ui.lab_vmosversion.setText(str(vm.OSTypeId))
                        self.ui.tb_vmdescription.append(unicode(vm.Description))
                        self.ui.lab_vmvmemsize.setText(str(vm.VRAMSize)+'MB')
                        self.ui.lab_vmSCname.setText(str((vm.StorageControllers[0])[0]))
                        if (vm.StorageControllers[0])[1] == '2':
                            self.ui.lab_vmSCtype.setText(u'类型:SATA')
                        if vm.MediumAttachment != [] or vm.Medium != []:
                            for ma in vm.MediumAttachment:
                                if ma[0]==(vm.StorageControllers[0])[0]:
                                    if ma[4]=='3':
                                        self.ui.lab_vmdiskname.setText(str(ma[1]))
                                        for m in vm.Medium:
                                            if m[0]==str(self.ui.lab_vmdiskname.text()):
                                                if float(m[3])/1024.0/1024.0/1024.0 > 1:
                                                    self.ui.lab_vmdisksize.setText(str(int(float(m[3])/1024.0/1024.0/1024.0))+'GB')
                                                else:
                                                    self.ui.lab_vmdisksize.setText(u'已使用'+str(int(float(m[3])/1024.0/1024.0))+'MB')
                                    if ma[4]=='2':
                                        if ma[1] != 'None':
                                            self.ui.lab_vmdvdname.setText(str(ma[1]))
                                        else:
                                            self.ui.lab_vmdvdname.setText(u'没有碟片')
                        else:
                            self.ui.lab_vmdiskname.setText(u'没有磁盘')
                            self.ui.lab_vmdisksize.setText('0 MB')
                            self.ui.lab_vmdvdname.setText(u'没有碟片')
                        self.ui.lab_vmNA1name.setText(str((vm.NetworkAdapter[0])[4]))

    #刷新Widght_host显示数据函数
    def widgethostReflash(self,hostname,hoststate):
        print('*-*-*-*-*-*-*-*-*-*-host')
        print(hostname,hoststate)
        for h in self.Hostlist:
            if h.Name==hostname:
                if h.isOnline:
                    self.ui.pgbar_cpuusage.setEnabled(True)
                    self.ui.pgbar_cpuusage.setValue(int(float(h.CPUUsage)))
                    self.ui.pgbar_memusage.setEnabled(True)
                    self.ui.pgbar_memusage.setValue(int(float(h.MemoryAvailable)/float(h.MemorySize)*100))
                    self.ui.pgbar_diskusage.setEnabled(True)
                    self.ui.pgbar_diskusage.setValue(int(float(h.DiskUsage)))
                else:
                    self.ui.pgbar_cpuusage.setEnabled(False)
                    self.ui.pgbar_cpuusage.setValue(0)
                    self.ui.pgbar_memusage.setEnabled(False)
                    self.ui.pgbar_memusage.setValue(0)
                    self.ui.pgbar_diskusage.setEnabled(False)
                    self.ui.pgbar_diskusage.setValue(0)
                self.ui.lab_hostname.setText(str(h.Name))
                self.ui.lab_IPAddr.setText(u'IP:'+str(h.IPAddr))
                self.ui.lab_hostver.setText(u'操作系统 : '+str(h.OSTypeId))
                self.ui.lab_cpucount.setText(str(h.CoreCount)+u'核心'+str(h.CPUCount)+u'线程')
                self.ui.lab_cpuinfo.setText(str(h.CPUInfo))
                self.ui.lab_memsize.setText(str(h.MemorySize))
                if float(h.VboxTotalSize) >(1024*1024):  #文件夹大小过GB
                    self.ui.lab_totalsize.setText(str(int(float(h.VboxTotalSize)/1024.0/1024.0))+u'GB')
                elif float(h.VboxTotalSize) >1024:  #文件夹大小过MB
                    self.ui.lab_totalsize.setText(str(int(float(h.VboxTotalSize)/1024.0))+u'MB')
                else:  #文件夹大小只过KB
                    self.ui.lab_totalsize.setText(str(int(h.VboxTotalSize))+u'KB')



    #QTreeWidget的项目选中后操作
    def tree_selected(self):
        item=self.ui.treeWidget.selectedItems()
        print(item[0].text(0)+' is selected !')
        if item[0].parent() is None:
            self.widgethostReflash(item[0].text(0),item[0].text(1))
            self.ui.widget_host.show()
            self.ui.widget_vm.hide()
            return (item[0].text(0),item[0].text(1),True)
        else:
            self.widgetvmReflash((item[0].parent()).text(0),item[0].text(0))
            self.ui.widget_vm.show()
            self.ui.widget_host.hide()
            return (item[0].text(0),item[0].text(1),(item[0].parent()).text(0))

    def vmpowerstate(self):
        vmname,vmstate,hostname=self.tree_selected()
        if (self.ui.btn_vmpowerstate.text())== u'启动':
           for host in self.Hostlist:
               if host.Name==hostname:
                   if host.isOnline == True:
                       host.socket_processor.vb.machine_poweron(vmname)
                       host.socket_processor.vb.get_guest_performance(vmname,True)
                   else:
                       QMessageBox.question(self, u'提示',u'服务端未连接.')

        else:
            for host in self.Hostlist:
               if host.Name==hostname:
                   if host.isOnline == True:
                       host.socket_processor.vb.machine_poweroff(vmname,True)
                   else:
                       QMessageBox.question(self, u'提示',u'服务端未连接.')



    #treeWidget右键菜单,自适应右键对象为Host项目与Vm项目
    def treeWidget_contextmenu(self):
        print ('1')
        item_name,item_state,isHost=self.tree_selected()
        popMenu = QMenu()
        if isHost is True:#如果右键的项目为一个host
            if item_state==u'已连接':#判断host状态 (已连接/离线)
                disconn_action=QAction(u'断开', self)
                self.connect(disconn_action,SIGNAL('triggered()'),self.disconnect_host)#信号设置:使用self的connect函数进行设定,信号发送者为对应的QAction对象,信号名称为triggered
                popMenu.addAction(disconn_action)
            else:
                conn_action=QAction(u'连接', self)
                self.connect(conn_action,SIGNAL('triggered()'),self.connect_host)
                popMenu.addAction((conn_action))
            new_action=QAction(u'新建虚拟机', self)
            self.connect(new_action,SIGNAL('triggered()'),self.vmsetting)
            popMenu.addAction(new_action)
            rename_action=QAction(u'重命名', self)
            self.connect(rename_action,SIGNAL('triggered()'),self.rename_host)
            popMenu.addAction(rename_action)
            del_action=QAction(u'删除', self)
            self.connect(del_action,SIGNAL('triggered()'),self.delete_host)
            popMenu.addAction(del_action)
        else:#如果右键的项目为一个Vm
            if item_name==u'停止':#判断虚拟机状态(通电/断电)
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
            setting_action=QAction(u'设定',self)
            self.connect(setting_action,SIGNAL('triggered()'),self.vmsetting)
            popMenu.addAction(setting_action)
            del_action=QAction(u'删除', self)
            self.connect(del_action,SIGNAL('triggered()'),self.fun1)
            popMenu.addAction(del_action)
        popMenu.exec_(QCursor.pos())

    def fun1(self):
        item_name=self.Tree_selected()[0]
        print(str(item_name))

    #连接新的宿主机
    def connectnewhost(self):
        newhostForm=Newhost(self)
        #newhostForm.passit(self.hostcallVcenter,self.reportfailure)
        newhostForm.show()
        newhostForm.exec_()

    #断开与一个现有宿主机的连接
    def disconnect_host(self):
        hostname,hoststate,NA=self.tree_selected()
        for h in self.Hostlist:
            if h.Name==hostname:
                h.socket_processor.disconn()

    #连接现有的已断开的一个宿主机
    def connect_host(self):
        hostname,hoststate,NA=self.tree_selected()
        for h in self.Hostlist:
            if h.Name==hostname:
                h.socket_processor.reset()
                h.socket_processor.start()

    #重命名宿主机
    def rename_host(self):
        #需要一个写入新宿主机名称的对话框
        pass

    #删除宿主机
    def delete_host(self):
        hostname,hoststate,NA=self.tree_selected()
        for i in range(0,len(self.Hostlist)):
            if self.Hostlist[i].Name==hostname:
                self.Hostlist[i].socket_processor.disconn()
                del self.Hostlist[i]

        self.treeRefrash()

    #新建虚拟机/设定虚拟机
    def vmsetting(self):
        name,state,isHost=self.tree_selected()
        if isHost is True:
            #新建一个新的虚拟机
            # print('new virtualmachine')
            if state== u'未连接':
                QMessageBox.question(self, u'提示',u'该服务端未连接')
            else:
                for host in self.Hostlist:
                    if host.Name == name:
                        newvm=setting(self,host)
                        newvm.show()
                        newvm.exec_()
        else:
            #打开一个虚拟机的设定窗口
            if state==u'运行中':
                QMessageBox.question(self, u'提示',u'虚拟机正在运行,无法设定.')
            else:
                for host in self.Hostlist:
                    if host.Name == isHost:
                        for vm in host.VMList:
                            if vm.Name == name:
                                vmsetting=setting(self,host,vm)
                                vmsetting.show()
                                vmsetting.exec_()



    #当vbox命令执行失败时,弹出对话框显示出错内容(传递至HostInfo对象中使用)
    def reportfailure(self,failureMSG):
        MSG=''
        for i in failureMSG:
            MSG=MSG+str(i)
        QMessageBox.question(self, u'发生错误',MSG)



    #传递给宿主机对象使用的函数,用于通知vcenter与当前连接的宿主机的连接状态发生改变(如已连接/已断开),或是需要立刻刷新widget面板的请求
    def hostcallVcenter(self,IPAddr='',state='',reflashtree='',reflash=''):
        print('Vcenter.hostcallVcenter')
        print(IPAddr,state,reflashtree,reflash)
        for i in self.Hostlist:
            if i.IPAddr==IPAddr:
                if state==u'\x01':
                    i.isOnline=True
                elif state==u'':
                    i.isOnline=False
                else:
                    pass
        if reflashtree==u'\x01':
            self.treeRefrash()
        if reflash==u'\x01':
            self.tree_selected()








if __name__ == "__main__":
    app=QApplication(sys.argv)
    myapp=Vcenter()
    myapp.show()
    sys.exit(app.exec_())