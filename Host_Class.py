# -*- coding: utf8 -*-
__author__ = 'Razy.Chen'
from socket_processor import *
from Vm_Class import VirtualMachineInfo
from Vbox_Command import Command
#服务端宿主机信息类,用于储存宿主机相关信息,其中包涵虚拟机信息类与跟服务端宿主机通讯的socket_processor对象及其相关函数
class HostInfo():
    def __init__(self):

        #宿主机对象对应的vbox命令操作模块,并将自身作为参数传入
        command=Command(self)

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

    #服务端对应的socket通讯对象
    socket_processor=Socket_processor()

    #Vcenter对象传递过来的失败报告函数
    reportfailure=None

    #Vcenter对象传递过来的通知函数,用于通知vcenter与当前连接的宿主机发生的状态改变
    hostcallVcenter=None
