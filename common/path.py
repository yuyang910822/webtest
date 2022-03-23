# -*- coding: utf-8 -*- 
# @Time : 2022/3/16 19:41 
# @Author : Yu yang
# @File : path.py
import os


dirs = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

log_dir = os.path.join(dirs, r'log\自动化日志.log')

dirs = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

mysql_dir = os.path.join(dirs, r'config\mysql.yaml')


jd_log_dir = os.path.join(log_dir,r'JD.log')

jd_api_dir = os.path.join(dirs, r'data\jd_api.yaml')

test_dir = os.path.join(dirs,r'test')

report_dir = os.path.join(dirs,r'reports')

png_dir = os.path.join(dirs,r'reports/images')

url_dir = os.path.join('http://10.3.1.207:8888/')

