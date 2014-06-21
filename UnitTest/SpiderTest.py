'''

Created on 2014.6.18

@author: MyGeN

Description: Spider unit test

'''

import sys
try:
    sys.path.index('../')
    pass
except Exception:
    sys.path.append('../')
    pass

import unittest
from WebCrawl.Spider import *


class SpiderTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSpiderFeed(self):
        tSpider = Spider()
        tSpider.Feed('http://blog.sina.com.cn/s/blog_80f3f42d0101c03t.html')
        data = tSpider.Go()
        self.assertIsNotNone(data)
        pass

if __name__ == '__main__':
    unittest.main()
