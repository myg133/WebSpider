'''
Created on 2014年6月12日

@author: MyGeN

Description:Entity Base Define

组合模式实现
'''


import sys
try:
    sys.path.index('../')
    pass
except Exception:
    sys.path.append('../')
    pass


class DataEntity(object):

    """docstring for DataEntity"""

    def __init__(self):
        self.__part = list()

    def Construct(self, partOfData):
        self.__part.append(partOfData)
        return self
