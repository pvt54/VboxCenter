# -*- coding: utf8 -*-
__author__ = '54'
import sys,random,win32ui
sys.path.append('forms')
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from forms.setting_form import Ui_setting_form

class setting(QMainWindow):
    def __init__(self,host,vm=None):
        QWidget.__init__(self,parent=None)
        self.host=host
        self.vm=vm
        self.ui=Ui_setting_form()
        self.ui.setupUi(self)
        self.ui.cb_vmOS.addItems([u'Other',
                                 u'Other_64',
                                 u'Windows31',
                                 u'Windows95',
                                 u'Windows98',
                                 u'WindowsMe',
                                 u'WindowsNT4',
                                 u'Windows2000',
                                 u'WindowsXP',
                                 u'WindowsXP_64',
                                 u'Windows2003',
                                 u'Windows2003_64',
                                 u'WindowsVista',
                                 u'WindowsVista_64',
                                 u'Windows2008',
                                 u'Windows2008_64',
                                 u'Windows7',
                                 u'Windows7_64',
                                 u'Windows8',
                                 u'Windows8_64',
                                 u'Windows81',
                                 u'Windows81_64',
                                 u'Windows2012_64',
                                 u'Windows10',
                                 u'Windows10_64',
                                 u'WindowsNT',
                                 u'WindowsNT_64',
                                 u'Linux22',
                                 u'Linux24',
                                 u'Linux24_64',
                                 u'Linux26',
                                 u'Linux26_64',
                                 u'ArchLinux',
                                 u'ArchLinux_64',
                                 u'Debian',
                                 u'Debian_64',
                                 u'OpenSUSE',
                                 u'OpenSUSE_64',
                                 u'Fedora',
                                 u'Fedora_64',
                                 u'Gentoo',
                                 u'Gentoo_64',
                                 u'Mandriva',
                                 u'Mandriva_64',
                                 u'RedHat',
                                 u'RedHat_64',
                                 u'Turbolinux',
                                 u'Turbolinux_64',
                                 u'Ubuntu',
                                 u'Ubuntu_64',
                                 u'Xandros',
                                 u'Xandros_64',
                                 u'Oracle',
                                 u'Oracle_64',
                                 u'Linux',
                                 u'Linux_64',
                                 u'Solaris',
                                 u'Solaris_64',
                                 u'OpenSolaris',
                                 u'OpenSolaris_64',
                                 u'Solaris11_64',
                                 u'FreeBSD',
                                 u'FreeBSD_64',
                                 u'OpenBSD',
                                 u'OpenBSD_64',
                                 u'NetBSD',
                                 u'NetBSD_64',
                                 u'OS2Warp3',
                                 u'OS2Warp4',
                                 u'OS2Warp45',
                                 u'OS2eCS',
                                 u'OS2',
                                 u'MacOS',
                                 u'MacOS_64',
                                 u'MacOS106',
                                 u'MacOS106_64',
                                 u'MacOS107_64',
                                 u'MacOS108_64',
                                 u'MacOS109_64',
                                 u'DOS',
                                 u'Netware',
                                 u'L4',
                                 u'QNX',
                                 u'JRockitVE'])
        self.ui.cb_NAadaptertype.addItems([u'I82540EM',u'Virtio',u'Am79C973',u'I82543GC',u'I82545EM',u'Null'])
        self.ui.cb_NAattachmentType.addItems([u'Bridged'])
        self.ui.cb_NAbridgedinterface.addItems(self.host.HostNetworkAdapter)
        if vm is not None:
            print ('加载一个已有的vm对象')
            self.setWindowTitle('虚拟机设定')
            self.ui.le_vmname=vm.Name
            self.ui.cb_vmOS.setEditable(False)
            self.ui.cb_NAadaptertype.setEditable(False)
            self.ui.cb_NAattachmentType.setEditable(False)
            self.ui.cb_NAbridgedinterface.setEditable(False)
            self.ui.cb_vmOS.setCurrentIndex(self.ui.cb_vmOS.findText(vm.OSTypeId))
            self.ui.sb_cpucount.setValue(int(vm.CPUCount))
            self.ui.sb_cpuexecutioncap.setValue(int(vm.CPUExecutionCap))
            self.ui.sb_vmvmemsize.setValue(int(vm.VRAMSize))
            self.ui.sb_vmmemsize.setMaximum(int(self.host.MemorySize)/10*6)
            self.ui.sb_vmmemsize.setValue(int(self.vm.MemorySize))
            self.ui.tb_description.append(self.vm.Description)\
            #---------------------------加入bootordertable初始化代码--------------------------
            self.table_bootorder_refresh()
            for med in vm.Medium:
                if med[2]=='2':
                    self.ui.lab_vmdiskname.setText(med[0])
                else:
                    self.ui.lab_vmdiskname.setText(u'没有盘片')
            if (vm.NetworkAdapter[0])[1]=='1':
                self.ui.cheakb_NAenabled.setChecked(True)
                self.ui.wg_NA.setEnabled(True)
                self.ui.cb_NAattachmentType.setCurrentIndex(0)
                if (vm.NetworkAdapter[0])[6]=='3':
                    self.ui.cb_NAadaptertype.setCurrentIndex(self.ui.cb_NAadaptertype.findText('I82540EM'))
                elif (vm.NetworkAdapter[0])[6]=='6':
                    self.ui.cb_NAadaptertype.setCurrentIndex(self.ui.cb_NAadaptertype.findText('Virtio'))
                elif (vm.NetworkAdapter[0])[6]=='2':
                    self.ui.cb_NAadaptertype.setCurrentIndex(self.ui.cb_NAadaptertype.findText('Am79C973'))
                elif (vm.NetworkAdapter[0])[6]=='4':
                    self.ui.cb_NAadaptertype.setCurrentIndex(self.ui.cb_NAadaptertype.findText('I82543GC'))
                elif (vm.NetworkAdapter[0])[6]=='5':
                    self.ui.cb_NAadaptertype.setCurrentIndex(self.ui.cb_NAadaptertype.findText('I82545EM'))
                self.ui.cb_NAbridgedinterface.setCurrentIndex(self.ui.cb_NAbridgedinterface.findText((vm.NetworkAdapter[0])[5]))
                self.ui.le_MACaddress.setText((self.vm.NetworkAdapter[0])[2])
                self.ui.cheakb_cableconnected.setChecked(True)
            else:
                self.ui.wg_NA.setEnabled(False)
        else:
            print('新建一个新的虚拟机')
            self.setWindowTitle('新建虚拟机')
            self.ui.cb_vmOS.setEditable(False)
            self.ui.cb_NAadaptertype.setEditable(False)
            self.ui.cb_NAattachmentType.setEditable(False)
            self.ui.cb_NAbridgedinterface.setEditable(False)
            self.ui.sb_cpucount.setValue(1)
            self.ui.sb_cpuexecutioncap.setValue(100)
            self.ui.sb_vmvmemsize.setValue(20)
            self.ui.sb_vmmemsize.setMaximum(int(self.host.MemorySize)/10*6)
            self.ui.sb_vmmemsize.setValue(256)
            #---------------------------加入bootordertable初始化代码--------------------------
            self.table_bootorder_refresh(True)
            self.ui.cheakb_NAenabled.setChecked(True)
            self.ui.wg_NA.setEnabled(True)
            self.ui.cb_NAadaptertype.setCurrentIndex(0)
            self.ui.cb_NAattachmentType.setCurrentIndex(0)
            self.ui.cb_NAbridgedinterface.setCurrentIndex(0)
            self.ui.cheakb_cableconnected.setChecked(True)
            self.MACGenerator()

    #随机生成一个MAC地址并返回
    def MACGenerator(self):
        Mac=''
        for i in range(1,7):
            RANDSTR = "".join(random.sample("0123456789abcdef",2))
            Mac=Mac+RANDSTR
        self.ui.le_MACaddress.setText(Mac)
        return Mac

    #刷新启动项表格,或者初始化数据
    def table_bootorder_refresh(self,New_bootorder=False):
        if New_bootorder:
            for i in range(0,4):
                tableitem=QTableWidgetItem(u'硬盘')
                self.ui.tab_bootorder.setItem(i,0,tableitem)
                tableitem=QTableWidgetItem(u'光驱')
                self.ui.tab_bootorder.setItem(i,0,tableitem)
                tableitem=QTableWidgetItem(u'网络')
                self.ui.tab_bootorder.setItem(i,0,tableitem)
                tableitem=QTableWidgetItem(u'软驱')
                self.ui.tab_bootorder.setItem(i,0,tableitem)
        else:
             for i in range(0,4):
                if self.vm.BootOrder[i] =='1':
                    tableitem=QTableWidgetItem(u'软驱')
                    self.ui.tab_bootorder.setItem(i,0,tableitem)
                if self.vm.BootOrder[i] =='2':
                    tableitem=QTableWidgetItem(u'光驱')
                    self.ui.tab_bootorder.setItem(i,0,tableitem)
                if self.vm.BootOrder[i] =='3':
                    tableitem=QTableWidgetItem(u'硬盘')
                    self.ui.tab_bootorder.setItem(i,0,tableitem)
                if self.vm.BootOrder[i] =='4':
                    tableitem=QTableWidgetItem(u'网络')
                    self.ui.tab_bootorder.setItem(i,0,tableitem)

    #返回目前启动项表格对应的启动项顺序列表(str,长度4位)
    def get_table_bootorder(self):
        bootorder_list=[]
        for i in range(0,4):
            if self.ui.tab_bootorder.item(i,0)=='软驱':
                bootorder_list.append('1')
            if self.ui.tab_bootorder.item(i,0)=='光驱':
                bootorder_list.append('2')
            if self.ui.tab_bootorder.item(i,0)=='硬盘':
                bootorder_list.append('3')
            if self.ui.tab_bootorder.item(i,0)=='网络':
                bootorder_list.append('4')
        return bootorder_list

    #上移启动项按钮对应函数
    def bootorder_up(self):
        print ('start_up')
        if len(self.ui.tab_bootorder.selectedItems()) != 0 and (self.ui.tab_bootorder.currentRow()) is not 0:
            current_row=self.ui.tab_bootorder.currentRow()
            current_item=QTableWidgetItem((self.ui.tableWidget.item(current_row,0)).text())
            up_item=QTableWidgetItem((self.ui.tableWidget.item(current_row-1,0)).text())
            self.ui.tab_bootorder.takeItem(current_row,0)
            self.ui.tab_bootorder.takeItem(current_row-1,0)
            self.ui.tab_bootorder.setItem(current_row-1,0,current_item)
            self.ui.tab_bootorder.setItem(current_row,0,up_item)
            #self.ui.tableWidget.setFocusPolicy(Qt.NoFocus)
            (self.ui.tab_bootorder.selectedItems())[0].setSelected(False)
            (self.ui.tab_bootorder.item(current_row-1,0)).isSelected()
        else:
            pass
        print ('end_up')

    #下移启动项按钮对应函数
    def bootorder_down(self):
        print ('start_down')
        if len(self.ui.tab_bootorder.selectedItems()) != 0 and (self.ui.tab_bootorder.currentRow()) is not 3:
            current_row=self.ui.tab_bootorder.currentRow()
            current_item=QTableWidgetItem((self.ui.tab_bootorder.item(current_row,0)).text())
            down_item=QTableWidgetItem((self.ui.tab_bootorder.item(current_row+1,0)).text())
            self.ui.tab_bootorder.takeItem(current_row,0)
            self.ui.tab_bootorder.takeItem(current_row+1,0)
            self.ui.tab_bootorder.setItem(current_row,0,down_item)
            self.ui.tab_bootorder.setItem(current_row+1,0,current_item)
            #self.ui.tableWidget.setFocusPolicy(Qt.NoFocus)
            (self.ui.tab_bootorder.selectedItems())[0].setSelected(False)
            (self.ui.tab_bootorder.item(current_row+1,0)).isSelected()
        else:
            pass
        print ('end_down')

    #根据启用网络适配器的checkbox情况来判断网络适配器设置面板是否启用
    def setNAwidgetEnabled(self):
        if self.ui.cheakb_NAenabled.isChecked():
            self.ui.wg_NA.setEnabled(True)
        else:
            self.ui.wg_NA.setEnabled(False)

    #打开文件选择对话框函数
    def openFileselectDialog(self):
        fileName = QFileDialog.getOpenFileName(self,self.tr('Open Image'),self.tr('ISO Files(*.ISO)'))
        print(fileName)
        self.ISOpath=fileName
