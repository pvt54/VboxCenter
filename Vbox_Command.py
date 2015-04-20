# -*- coding: utf8 -*-
__author__ = '54'
from Vm_Class import VirtualMachineInfo

class Command():
    def __init__(self):
        self.host=None #传递过来的对应的hostinfo对象


    def get_host_osversion(self,reflash=False):
        command='GET_HOST_OSVERSION|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_host_cpuinfo(self,reflash=False):
        command='GET_HOST_CPUINFO|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_host_cpu_usage(self,reflash=False):
        command='GET_HOST_CPU_USAGE|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_host_memsize(self,reflash=False):
        command='GET_HOST_MEMSIZE|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_host_mem_avail(self,reflash=False):
        command='GET_HOST_MEM_AVAIL|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_host_storageinfo(self,reflash=False):
        command='GET_HOST_STORAGEINFO|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_powerstate(self,VMName,reflash=False):
        command='GET_GUEST_POWERSTATE|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_cpucount(self,VMName,reflash=False):
        command='GET_GUEST_CPUCOUNT|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def set_guest_cpucount(self,VMName,CPUCount,reflash=False):
        command='set_guest_cpucount|'+VMName+'|'+str(CPUCount)+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_cpuexecutioncap(self,VMName,reflash=False):
        command='GET_GUEST_CPUEXECUTIONCAP|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def set_guest_cpuexecutioncap(self,VMName,CPUExecutioncap,reflash=False):
        command='SET_GUEST_CPUEXECUTIONCAP|'+VMName+'|'+CPUExecutioncap+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_vramsize(self,VMName,reflash=False):
        command='GET_GUEST_VRAMSIZE|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def set_guest_vramsize(self,VMName,VRAMSize,reflash=False):
        command='SET_GUEST_VRAMSIZE|'+VMName+'|'+str(VRAMSize)+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_memsize(self,VMName,reflash=False):
        command='GET_GUEST_MEMSIZE|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def set_guest_memsize(self,VMName,MEMSize,reflash=False):
        command='SET_GUEST_MEMSIZE|'+VMName+'|'+str(MEMSize)+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_performance(self,VMName,reflash=False):
        command='GET_GUEST_PERFORMANCE|'+VMName+str(reflash)
        self.host.socket_processor.append_command(command)

    def set_guest_name(self,VMName,NewVMName,reflash=False):
        command='SET_GUEST_NAME|'+VMName+'|'+NewVMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_osversion(self,VMName,reflash=False):
        command='GET_GUEST_OSVERSION|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def set_guest_osversion(self,VMName,OSVersion,reflash=False):
        command='SET_GUEST_OSVERSION|'+VMName+'|'+OSVersion+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_bootorder(self,VMName,reflash=False):
        command='GET_GUEST_BOOTORDER|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def set_guest_bootorder(self,VMName,boot1,boot2,boot3,boot4,reflash=False):
        command='SET_GUEST_BOOTORDER|'+VMName+'|'+boot1+'|'+boot2+'|'+boot3+'|'+boot4+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_storagectrls(self,VMName,reflash=False):
        command='GET_GUEST_STORAGECTRLS|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def set_guest_storagectrls(self,VMName,SCName,ControllerType,useHostIOCache,reflash=False):
        #useHostIOCache的类型假设为int,有效值为1,0
        command='SET_GUEST_STORAGECTRLS|'+VMName+'|'+SCName+'|'+ControllerType+'|'+useHostIOCache+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_mediumattachmen(self,VMName,SCName,reflash=False):
        command='GET_GUEST_MEDIUMATTACHMEN|'+VMName+'|'+SCName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_mediums(self,VMName,SCName,reflash=False):
        command='GET_GUEST_MEDIUMS|'+VMName+'|'+SCName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_networkadapters(self,VMName,reflash=False):
        command='GET_GUEST_NETWORKADAPTERS|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def set_guest_networkadapters(self,VMName,slot,enabled,MACAddress,attachmentType,bridgedInterface,adapterType,cableConnected,reflash=False):
        command='SET_GUEST_NETWORKADAPTERS|'+VMName+'|'+slot+'|'+enabled+'|'+MACAddress+'|'+attachmentType+'|'+bridgedInterface+'|'+adapterType+'|'+cableConnected+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_host_networkadapters(self):
        command='GET_HOST_NETWORKADAPTERS'
        self.host.socket_processor.append_command(command)

    def get_guest_sharedfolders(self,VMName,reflash=False):
        command='GET_GUEST_SHAREDFOLDERS|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def add_guest_mediums_dvd(self,VMName,SCName,Port,ISOFileName,reflash=False):
        command='ADD_GUEST_MEDIUMS_DVD|'+VMName+'|'+SCName+'|'+Port+'|'+ISOFileName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def del_machine(self,VMName,reflash=False):
        command='DEL_MACHINE|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def create_new_machine(self,VMName,Description,GuestOSTypes,MemSize,VRAMSize,VdiskName,VdiskSize,reflash=False):
        command='CREATE_NEW_MACHINE|'+VMName+'|'+Description+'|'+GuestOSTypes+'|'+str(MemSize)+'|'+str(VRAMSize)+'|'+VdiskName+'|'+str(VdiskSize)+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def get_guest_description(self,VMName,reflash=False):
        command='GET_GUEST_DESCRIPTION|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def set_guest_description(self,VMName,Description,reflash=False):
        command='SET_GUEST_DESCRIPTION|'+VMName+'|'+Description+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def machine_poweron(self,VMName,reflash=False):
        command='MACHINE_POWERON|'+VMName+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def machine_poweroff(self,VMName,reflash=False):
        VMPidList=[]
        for vm in self.host.VMList:
            if vm.Name==VMName:
                VMPidList=vm.PIDList
        command='MACHINE_POWEROFF|'+VMName
        for pid in VMPidList:
            command=command+'|'+pid
        command=command+'|'+str(reflash)
        self.host.socket_processor.append_command(command)

    def ftp_on(self):
        command='ftp_start'
        self.host.socket_processor.append_command(command)

    def ftp_off(self):
        command='ftp_close'
        self.host.socket_processor.append_command(command)


    def get_guest_list(self,reflash=False):#该函数在获取所有虚拟机名称的列表
        command='GET_GUEST_LIST|'+'|'+str(reflash)
        self.host.socket_processor.append_command(command)
        print ('call get_guest_list')

    #该函数只由reply_get_guest_list函数进行调用,在返回所有虚拟机名称列表并创建对应的对象之后用于填充对象数据
    def findEmptyVM_and_fillin(self):
        for vm in self.host.VMList:
            #通过对VM对象的PowerState属性的None判断来确定是否为空vm对象
            if vm.PowerState is None:
                self.get_guest_powerstate(vm.Name)
                self.get_guest_cpucount(vm.Name)
                self.get_guest_cpuexecutioncap(vm.Name)
                self.get_guest_vramsize(vm.Name)
                self.get_guest_memsize(vm.Name)
                self.get_guest_osversion(vm.Name)
                self.get_guest_bootorder(vm.Name)
                self.get_guest_storagectrls(vm.Name)
                self.get_guest_networkadapters(vm.Name)
                self.get_guest_description(vm.Name,True)
        print('fillin complete')






