# -*- coding: utf8 -*-
__author__ = '54'
import sys,random,os
from ftplib import FTP
sys.path.append('forms')
reload(sys)
sys.setdefaultencoding('utf8')
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from forms.setting_form import Ui_setting_form

class setting(QMainWindow):
    def __init__(self,Vcenter,host,vm=None):
        QWidget.__init__(self,parent=Vcenter)
        self.Vcenter=Vcenter
        self.host=host
        self.vm=vm
        self.ui=Ui_setting_form()
        self.ui.setupUi(self)
        self.ISOpath=None
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
            self.setWindowTitle(u'虚拟机设定')
            self.ui.le_vmname.setText(vm.Name)
            self.ui.cb_vmOS.setEditable(False)
            self.ui.cb_NAadaptertype.setEditable(False)
            self.ui.cb_NAattachmentType.setEditable(False)
            self.ui.cb_NAbridgedinterface.setEditable(False)
            self.ui.cb_vmOS.setCurrentIndex(self.ui.cb_vmOS.findText(vm.OSTypeId))
            self.ui.sb_cpucount.setValue(int(vm.CPUCount))
            self.ui.sb_cpuexecutioncap.setValue(int(vm.CPUExecutionCap))
            self.ui.sb_vmvmemsize.setMaximum(64)
            self.ui.sb_vmvmemsize.setValue(int(vm.VRAMSize))
            self.ui.sb_vmmemsize.setMaximum(int(self.host.MemorySize)/10*6)
            self.ui.sb_vmmemsize.setValue(int(self.vm.MemorySize))
            self.ui.te.appendPlainText(self.vm.Description)
            #---------------------------加入bootordertable初始化代码--------------------------
            self.table_bootorder_refresh()
            self.ui.lab_vmdiskname.setText(u'没有盘片')
            for med in vm.Medium:
                if med[2]=='2':
                    self.ui.lab_vmdiskname.setText(med[0])
                else:
                    self.ui.lab_vmdiskname.setText(u'没有盘片')
                if med[2]=='3':
                    self.ui.le_vdiname.setText(med[0])
                    self.ui.le_vdiname.setEnabled(False)
                    self.ui.sb_vdisize.setValue(int(float(med[4])/1000/1000))
                    self.ui.sb_vdisize.setEnabled(False)
                else:
                    self.ui.le_vdiname.setText(u'')
                    self.ui.le_vdiname.setEnabled(False)
                    self.ui.sb_vdisize.setValue(0)
                    self.ui.sb_vdisize.setEnabled(False)
            if (vm.NetworkAdapter[0])[1]=='1':
                self.ui.cheakb_NAenabled.setChecked(True)
                self.ui.wg_NA.setEnabled(True)
                self.ui.cb_NAattachmentType.setCurrentIndex(0)
                if (vm.NetworkAdapter[0])[5]=='3':
                    self.ui.cb_NAadaptertype.setCurrentIndex(self.ui.cb_NAadaptertype.findText('I82540EM'))
                elif (vm.NetworkAdapter[0])[5]=='6':
                    self.ui.cb_NAadaptertype.setCurrentIndex(self.ui.cb_NAadaptertype.findText('Virtio'))
                elif (vm.NetworkAdapter[0])[5]=='2':
                    self.ui.cb_NAadaptertype.setCurrentIndex(self.ui.cb_NAadaptertype.findText('Am79C973'))
                elif (vm.NetworkAdapter[0])[5]=='4':
                    self.ui.cb_NAadaptertype.setCurrentIndex(self.ui.cb_NAadaptertype.findText('I82543GC'))
                elif (vm.NetworkAdapter[0])[5]=='5':
                    self.ui.cb_NAadaptertype.setCurrentIndex(self.ui.cb_NAadaptertype.findText('I82545EM'))
                self.ui.cb_NAbridgedinterface.setCurrentIndex(self.ui.cb_NAbridgedinterface.findText((vm.NetworkAdapter[0])[4]))
                self.ui.le_MACaddress.setText((self.vm.NetworkAdapter[0])[2])
                self.ui.cheakb_cableconnected.setChecked(True)
            else:
                self.ui.wg_NA.setEnabled(False)
        else:
            print('新建一个新的虚拟机')
            self.setWindowTitle(u'新建虚拟机')
            self.ui.cb_vmOS.setEditable(False)
            self.ui.cb_NAadaptertype.setEditable(False)
            self.ui.cb_NAattachmentType.setEditable(False)
            self.ui.cb_NAbridgedinterface.setEditable(False)
            self.ui.sb_cpucount.setValue(1)
            self.ui.sb_cpuexecutioncap.setValue(100)
            self.ui.sb_vmvmemsize.setValue(20)
            self.ui.sb_vmvmemsize.setMaximum(64)
            self.ui.sb_vmmemsize.setMaximum(int(self.host.MemorySize)/10*6)
            self.ui.sb_vmmemsize.setValue(256)
            #---------------------------加入bootordertable初始化代码--------------------------
            self.table_bootorder_refresh(True)
            self.ui.lab_vmdiskname.setText(u'没有盘片')
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
        if New_bootorder is True:
            print('new_bootorder start')
            tableitem=QTableWidgetItem(u'硬盘')
            self.ui.tab_bootorder.setItem(0,0,tableitem)
            tableitem=QTableWidgetItem(u'光驱')
            self.ui.tab_bootorder.setItem(1,0,tableitem)
            tableitem=QTableWidgetItem(u'网络')
            self.ui.tab_bootorder.setItem(2,0,tableitem)
            tableitem=QTableWidgetItem(u'软驱')
            self.ui.tab_bootorder.setItem(3,0,tableitem)
            print('new_bootorder end')
        else:
            print('self.vm.BootOrder')
            print(self.vm.BootOrder)
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
            if (self.ui.tab_bootorder.item(i,0).text())==u'软驱':
                bootorder_list.append('1')
            if (self.ui.tab_bootorder.item(i,0).text())==u'光驱':
                bootorder_list.append('2')
            if (self.ui.tab_bootorder.item(i,0).text())==u'硬盘':
                bootorder_list.append('3')
            if (self.ui.tab_bootorder.item(i,0).text())==u'网络':
                bootorder_list.append('4')
        return bootorder_list

    #上移启动项按钮对应函数
    def bootorder_up(self):
        print ('start_up')
        if len(self.ui.tab_bootorder.selectedItems()) != 0 and (self.ui.tab_bootorder.currentRow()) is not 0:
            current_row=self.ui.tab_bootorder.currentRow()
            current_item=QTableWidgetItem((self.ui.tab_bootorder.item(current_row,0)).text())
            up_item=QTableWidgetItem((self.ui.tab_bootorder.item(current_row-1,0)).text())
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
        fileName = QFileDialog.getOpenFileName(self,self.tr('Open Image'),'c:',self.tr('ISO Files(*.ISO)'))
        print(fileName)
        fileName=unicode(fileName)
        self.ISOpath=fileName
        self.ui.lab_vmdiskname.setText(os.path.basename(fileName))

    def ftp_upload(self):
        ftp=FTP()
        ftp.set_debuglevel(2)#打开调试级别2，显示详细信息;0为关闭调试信息
        ftp.connect(str(self.host.IPAddr),'54221')#连接
        ftp.login('','')#登录，如果匿名登录则用空串代替即可
        #print ftp.getwelcome()#显示ftp服务器欢迎信息
        #ftp.cwd('xxx/xxx/') #选择操作目录
        bufsize = 1024#设置缓冲块大小
        file_handler = open(self.ISOpath,'rb')#以读模式在本地打开文件
        ftp.storbinary('STOR %s' % os.path.basename(self.ISOpath),file_handler,bufsize)#上传文件
        ftp.set_debuglevel(0)
        file_handler.close()
        ftp.quit()
        print "ftp up OK"

    #确认按钮对应函数
    def confirm(self):
        if self.vm is not None: #进行虚拟机设定的校验提交
            #校验部分,非空检查
            if (self.ui.le_vmname.text()) =='':
                QMessageBox.question(self, u'提示',u'请输入虚拟机名称')
            elif (self.ui.le_MACaddress.text()) =='':
                QMessageBox.question(self, u'提示',u'请输入MAC地址')
            else:
                    #逐个判断控件的值是否发生变化,如果有,这调用对应的值得提交修改函数
                if str(self.ui.cb_vmOS.currentText()) != self.vm.OSTypeId:
                    self.host.socket_processor.vb.set_guest_osversion(self.vm.Name,self.ui.cb_vmOS.currentText(),True)
                if str(self.ui.sb_cpucount.value()) != self.vm.CPUCount:
                    self.host.socket_processor.vb.set_guest_cpucount(self.vm.Name,self.ui.sb_cpucount.value(),True)
                if str(self.ui.sb_cpuexecutioncap.value()) != self.vm.CPUExecutionCap:
                    self.host.socket_processor.vb.set_guest_cpuexecutioncap(self.vm.Name,self.ui.sb_cpuexecutioncap.value(),True)
                if str(self.ui.sb_vmvmemsize.value()) != self.vm.VRAMSize:
                    self.host.socket_processor.vb.set_guest_vramsize(self.vm.Name,self.ui.sb_vmvmemsize.value(),True)
                if str(self.ui.sb_vmmemsize.value()) != self.vm.MemorySize:
                    self.host.socket_processor.vb.set_guest_memsize(self.vm.Name,self.ui.sb_vmmemsize.value(),True)
                if str(self.ui.te.toPlainText()) != self.vm.Description:
                    self.host.socket_processor.vb.set_guest_description(self.vm.Name,self.ui.te.toPlainText(),True)
                if (self.get_table_bootorder()) != self.vm.BootOrder:
                    bootorder=self.get_table_bootorder()
                    self.host.socket_processor.vb.set_guest_bootorder(self.vm.Name,bootorder[0],bootorder[1],bootorder[2],bootorder[3],True)
                if self.ISOpath is not None:
                    self.host.socket_processor.vb.ftp_on()
                    self.ftp_upload()
                    self.host.socket_processor.vb.ftp_off()
                    for ma in self.vm.MediumAttachment:
                        if ma[4]=='2':
                            self.host.socket_processor.vb.add_guest_mediums_dvd(self.vm.Name,ma[0],ma[2],os.path.basename(self.ISOpath),True)
                if self.ui.cheakb_NAenabled.isChecked():
                    adapterType=None
                    if (self.ui.cb_NAadaptertype.currentText()) == 'I82540EM':
                        adapterType='3'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'Virtio':
                        adapterType='6'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'Am79C973':
                        adapterType='2'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'I82543GC':
                        adapterType='4'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'I82545EM':
                        adapterType='5'
                    if (self.ui.cb_NAbridgedinterface.currentText()) != (self.vm.NetworkAdapter[0])[4] or adapterType!=(self.vm.NetworkAdapter[0])[5] or (self.ui.le_MACaddress.text())!=(self.vm.NetworkAdapter[0])[2] or str(int(self.ui.cheakb_cableconnected.isChecked()))!=(self.vm.NetworkAdapter[0])[6]:
                        self.host.socket_processor.vb.set_guest_networkadapters(self.vm.Name,'0','1',self.ui.le_MACaddress.text(),'2',self.ui.cb_NAbridgedinterface.currentText(),adapterType,str(int(self.ui.cheakb_cableconnected.isChecked())))
                else:
                    adapterType=None
                    if (self.ui.cb_NAadaptertype.currentText()) == 'I82540EM':
                        adapterType='3'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'Virtio':
                        adapterType='6'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'Am79C973':
                        adapterType='2'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'I82543GC':
                        adapterType='4'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'I82545EM':
                        adapterType='5'
                    self.host.socket_processor.vb.set_guest_networkadapters(self.vm.Name,'0','0',self.ui.le_MACaddress.text(),'2',self.ui.cb_NAbridgedinterface.currentText(),adapterType,str(int(self.ui.cheakb_cableconnected)))
                if(self.ui.le_vmname.text()) != self.vm.Name:
                    self.host.socket_processor.vb.set_guest_name(self.vm.Name,self.ui.le_vmname.text(),True)
                self.close()
        #---------------------------------------进行虚拟机设定的校验提交结束-------------------------------------
        else:
        #进行新建虚拟机的校验提交
        #校验部分,非空检查
            if (self.ui.le_vmname.text()) =='':
                QMessageBox.question(self, u'提示',u'请输入虚拟机名称')
            elif (self.ui.le_MACaddress.text()) =='':
                QMessageBox.question(self, u'提示',u'请输入MAC地址')
            elif (self.ui.le_vdiname.text()) =='':
                QMessageBox.question(self, u'提示',u'请输入虚拟磁盘名称')
            else:
                self.host.socket_processor.vb.create_new_machine(self.ui.le_vmname.text(),self.ui.te.toPlainText(),self.ui.cb_vmOS.currentText(),self.ui.sb_vmmemsize.value(),self.ui.sb_vmvmemsize.value(),self.ui.le_vdiname.text(),(self.ui.sb_vdisize.value())*1000*1000)
                bootorder=self.get_table_bootorder()
                print('bootorder:')
                print(bootorder)
                self.host.socket_processor.vb.set_guest_bootorder(self.ui.le_vmname.text(),bootorder[0],bootorder[1],bootorder[2],bootorder[3])
                self.host.socket_processor.vb.set_guest_cpuexecutioncap(self.ui.le_vmname.text(),self.ui.sb_cpuexecutioncap.value())
                if self.ISOpath is not None:
                    if self.host.FTPstate != True:
                        self.host.socket_processor.vb.ftp_on()
                    for i in range(0,5):
                        if self.host.FTPstate == True:
                            self.ftp_upload()
                            for ma in self.vm.MediumAttachment:
                                if ma[4]=='2':
                                    self.host.socket_processor.vb.add_guest_mediums_dvd(self.vm.Name,ma[0],ma[2],os.path.basename(self.ISOpath),True)
                            self.host.socket_processor.vb.ftp_off()
                            break
                        if i == 4:
                             QMessageBox.question(self, u'提示',u'无法连接服务端的FTP服务')

                if self.ui.cheakb_NAenabled.isChecked():
                    adapterType=None
                    if (self.ui.cb_NAadaptertype.currentText()) == 'I82540EM':
                        adapterType='3'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'Virtio':
                        adapterType='6'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'Am79C973':
                        adapterType='2'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'I82543GC':
                        adapterType='4'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'I82545EM':
                        adapterType='5'
                    if (self.ui.cb_NAbridgedinterface.currentText()) != (self.vm.NetworkAdapter[0])[4] or adapterType!=(self.vm.NetworkAdapter[0])[5] or (self.ui.le_MACaddress.text())!=(self.vm.NetworkAdapter[0])[2] or str(int(self.ui.cheakb_cableconnected))!=(self.vm.NetworkAdapter[0])[6]:
                        self.host.socket_processor.vb.set_guest_networkadapters(self.vm.Name,'0','1',self.ui.le_MACaddress.text(),'2',self.ui.cb_NAbridgedinterface.currentText(),adapterType,str(int(self.ui.cheakb_cableconnected)))
                else:
                    adapterType=None
                    if (self.ui.cb_NAadaptertype.currentText()) == 'I82540EM':
                        adapterType='3'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'Virtio':
                        adapterType='6'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'Am79C973':
                        adapterType='2'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'I82543GC':
                        adapterType='4'
                    elif (self.ui.cb_NAadaptertype.currentText()) == 'I82545EM':
                        adapterType='5'
                    self.host.socket_processor.vb.set_guest_networkadapters(self.vm.Name,'0','0',self.ui.le_MACaddress.text(),'2',self.ui.cb_NAbridgedinterface.currentText(),adapterType,str(int(self.ui.cheakb_cableconnected)))
