# -*- coding: utf8 -*-
__author__ = '54'
from socket_processor import Socket_processor
from Vm_Class import  VirtualMachineInfo
from Host_Class import HostInfo

class Command():
    def __init__(self,host):
        self.host=host

    def reply_get_host_osversion(self,listset):
        if listset[0]=='success':
            self.host.OSTypeId=listset[2]+listset[3]
            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_get_host_cpuinfo(self,listset):
        if listset[0]=='success':
            self.host.CPUInfo=listset[2]
            self.host.CoreCount=listset[3]
            self.host.CPUCount=listset[4]
            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_get_host_cpu_usage(self,listset):
        if listset[0]=='success':
            self.host.CPUUsage=listset[2]
            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_get_host_memsize(self,listset):
        if listset[0]=='success':
            self.host.MemorySize=listset[2]
            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_get_host_mem_avail(self,listset):
        if listset[0]=='success':
            self.host.MemoryAvailable=listset[2]
            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_get_host_storageinfo(self,listset):
        if listset[0]=='success':
            self.host.DiskTotalSize=listset[3]
            self.host.DiskTotalSize=listset[4]
            self.host.DiskTotalSize=listset[6]
            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_list(self,listset):
        if listset[0]=='success':
            for i in range(2,len(listset)-1):
                vm=VirtualMachineInfo()
                vm.Name=listset[i]
                self.host.VMList.append(vm)

            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_powerstate(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.PowerState=listset[3]

            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_cpucount(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.CPUCount=listset[3]

            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_cpucount(self,listset):
        self.reply_get_guest_cpucount(listset)


    def reply_get_guest_cpuexecutioncap(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.CPUExecutionCap=listset[3]

            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_cpuexecutioncap(self,listset):
        self.reply_get_guest_cpuexecutioncap(listset)

    def reply_get_guest_vramsize(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.VRAMSize=listset[3]

            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_vramsize(self,listset):
        self.reply_get_guest_vramsize(listset)

    def reply_get_guest_memsize(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.MemorySize=listset[3]

            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_performance(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.CPUUsage=listset[3]
                    vm.MemoryUsage=listset[4]

            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_set_guest_name(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:
                    vm.Name=listset[3]

            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)

    def reply_get_guest_osversion(self,listset):
        if listset[0]=='success':
            for vm in self.host.VMList:
                if vm.Name==listset[2]:

            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)


        if listset[0]=='success':


            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)


        if listset[0]=='success':


            if listset[len(listset)-1]:
                self.host.hostcallVcenter()
        else:
            self.host.reportfailure(listset)



     #关键字对应方法字典
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

    def vbox_funcation(self,listset):
        listset=tuple(listset)
        print('-------------------------')
        print(listset)
        self.function_dict[listset[1]](self,listset)