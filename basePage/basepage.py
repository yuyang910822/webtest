# -*- coding: utf-8 -*- 
# @Time : 2022/3/14 17:57 
# @Author : Yu yang
# @File : driver.py
import os
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.log import Log
from common.path import log_dir


class Baseview(Log):
    """
    所有业务逻辑类的基类
    """

    def __init__(self, driver: webdriver.Chrome, url):
        self.driver = driver
        self.driver.get(url)
        self.driver.maximize_window()
        super(Baseview, self).__init__(file=log_dir)
        time.sleep(3)

    def input_element(self, loc, value):
        """
        元素可见场景进行输入操作
        :param loc:
        :param value:
        :return:
        """
        try:
            loc_value = loc[1].split('[')[1].split(']')[0]
            WebDriverWait(self.driver, 20, poll_frequency=1, ignored_exceptions=None). \
                until(EC.visibility_of_any_elements_located(loc), f'{loc_value}元素不可见')

        except TimeoutException as e:
            self.screenshot()
            self.error(f'{e}')
            raise False
        else:
            self.info(f'{loc_value}元素可见，输入{value}')
            # time.sleep(2)
            return self.driver.find_element(*loc).send_keys(value)

    def click_element(self, loc):
        """
        元素可见场景进行点击操作
        :param loc:
        :return:
        """
        try:
            loc_value = loc[1].split('[')[1].split(']')[0]
            WebDriverWait(self.driver, 20, poll_frequency=1, ignored_exceptions=None). \
                until(EC.visibility_of_any_elements_located(loc), f'{loc_value}:元素不可见')
        except TimeoutException as e:
            self.screenshot()
            self.error(e)
            raise False
        else:
            # ['xpath', '//*[@type="button"]']
            self.info(f'{loc_value}元素可见，点击')
            time.sleep(1)
            return self.driver.find_element(*loc).click()

    def text_element(self, loc):
        """
        元素可见场景进行文本获取
        :param loc:
        :return:
        """

        try:
            loc_value = loc[1].split('[')[1].split(']')[0]
            WebDriverWait(self.driver, 2, poll_frequency=0.1, ignored_exceptions=None). \
                until(EC.visibility_of_any_elements_located(loc), f'{loc_value}元素不可见')
        except TimeoutException as e:

            self.screenshot()
            self.error(e)
            raise False
        else:
            data = self.driver.find_element(*loc).text
            self.info(f'{loc_value}元素可见，获取文本:{data}')
            return data

    def getdate(self):
        """
        获取当前日期
        :return:
        """
        return time.strftime('%Y.%m.%d', time.localtime(time.time()))

    def getdatetime(self):
        """
        获取当前日期时间
        :return:
        """
        return time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time()))

    def screenshot(self):
        # """
        # 截图
        # :param name:
        # :return:
        # """
        # self.driver.get_screenshot_as_file(f'../png/{name}{self.getdatetime()}.png')
        # return f'../png/{name}{self.getdatetime()}.png'
        """
        截取图片,并保存在images文件夹

        :param name:
        :return:
        """
        timestrmap = time.strftime('%Y%m%d%H%M%S')
        timestrmap1 = time.strftime('%Y%m%d')

        path = r'C:\Users\yuyang\PycharmProjects\pythonProject3\reports\images\\'
        if not os.path.exists(path + timestrmap1):
            os.mkdir(path + timestrmap1)

        imgPath = os.path.join(f'../reports/images/%s' % str(timestrmap1), '%s.png' % str(timestrmap))

        self.driver.save_screenshot(imgPath)
        print('screenshot:', f"{timestrmap}.png")

    def quit(self):
        time.sleep(2)
        return self.driver.quit()


if __name__ == '__main__':
    pass
