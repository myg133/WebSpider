# -*- Coding:utf-8 -*-
import codecs
from html.parser import HTMLParser
import sys


class DMHtmlParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.__bContent=False     #
    self.__bValueOfAttr=False #
    self.__strAttrName=None   #
    self.__aTaglist = []  #

  def handle_starttag(self, tag, attrs):
    if tag == "ul" :
      for attr in attrs :
        if attr[0] =="class" and attr [1]== "detail_body_right_sec_three" :
          print(1)


if __name__ == '__main__':
  parser = DMHtmlParser()
  parser.reset()
  f = open("result.txt","r",encoding="utf-8")
  d = f.read()
  parser.feed(d)
