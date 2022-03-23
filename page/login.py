# -*- coding: utf-8 -*- 
# @Time : 2022/3/16 11:23 
# @Author : Yu yang
# @File : login.py
import time

from ddt import ddt, data
from selenium.webdriver.common.by import By
from basePage.basepage import Baseview


class Login(Baseview):
    """登录页面"""

    # 账号信息
    accont_info = [['int_admin1', '000000'], ['int_admin', '000000']]
    # 国家信息
    state_info = ['english', 'japanese']
    # 公司标题
    company_title = ['f(x)集群平台系统', 'f(x) Cluster Platform', 'f（x）フリートマネージャー']
    # 账号密码未填写
    login_info = ['用户名不能为空！', '密码不能为空！', 'The username cant be blank!', 'The password cant be blank!',
                  'login.userNameValid', 'login.pwdValid']
    # 登录按钮
    login_button = ['登 录', 'Log in', 'ログイン']
    # 登录结果信息
    login_result_info = ['登录成功', '用户名或密码不正确,请重新登录', 'The login was successful.',
                         'If your username or password is incorrect, sign in again.', 'ログイン成功',
                         'If your username or password is incorrect, sign in again.', ]

    # 用户名
    username = [By.XPATH, '//input[@type="text"]']
    # 账号空提示
    username_null = [By.XPATH, '//form[@class="login-form ant-form ant-form-horizontal"]/child::div[1]/div/div/div']
    # 密码输入
    password = [By.XPATH, '//input[@type="password"]']
    # 密码空提示
    password_null = [By.XPATH, '//form[@class="login-form ant-form ant-form-horizontal"]/child::div[2]/div/div/div']
    # 登录
    click = [By.XPATH, '//*[@type="button"]']
    # 登录结果
    accont_result = [By.XPATH, '//div[@class="ant-message-notice-content"]']
    # 切换国家模式
    icon = [By.XPATH, '//*[@class="svg-icon lang-svg"]']
    # 具体模式
    chinese_icon = [By.XPATH, '//*[text()="简体中文"]']
    english_icon = [By.XPATH, '//*[text()="English"]']
    japanese_icon = [By.XPATH, '//*[text()="日本語"]']
    # 公司名称
    company_name = [By.XPATH, '//div[@class="title"]']

    def login(self, loc, value):
        """
        登录接口
        :param value:
        :param loc: 用户名&密码
        :return:
        """
        self.input_element(self.username, str(loc[0]))
        self.input_element(self.password, str(loc[1]))
        self.click_element(self.click)
        try:
            data = self.text_element(self.accont_result)
            if data == value:
                return True
            else:
                raise ValueError
        except ValueError:
            self.screenshot()
            return False

    def language_switch(self, language):
        """
        国际化切换
        :param language: 选择语言:chinese,english,japanese
        :return:
        """
        self.click_element(self.icon)
        time.sleep(1)
        self.error(language)
        if language == 'chinese':
            self.click_element(self.chinese_icon)
        elif language == 'english':
            self.click_element(self.english_icon)
        else:
            self.click_element(self.japanese_icon)
        time.sleep(1)

    def check_text(self, loc, value):
        """
        校验属性值
        :param loc: 校验的属性
        :param value: 期望值
        :return:
        """
        self.click_element(self.click)
        data = self.text_element(loc)
        try:
            if data == value:
                return True
            else:
                raise ValueError
        except ValueError:
            self.screenshot()


if __name__ == '__main__':
    f = Login('http://web.int.test.fe.hwc.forwardx.com/')
    f.language_switch('english')
