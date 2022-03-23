# -*- coding: utf-8 -*- 
# @Time : 2022/3/16 19:54 
# @Author : Yu yang
# @File : setup_down.py
import time
import unittest
import warnings

from selenium import webdriver


#
#
class StartEnd(unittest.TestCase):

    def setUp(self) -> None:
        print('开始测试')
        self.driver = webdriver.Chrome()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        print('退出浏览器')
        time.sleep(1)
        self.driver.quit()