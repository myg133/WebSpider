#
#
# Spider.py
# Python implementation of the Class Spider
# Generated by Enterprise Architect
# Created on:      22-05-2014 23:10:09
# Original author: MyGeN
#
#
import sys
try:
    sys.path.index('../')
    pass
except Exception:
    sys.path.append('../')
    pass

import urllib.request
import re


class Spider(object):
    SID = 0

    def __init__(self, url=''):
        Spider.SID += 1
        self.__url = url
        pass

    def Feed(self, url):
        self.__url = url
        pass

    def Go(self):
        req = urllib.request.urlopen(self.__url)
        data = req.read()
        req.close()
        m = re.search(r'charset=(.*)".*', str(data))
        charset = 'utf-8'
        if m.group(1).split('\"')[0]:
            charset = m.group(1).split('\"')[0]
        data = data.decode(charset)
        del self.__url
        return data
