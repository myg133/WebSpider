# -*- coding:UTF-8 -*-
# fiel name spider.py
import urllib.request
import os
import sys
import codecs

def getHtml(url):
  req = urllib.request.urlopen('http://www.pythontab.com/')
  f = open('result.txt','w')
  data = req.read()
  req.close()
  data = data.decode('utf-8')
  f.write(data)
  f.close()

if __name__=='__main__':
  req = urllib.request.urlopen('http://manhua.ali213.net/comic/2121/')
  f = open('result.txt','w',encoding='utf-8')
  data = req.read()
  req.close()
  data = data.decode('utf-8')
  f.write(data)
  f.close()
