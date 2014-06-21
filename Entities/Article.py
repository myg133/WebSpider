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

from Entities.EntityBase import EntityBase


class Article(EntityBase):

    """docstring for Article"""

    def __init__(self):
        EntityBase.__init__(self)
