# -*- coding: utf-8 -*- 
# @Time : 2022/3/16 11:17 
# @Author : Yu yang
# @File : test_01.py
import unittest

import ddt
from ddt import ddt, data
import parameterized as parameterized

from common.startend import StartEnd
from page.login import Login


class Test_login(StartEnd):
    """
    国际化登录
    """
    url = 'http://web.int.test.fe.hwc.forwardx.com/'

    def test01(self):
        """中文登录成功提示"""
        Projects = Login(self.driver, self.url)
        result = Projects.login(Projects.accont_info[0], Projects.login_result_info[0])

        self.assertTrue(result)

    def test02(self):
        """中文登录失败提示"""
        Projects = Login(self.driver, self.url)
        result = Projects.login(Projects.accont_info[1], Projects.login_result_info[1])
        self.assertTrue(result)

#     def test03(self):
#         """英文登录成功提示"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[0])
#         result = Projects.login(Projects.accont_info[0], Projects.login_result_info[2])
#         self.assertTrue(result)
#
#     def test04(self):
#         """英文登录失败提示"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[0])
#         result = Projects.login(Projects.accont_info[1], Projects.login_result_info[3])
#         self.assertTrue(result)
#
#     def test05(self):
#         """日文登录成功提示"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[1])
#         result = Projects.login(Projects.accont_info[0], Projects.login_result_info[4])
#         self.assertTrue(result)
#
#     def test06(self):
#         """日文登录失败提示"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[1])
#         result = Projects.login(Projects.accont_info[1], Projects.login_result_info[5])
#         self.assertTrue(result)
#
#     def test07(self):
#         """中文公司名称"""
#         Projects = Login(self.driver, self.url)
#         result = Projects.check_text(Projects.company_name, Projects.company_title[0])
#         self.assertTrue(result)
#
#     def test08(self):
#         """英文公司名称"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[0])
#         result = Projects.check_text(Projects.company_name, Projects.company_title[1])
#         self.assertTrue(result)
#
#     def test09(self):
#         """日文公司名称"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[1])
#         result = Projects.check_text(Projects.company_name, Projects.company_title[2])
#         self.assertTrue(result)
#
#     def test10(self):
#         """中文登录按钮名称"""
#         Projects = Login(self.driver, self.url)
#         result = Projects.check_text(Projects.click, Projects.login_button[0])
#         self.assertTrue(result)
#
#     def test11(self):
#         """英文登录按钮名称"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[0])
#         result = Projects.check_text(Projects.click, Projects.login_button[1])
#         self.assertTrue(result)
#
#     def test12(self):
#         """日文登录按钮名称"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[1])
#         result = Projects.check_text(Projects.click, Projects.login_button[2])
#         self.assertTrue(result)
#
#     def test13(self):
#         """中文账号未输入提示"""
#         Projects = Login(self.driver, self.url)
#         result = Projects.check_text(Projects.username_null, Projects.login_info[0])
#         self.assertTrue(result)
#
#     def test14(self):
#         """中文密码未输入提示"""
#         Projects = Login(self.driver, self.url)
#         result = Projects.check_text(Projects.password_null, Projects.login_info[1])
#         self.assertTrue(result)
#
#     def test15(self):
#         """英文账号未输入提示"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[0])
#         result = Projects.check_text(Projects.username_null, Projects.login_info[2])
#         self.assertTrue(result)
#
#     def test16(self):
#         """英文密码未输入提示"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[0])
#         result = Projects.check_text(Projects.password_null, Projects.login_info[3])
#         self.assertTrue(result)
#
#     def test17(self):
#         """日文账号未输入提示"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[1])
#         result = Projects.check_text(Projects.username_null, Projects.login_info[4])
#         self.assertTrue(result)
#
#     def test18(self):
#         """日文密码未输入提示"""
#         Projects = Login(self.driver, self.url)
#         Projects.language_switch(Projects.state_info[1])
#         result = Projects.check_text(Projects.password_null, Projects.login_info[5])
#         self.assertTrue(result)
#
#
# if __name__ == '__main__':
#     # 创建一个测试套件
#     suite = unittest.TestSuite()
#     # 将用例加载到测试套件中
#     suite.addTest(Test_login('test01'))
#     # 用例运行
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
