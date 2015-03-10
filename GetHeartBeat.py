# -*- coding: utf8 -*-
__author__ = 'Razy.Chen'
from PyQt4.QtCore import *
import time
class HeartBeat(QThread):
    def __init__(self,fun,stopfun,parent=None):
        QThread.__init__(self, parent)
        self.set_command_list=fun
        self.disconn=stopfun
        self.stop_flag=False
        #每次发起心跳询问时将heartbeating赋值为Flase,如果外部socket_processor收到heartbeat返回,调用inHeartBeating方法,则赋值为True
        self.heartbeating=False
        self.heartbeatstoptimes=0
    def inHeartBeating(self):
        self.heartbeating=True
        self.heartbeatstoptimes=0
    def stop(self):
        self.stop_flag=True
    def run(self):
        while True:
            if self.stop_flag:
                break
            #如果在2个查询心跳未得到心跳返回,则判定连接的宿主机服务已非正常关闭,则关闭对应的socket连接
            if self.heartbeatstoptimes==3:
                self.disconn()
                break
            self.heartbeating=False
            self.set_command_list('heartbeat')
            time.sleep(1)
            if self.heartbeating:
                continue
            else:
               self.heartbeatstoptimes+=1

