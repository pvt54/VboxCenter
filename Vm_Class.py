# -*- coding: utf8 -*-
__author__ = 'Razy.Chen'
#虚拟机信息类,用于储存虚拟机的相关配置信息
class VirtualMachineInfo():
    #虚拟机名称(str)
    Name=None

    #虚拟机描述信息(str)
    Description=None

    #虚拟机电源状态int(搭配常数字典MachineState)
    PowerState=None

    #虚拟机操作系统版本(str)
    OSTypeId=None

    #虚拟机CPU分配数量(int)
    CPUCount=None

    #虚拟机CPU使用峰值(int)
    CPUExecutionCap=None

    #虚拟机物理内存大小/MB(int)
    MemorySize=None

    #虚拟机显存大小/MB(int)
    VRAMSize=None

    # #虚拟机剪贴板设定情况(int)(搭配常数字典)
    # ClipboardMode=None

    # #虚拟机session状态(int)(搭配常数字典)
    # SessionState=None

    #虚拟机CPU使用率
    CPUUsage=None

    #虚拟机内存使用率
    MemoryUsage=None

    #虚拟机状态文件路径(str)(注意双反斜杠转义)
    StateFilePath=None

    #虚拟机共享文件夹信息(list)
    #结构:sharedFolders中的元素均为存放了ISharedFolder对象属性的列表,其存放顺序为:[name(str),HostPath(str),Writable(bool)]
    SharedFolders=[]

    #虚拟机引导顺序(list)(搭配参数字典DeviceType)
    #结构:列表长度最长4位,存放DeviceType对应的启动设备序号
    BootOrder=[0, 0, 0, 0]

    #虚拟机存储控制器(list)
    #结构:StorageControllers中的元素均为存放了IStorageController对象属性的列表,其存放顺序为:[Name(str),Bus(int)(搭配常数字典StorageBus),ControllerType(int)(搭配常数字典StorageControllerType),useHostIOCache(bool)]
    StorageControllers=[]

    #虚拟机媒体medium(list)
    #结构:Medium中的元素均为存放了IMedium对象属性的列表,其存放顺序为:[name(str),format(str),DeviceType(int)(搭配常数字典DeviceType),size(long,Byte),logicalSize(long,Byte)]
    #sc_name表示
    Medium=[]

    #结构:MediumAttachment中的元素均为存放了IMediumAttachment对象属性的列表,其存放顺序为:[name(str)(StorageController.name]),name(str)(medium.name),port(int),device=0(int),type(int)(搭配常数字典DeviceType)]
    MediumAttachment=[]

    #虚拟机网络适配器(list)
    #结构:NetworkAdapter中的元素均为存放了INetworkAdapter对象属性的列表,其存放顺序为:[slot(long),enabled(int),MACAddress(str),attachmentType(int)(需搭配常数字典NetworkAttachmentType),BridgedInterface(str),adapterType(int)(需搭配常数字典NetworkAdapterType),cableConnected(bool)]
    NetworkAdapter=[]

    #虚拟机PID列表,用于存储虚拟机运行后产生的进程的PID号
    PIDList=[]