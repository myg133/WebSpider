'''
Created on 2014年6月6日

@author: MyGeN
'''
import sys
try:
    sys.path.index('../')
    pass
except Exception:
    sys.path.append('../')
    pass

from Common.Msg import *
from Common.ThreadBase import ThreadBase


class Scheduler(ThreadBase):

    '''
              消息调度器类，主要负责消息转发
    '''

    def __init__(self):
        ThreadBase.__init__(self, 'Scheduler')
        self.Models = dict()

    # Add a model to self
    def RegisterModel(self, Name, Model):
        self.Models[Name] = Model
        pass

    # Send message to target model
    def PostMsg(self, msg):
        self.ReviceMsg(msg)
        pass

    def HandleMsg(self, msg):
        modelName = msg.get_dst()
        self.Models[modelName].ReviceMsg(msg)
        pass
