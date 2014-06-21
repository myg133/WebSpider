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


class EntityBase(object):

    def __init__(self):
        self.Datas = list()
        pass

    def Add(self, entitybase):
        self.Datas.append(entitybase)
        pass

    def Remove(self, entitybase):
        try:
            self.Datas.remove(entitybase)
            return True
        except ValueError as e:
            return False
        pass

    pass
