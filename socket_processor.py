# -*- coding: utf8 -*-
__author__ = '54'
from PyQt4.QtCore import *
import socket
import time
from GetHeartBeat import HeartBeat

class Socket_processor(QThread): #注意继承QThread
    def __init__(self,parent=None):
        QThread.__init__(self, parent)#添加QThread初始化方法
        self.msg_sock=None
        #self.thread_sock=None#负责socket通讯与业务处理的子线程
        self.disconn_flag=False #连接断开信号
        self.command_list=[] #需要执行的命令表
        self.result_list=[] #命令返回结果集
        self.loginflag=None #登录验证标志,为1为登录成功,-1为密码错误,-2网络错误
        self.callVcenter=None #由Vcenter传递过来的函数,用于通知vcenter与当前连接的宿主机发生的连接状态改变(如已连接/已断开)
        self.vbox_funcation=None #由Vbox_command传递过来的执行函数
    #封装的传递显示信息的方法
    def tb(self,msg,addr=''):
        print (msg)
        # addr='--'+addr
        # msg=time.asctime()+':  '+msg+addr
        # self.ui.tb_sock.append(msg)

    #重置类实例(重新执行__init__)
    def reset(self):
        self.msg_sock=None
        self.disconn_flag=False #连接断开信号
        self.command_list=[] #需要执行的命令表
        self.result=None #命令返回结果集
        self.loginflag=None
    #连接设置方法,设定连接的IP地址与密码
    def set_conn(self,IPaddr,password):
        self.IPAddr=IPaddr
        self.password=password

    #给命令列表添加命令的方法
    def append_command(self,command):
        self.command_list.append(command)
        print('isappended')

    #socket收到的字符串,每一位字符后会被加上'\x00'.原因不明,以下的遍历用以除去'\x00'
    def remove(self,l):
        list_removed=''
        for tem in l:
            if tem=='\x00':
                continue
            list_removed=list_removed+tem
        return list_removed

    #启动socket线程,开始尝试连接宿主机
    def run(self):
        try:
            print('5')
            #配置socket
            self.msg_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print('111')
            self.msg_sock.setblocking(1)#socket使用阻塞模式
            self.msg_sock.connect_ex((self.IPAddr,54254))
            self.tb(u'正在连接指定宿主机',self.IPAddr)
            self.msg_sock.sendall('login|'+self.password)#发送密码进行验证
            self.tb(u'正在进行连接验证')
            print('111')
            while True:#循环recv()循环
                recv_data=self.msg_sock.recv(4096)
                if len(recv_data) !=0:
                        print(recv_data)
                        break
            list=self.remove(recv_data)
            list=list.split('|')
            if list[0]=='login':
                if list[1]=='success':
                    print('success')
                    self.tb(u'验证成功,已连接',self.IPAddr)
                    #发送成功连接信号
                    #self.emit(SIGNAL('set_flag(int)'),1)
                    self.callVcenter(self.IPAddr,1)
                    self.loginflag=1
                    #开始进入业务处理函数
                    self.link_processor(self.msg_sock)
                elif list[1]=='wrong password':
                    print('wrong password')
                    self.tb(u'验证失败,密码错误',self.IPAddr)
                    self.loginflag=-1
                else:
                    print('failure')
                    self.tb(u'连接失败!')
            self.msg_sock.close()
            self.tb(u'连接断开',self.IPAddr)

            #发送成功断开信号
            self.callVcenter(self.IPAddr,0)
            #self.emit(SIGNAL('set_flag(int)'),2)
        except socket.error,e:
            self.tb(u'网络连接错误,请重试')
            self.loginflag=-2
        finally:
            pass
            self.msg_sock.close()

    #界面断开连接信号对应的方法
    def disconn(self):
        if self.msg_sock is not None:
            self.disconn_flag=True
            #self.emit(SIGNAL("set_info(QString)"),time.asctime()+':  socket is not open !')

    def disconnforheartbeating(self):
        self.disconn_flag=True
        self.tb(u'与宿主机的连接中断',self.IPAddr)

    def link_processor(self,sock): #连接处理函数
        self.tb(u'开始与宿主机进行通讯',self.IPAddr)
        try:
            #开启获取心跳包功能
            self.heartbeat=HeartBeat(self.set_command_list,self.disconnforheartbeating)
            self.heartbeat.start()
            while True:#开始业务处理循环,先判断命令返回结果集列表是否有需要处理的命令,再判断命令列表时候有需要发送的命令
                if self.disconn_flag==True: #判断是否有断开连接的信号
                        self.tb(u'正在断开连接',self.IPAddr)
                        sock.sendall('exit')
                        raise ServerStop()
                        break
                #查找命令表表头是否为空,如为空,跳过此轮循环
                #命令返回结果集list表头是否为空的判断
                if self.result_list==[]:
                    pass
                else:
                    self.vbox_funcation(self.result_list[0])
                    self.result_list.pop(0)
                if self.command_list==[]:
                    continue
                else:
                    sock.sendall(self.command_list[0])
                    self.tb(u'命令 ['+self.command_list.pop(0)+u'] 已发送',self.IPAddr)
                    while True:#循环recv()循环
                        if self.disconn_flag==True: #判断是否有断开连接的信号
                            self.tb(u'正在断开连接',self.IPAddr)
                            sock.sendall('exit')
                            raise ServerStop()
                            break
                        recv_data=self.msg_sock.recv(4096)
                        if len(recv_data) !=0:
                            print(recv_data)
                            break
                    print('recv_data is',recv_data)
                    list=self.remove(recv_data)
                    list=list.split('|')
                    if list[0]=='exit':
                        self.tb(u'宿主机服务被关闭,连接中断',self.IPAddr)
                        raise ServerStop()
                    if list[0]=='heartbeating':
                        self.heartbeat.inHeartBeating()
                        #self.tb(u'收到心跳包,来自',self.IPaddr)
                    self.result_list.append(list)
                    if list[0]=='success':
                        print('??')
                        self.tb(u'命令已执行完成',self.IPAddr)
                        # #加个命令完成信号
                        # self.emit(SIGNAL('set_flag(int)'),3)
                        print(list)
                    elif list[0]=='failure':
                        self.tb(u'命令执行失败',self.IPAddr)
                        #加个命令执行失败信号
                        # self.emit(SIGNAL('set_flag(int)'),4)

            #-----------执行命令表中的命令的循环结束------------------
            #self.emit(SIGNAL('set_flag(int)'),2)

        except socket.error,e:
            self.tb(u'网络通讯错误',self.IPAddr)
        except ServerStop,e:
            pass
        finally:
            sock.close()

class ServerStop(StandardError): #用于在停止服务时直接跳出link_processor的错误
    pass