# -*- coding: utf-8 -*-
# @Time    : 2021/12/27 3:49 下午
# @Author  : Alen
# @Email   : 16621710374@163.com
# @File    : delete_case.py
# @Software: PyCharm


import unittest
import warnings

from pojo.pojo_config import PojoList
from tools.do_regx import DoRegx
from tools.http_request import HttpRequest
from ddt import ddt,data
from tools.excel_load import LoadExcel
from tools.mylog import MyLog
from tools.path_maneger import *
from tools.read_config import ReadConfig

# 首先依旧是先读取配置、读取Excel中的数据
test_data = LoadExcel.load_excel(test_config_contrl_path,"DELETE","mode")
print(test_data)

@ddt
class DelAccountCase(unittest.TestCase):
    def setUp(self):
        # 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback5
        warnings.simplefilter('ignore', ResourceWarning)
        pass

    @data(*test_data)
    def test_request_api(self,every_row_data):

        # login_url = "http://127.0.0.1:8888/api/private/v1/login"
        # login_data = {"username":"admin","password":"12345689"}
        # 设置请求头信息
        header = {}
        # 为请求头添加token值，没有时为空
        # header["Authorization"] = getattr(PojoList, "TOKEN")
        header["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE2NDA1ODk1MzQsImV4cCI6MTY0MDY3NTkzNH0.zYYXi6eY6MNWKBappMDmUwQqvNdbCg8wmmtUuc3y4D4"

        # 判断，在执行第二条用例的时候，需要遍历存储的列表
        if every_row_data["caseId"] != 2 :
            # 直接执行请求
            MyLog().info("我请求的数据内容是***************" + str(every_row_data))
            res = HttpRequest.http_request(every_row_data["method"]
                                           ,every_row_data["url"]
                                           ,headers = header)
            actuality = res.json()
        # 判断如果接口请求返回值不为空时，就从接口相应信息中，将token取出来，放入token中
            MyLog().info("我是接口请求的结果**************"+str(res.text))
            # 断言部分新增校验，校验数据库查询前后，是否条数有变化，或者是查询某个字段是否与数据中插入的字段相同
            try:
                # 断言
                # 如果断言通过就返回PASS，如果失败就返回Failed
                self.assertEqual(every_row_data["expected"], res.json()['meta']['status'])
                testResult = "Pass"
            except AssertionError as e:
                print(e)
                testResult = "Failed"
                raise e
            finally:
                # 根据表单名，将对应用例执行的结果回写进Excel
                LoadExcel.write_back(every_row_data["sheet_name"], every_row_data["caseId"] + 1, "result", testResult)
                LoadExcel.write_back(every_row_data["sheet_name"], every_row_data["caseId"] + 1, "actuality",
                                     str(actuality))

        else:
            # delete_id_list = getattr(PojoList,"DEKETE_ID_LIST")
            delete_id_list = [645, 646]
            MyLog().info("我获取到的列表是================{}".format(delete_id_list))

            for i in delete_id_list:
                MyLog().info("i值================{}".format(i))
                after_joint_url = every_row_data["url"] + "/" + str(i)
                # 直接执行请求
                MyLog().info("我请求的数据内容是================" + after_joint_url)
                res = HttpRequest.http_request(every_row_data["method"]
                                               , url = after_joint_url
                                               , headers=header)
                actuality = res.json()
                # 判断如果接口请求返回值不为空时，就从接口相应信息中，将token取出来，放入token中
                MyLog().info("我是接口请求的结果============" + str(res.text))

                # 断言部分新增校验，校验数据库查询前后，是否条数有变化，或者是查询某个字段是否与数据中插入的字段相同
                try:
                    # 断言
                    # 如果断言通过就返回PASS，如果失败就返回Failed
                    self.assertEqual(every_row_data["expected"],res.json()['meta']['status'])
                    testResult = "Pass"
                    continue
                except AssertionError as e:
                    print(e)
                    testResult = "Failed"
                    raise e
                finally:
                    # 并且重写数据返到Excel中，重写的数据包括，caseId,method,describe,url,data,expected,actuality,result
                    # 根据表单名，将对应用例执行的结果回写进Excel
                    LoadExcel.write_back(every_row_data["sheet_name"],every_row_data["caseId"] + 1 ,"result",   testResult)
                    LoadExcel.write_back(every_row_data["sheet_name"],every_row_data["caseId"] + 1, "actuality", str(actuality))

    def tearDown(self):
        pass



