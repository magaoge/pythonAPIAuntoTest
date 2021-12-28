# -*- coding: utf-8 -*-
# @Time    : 2021/12/15 2:41 下午
# @Author  : Alen
# @Email   : mat_wu@163.com
# @File    : run_suit.py
# @Software: PyCharm

import unittest
import haohan_HTMLTestRunner
import request_case
from request_case import *
from tools.path_maneger import *

suite = unittest.TestSuite()
# suite.addTest(HttpRequestCase('test_request_api'))

loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(HttpRequestCase))
suite.addTest(loader.loadTestsFromTestCase(DelAccountCase))

runner = unittest.TextTestRunner()

with open(test_report_path,"wb") as file:
    runner = haohan_HTMLTestRunner.HTMLTestRunner( stream=file,#报告输出文件对象
                                                   verbosity=2,#报告详细级别
                                                   title="magaoge 的 haohan 测试报告",#报告标题
                                                   description="第一份测试报告",#报告描述
                                                   tester="magaoge")#测试人
    # 执行
    runner.run(suite)


