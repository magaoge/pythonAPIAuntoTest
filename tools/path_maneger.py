# -*- coding: utf-8 -*-
# @Time    : 2021/12/15 4:49 下午
# @Author  : Alen
# @Email   : 16621710374@163.com
# @File    : path_maneger.py
# @Software: PyCharm

import os

# 返回当前文件相对路径
# os.path.split应该是以系统分隔符去切分获取到的路径
project_root_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# os.path.join(path ,*paths),将path和后面所有的paths变量拼接为字符串路径返回

# 测试数据文件路径
test_data_path = os.path.join(project_root_path,"test_data","apiTestData.xlsx")
# 测试报告输出路径
test_report_path = os.path.join(project_root_path,"test_result/html_report","test_repoet.html")
# 监控日志输出路径
test_log_path = os.path.join(project_root_path,"test_result/log","log.txt")

# 各种配置配置管理的配置文件路径
test_config_contrl_path = os.path.join(project_root_path,"test_data","test_config_contrl.config")

