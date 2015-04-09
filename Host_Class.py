# -*- coding: utf8 -*-
__author__ = 'Razy.Chen'
from socket_processor import *
from Vm_Class import VirtualMachineInfo
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#服务端宿主机信息类,用于储存宿主机相关信息,其中包涵虚拟机信息类与跟服务端宿主机通讯的socket_processor对象及其相关函数
class HostInfo(QMainWindow):
    def __init__(self,Vcenter):
        QWidget.__init__(self,parent=None)
        #Vcenter实例化对象,用于定义信号
        self.Vcenter=Vcenter
        #宿主机对象对应的vbox命令操作模块,并将自身作为参数传入
        #服务端对应的socket通讯对象
        self.socket_processor=Socket_processor()
        self.socket_processor.vb.host=self
        self.socket_processor.callVcenter=self.hostcallVcenter
        self.connect(self,SIGNAL('callVcenter(QString,QString,QString)'),self.Vcenter.hostcallVcenter)
        self.connect(self,SIGNAL('reportfailure(QString)'),self.Vcenter.reportfailure)

    #宿主机名称
    Name=None

    #是否连接
    isOnline=False

    #宿主机IP地址
    IPAddr=None

    #宿主机操作系统
    OSTypeId=None

    #宿主机CPU信息
    CPUInfo=None

    #宿主机CPU物理核心数
    CoreCount=None

    #宿主机CPU逻辑核心数
    CPUCount=None

    #宿主机内存大小
    MemorySize=None

    #宿主机内存当前可用大小
    MemoryAvailable=None

    #宿主机CPU使用率
    CPUUsage=None

    #宿主机网络适配器名称(用于虚拟网卡桥接设定)
    HostNetworkAdapter=[]

    #宿主机VM文件夹所在分区总大小
    DiskTotalSize=None

    #宿主机VM文件夹所在分区已用大小
    DiskUsageSize=None

    #宿主机VM文件夹所在分区使用率
    DiskUsage=None

    #宿主机VM文件夹大小
    VboxTotalSize=None

    #服务端包含的虚拟机对象列表
    VMList=[]

    #向Vcenter发送产生错误的信号的函数
    def reportfailure(self,failureMSG):
        failureMSG=str(failureMSG)
        self.emit(SIGNAL('reportfailure(QString)'),failureMSG)

    #向Vcenter发送状态的信号的函数
    def hostcallVcenter(self,IPAddr='',state='',reflash=''):
        state=QString(state)
        reflash=QString(reflash)
        self.emit(SIGNAL('callVcenter(QString,QString,QString)'),IPAddr,state,reflash)
        print('Host.Info.hostcallVcenter')
        print(IPAddr,state,reflash)
