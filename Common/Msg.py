#######################################################
# 
# Msg.py
# Python implementation of the Class Msg
# Generated by Enterprise Architect
# Created on:      22-05-2014 23:15:10
# Original author: MyGeN
# 
#######################################################

class MSGTYPE(object):
  CALL = 1
  RETURN = 2

class Msg(object):
    def __init__(self, srcModel, dstModel, data = None, msgType = MSGTYPE.CALL, action = None):
      self.__sequence = 0
      self.__src = srcModel
      self.__dst = dstModel
      self.__data = data
      self.__action = action
      self.__type = msgType
      pass

    def WarpSrcDst(self):
      self.__src, self.__dst = self.__dst, self.__src
      pass

    #===========================================================================
    # 属性
    #===========================================================================
    def get_data(self):
      return self.__data


    def get_type(self):
      return self.__type


    def get_src(self):
      return self.__src


    def get_dst(self):
      return self.__dst

    def get_action(self):
      return self.__action


    def set_data(self, value):
      self.__data = value


    def set_type(self, value):
      self.__type = value


    def set_src(self, value):
      self.__src = value


    def set_dst(self, value):
      self.__dst = value

    def set_action(self, value):
      self.__action = value


    def del_data(self):
      del self.__data


    def del_type(self):
      del self.__type


    def del_src(self):
      del self.__src


    def del_dst(self):
      del self.__dst

    def del_action(self):
      del self.__action

    Data = property(get_data, set_data, del_data, "data's docstring")
    Type = property(get_type, set_type, del_type, "type's docstring")
    Src = property(get_src, set_src, del_src, "src's docstring")
    Dst = property(get_dst, set_dst, del_dst, "dst's docstring")
    Action = property(get_action, set_action, del_action, "action's docstring")
    