#-------------------------------------------------------------------------------------------------
#-------------------------------以下为处理服务端回复信息的函数------------------------------------
#-------------------------------------------------------------------------------------------------



    def reply_get_host_osversion(self,listset):
        if listset[0]=='success':
            self.host.OSTypeId=listset[2]+'  '+listset[3]
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_host_cpuinfo(self,listset):
        if listset[0]=='success':
            self.host.CPUInfo=listset[2]
            self.host.CoreCount=listset[3]
            self.host.CPUCount=listset[4]
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_host_cpu_usage(self,listset):
        if listset[0]=='success':
            self.host.CPUUsage=listset[2]
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_host_memsize(self,listset):
        if listset[0]=='success':
            self.host.MemorySize=listset[2]
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_host_mem_avail(self,listset):
        if listset[0]=='success':
            self.host.MemoryAvailable=listset[2]
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_host_storageinfo(self,listset):
        if listset[0]=='success':
            self.host.DiskTotalSize=listset[2]
            self.host.DiskUsageSize=listset[3]
            self.host.DiskUsage=listset[4]
            self.host.VboxTotalSize=listset[5]
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_list(self,listset):
        if listset[0]=='success':
            #需建立已有vm的名称的集合与新vm名称的的集合
            Oldvmset,Newvmset=set(),set()
            if len(self.host.VMList)!=0:
                for vm in self.host.VMList:
                    Oldvmset.add(vm.Name)
            print(Oldvmset)
            if len(listset)>2:
                for i in range(2,len(listset)-1):
                    Newvmset.add(listset[i])
            print (Newvmset)
            print (Newvmset-Oldvmset)
            print (Oldvmset-Newvmset)

            #两集合相减得到新增加的虚拟机名称,如果相剪之后的集合==set()表示为空集,表示有可能没有新虚拟机
            #或者是有虚拟机已经被删除
            if Newvmset-Oldvmset != set() and Oldvmset-Newvmset==set():#有添加新虚拟机的情况
                vmset=Newvmset-Oldvmset
                print ('新增虚拟机')
                print(vmset)
                for name in vmset:
                    vm=VirtualMachineInfo()
                    vm.Name=name
                    self.host.VMList.append(vm)
                self.findEmptyVM_and_fillin()
            elif Newvmset-Oldvmset == set() and Oldvmset-Newvmset != set(): #有删除虚拟机的情况
                vmset=Oldvmset-Newvmset
                print ('减少虚拟机')
                print(vmset)
                for name in vmset:
                    self.host.VMList.remove(name)

            else:#虚拟机列表无变化
                print('无变化')
                pass
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_powerstate(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.PowerState=listset[3]

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_cpucount(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.CPUCount=listset[3]

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_cpucount(self,listset):
        if listset[0]=='success':
            self.reply_get_guest_cpucount(listset)
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)



    def reply_get_guest_cpuexecutioncap(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.CPUExecutionCap=listset[3]

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_cpuexecutioncap(self,listset):
        if listset[0]=='success':
            self.reply_get_guest_cpuexecutioncap(listset)

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)


    def reply_get_guest_vramsize(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.VRAMSize=listset[3]

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_vramsize(self,listset):
        if listset[0]=='success':
            self.reply_get_guest_vramsize(listset)

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)


    def reply_get_guest_memsize(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.MemorySize=listset[3]

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_memsize(self,listset):
        if listset[0]=='success':
            self.reply_get_guest_memsize(listset)

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)


    def reply_get_guest_performance(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.CPUUsage=listset[3]
                    vm.MemoryUsage=listset[4]

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_name(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.Name=listset[3]

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_osversion(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.OSTypeId=listset[3]

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_osversion(self,listset):
        if listset[0]=='success':
            self.reply_get_guest_osversion(listset)

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)


    def reply_get_guest_bootorder(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    for i in range(0,4):
                        vm.BootOrder[i]=listset[i+3]

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_bootorder(self,listset):
        if listset[0]=='success':
            self.reply_get_guest_bootorder(listset)

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)


    def reply_get_guest_storagectrls(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    if vm.Name==listset[2]:
                        i=3
                        while True:
                            sc=[]
                            for ii in range(0,4):
                                sc.append(listset[i])
                                i=i+1
                            vm.StorageControllers.append(sc)
                            self.get_guest_mediumattachmen(listset[2],sc[0])
                            self.get_guest_mediums(listset[2],sc[0])
                            if len(listset)==i+1:
                                break


            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_storagectrls(self,listset):
        if listset[0]=='success':
            self.reply_get_guest_storagectrls(listset)
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_mediumattachmen(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    i=3
                    if len(listset)>4:
                        while True:
                            ma=[]
                            for ii in range(0,5):
                                ma.append(listset[i])
                                i=i+1
                            vm.MediumAttachment.append(ma)
                            if len(listset)==(i+1):
                                break
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_mediums(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    i=3
                    while True:
                        med=[]
                        for ii in range(0,5):
                            med.append(listset[i])
                            i=i+1
                        vm.Medium.append(med)
                        if len(listset)==i+1:
                            break
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_networkadapters(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    i=3
                    while True:
                        med=[]
                        for ii in range(0,7):
                            med.append(listset[i])
                            i=i+1
                        vm.NetworkAdapter.append(med)
                        if len(listset)==i+1:
                            break

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_networkadapters(self,listset):
        self.reply_get_guest_networkadapters(listset)


    def reply_get_host_networkadapters(self,listset):
        if listset[0]=='success':
            for i in range(2,len(listset)):
                self.host.HostNetworkAdapter.append(listset[i])

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
                self.host.reportfailure(listset)

    def reply_get_guest_sharedfolders(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    i=3
                    while True:
                        sf=[]
                        for i in range(0,3):
                            sf.append(listset[i])
                            i=i+1
                        vm.SharedFolders.append(sf)
                        if len(listset)==i+1:
                            break

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_add_guest_mediums_dvd(self,listset):
        if listset[0]=='success':
            #------------------------------
            #如果成功,再执行get_guest_mediumattachmen()与get_guest_medium即可
            #------------------------------
            self.get_guest_mediumattachmen(listset[2],listset[3],listset[len(listset)-1])
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_del_machine(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    self.host.VMList.remove(vm)

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_create_new_machine(self,listset):
        if listset[0]=='success':
            #------------------
            #成功添加新虚拟机后直接调用本地的get_guest_list方法更新虚拟机列表(VMlist)并填充数据
            #------------------
            self.get_guest_list()
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_description(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.Description=listset[3]

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_description(self,listset):
        if listset[0]=='success':
            self.reply_get_guest_description(listset)
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_machine_poweron(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.PowerState=1
                    for i in range(3,len(listset)-1):
                        vm.PIDList.append(listset[i])

            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)

    def reply_machine_poweroff(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.PowerState=5
            if listset[len(listset)-1]=='True':
                self.host.hostcallVcenter('','',1,1)
        else:
            self.host.reportfailure(listset)



    #服务端回复信息对应关键字处理字典
    function_dict={
        'GET_HOST_OSVERSION':reply_get_host_osversion,
        'GET_HOST_CPUINFO':reply_get_host_cpuinfo,
        'GET_HOST_CPU_USAGE':reply_get_host_cpu_usage,
        'GET_HOST_MEMSIZE':reply_get_host_memsize,
        'GET_HOST_MEM_AVAIL':reply_get_host_mem_avail,
        'GET_HOST_STORAGEINFO':reply_get_host_storageinfo,
        'GET_GUEST_LIST':reply_get_guest_list,
        'GET_GUEST_POWERSTATE':reply_get_guest_powerstate,
        'GET_GUEST_CPUCOUNT':reply_get_guest_cpucount,
        'SET_GUEST_CPUCOUNT':reply_set_guest_cpucount,
        'GET_GUEST_CPUEXECUTIONCAP':reply_get_guest_cpuexecutioncap,
        'SET_GUEST_CPUEXECUTIONCAP':reply_set_guest_cpuexecutioncap,
        'GET_GUEST_VRAMSIZE':reply_get_guest_vramsize,
        'SET_GUEST_VRAMSIZE':reply_set_guest_vramsize,
        'GET_GUEST_MEMSIZE':reply_get_guest_memsize,
        'SET_GUEST_MEMSIZE':reply_set_guest_memsize,
        'GET_GUEST_PERFORMANCE':reply_get_guest_performance,
        'SET_GUEST_NAME':reply_set_guest_name,
        'GET_GUEST_OSVERSION':reply_get_guest_osversion,
        'SET_GUEST_OSVERSION':reply_set_guest_osversion,
        'GET_GUEST_BOOTORDER':reply_get_guest_bootorder,
        'SET_GUEST_BOOTORDER':reply_set_guest_bootorder,
        'GET_GUEST_STORAGECTRLS':reply_get_guest_storagectrls,
        'SET_GUEST_STORAGECTRLS':reply_set_guest_storagectrls,
        'GET_GUEST_MEDIUMATTACHMEN':reply_get_guest_mediumattachmen,
        # 'SET_GUEST_MEDIUMS':set_guest_mediums,(待定)
        'GET_GUEST_MEDIUMS':reply_get_guest_mediums,
        'GET_GUEST_NETWORKADAPTERS':reply_get_guest_networkadapters,
        'SET_GUEST_NETWORKADAPTERS':reply_set_guest_networkadapters,
        'GET_HOST_NETWORKADAPTERS':reply_get_host_networkadapters,
        'GET_GUEST_SHAREDFOLDERS':reply_get_guest_sharedfolders,
        # 'ADD_GUEST_SHAREDFOLDERS':add_guest_sharedfolders,(待定)
        # 'REMOVE_GUEST_SHAREDFOLDERS':remove_guest_sharedfolders,(待定)
        'ADD_GUEST_MEDIUMS_DVD':reply_add_guest_mediums_dvd,
        'DEL_MACHINE':reply_del_machine,
        'CREATE_NEW_MACHINE':reply_create_new_machine,
         'GET_GUEST_DESCRIPTION':reply_get_guest_description,
         'SET_GUEST_DESCRIPTION':reply_set_guest_description,
         'MACHINE_POWERON':reply_machine_poweron,
         'MACHINE_POWEROFF':reply_machine_poweroff,
        }

    def vbox_function(self,listset):
        listset=tuple(listset)
        print('-------------------------')
        print(listset)
        self.function_dict[listset[1]](self,listset)
        print('*****************************')