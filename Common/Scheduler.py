'''
Created on 2014年6月6日

@author: MyGeN
'''

from Common.Msg import *

class Scheduler(object):
    '''
              消息调度器类，主要负责消息转发
    '''
    def __init__(self):
      self.Models = dict()
    
    # Add a model to self
    def RegisterModel(self, Name, Model):
      self.Models[Name] = Model
      pass
    
    # Send message to target model
    def PostMsg(self,msg):
      modelName = msg.get_dst()
      self.Models[modelName].ReviceMsg(msg)
      pass
