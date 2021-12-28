import unittest

from pojo.pojo_config import PojoList
from tools.do_regx import DoRegx
from tools.http_request import HttpRequest
from ddt import ddt,data
from tools.excel_load import LoadExcel
from tools.mylog import MyLog
from tools.path_maneger import *
from tools.read_config import ReadConfig


test_data = LoadExcel.load_excel()
print(test_data)

@ddt
class HttpRequestCase(unittest.TestCase):
    def setUp(self):
        pass


    @data(*test_data)
    def test_request_api(self,every_row_data):

        # login_url = "http://127.0.0.1:8888/api/private/v1/login"
        # login_data = {"username":"admin","password":"12345689"}
        # 设置请求头信息
        header = {}
        # 为请求头添加token值，没有时为空
        header["Authorization"] = getattr(PojoList, "TOKEN")

        # 1.声明列表，用来存放创建于用户返回的ID
        delete_id_list = []

        # 3.收集完成之后，作为数据源，遍历，拼接在删除接口的URL上
        if every_row_data["sheet_name"] == "delAccount" and every_row_data["caseId"] == 2:
            for i in delete_id_list:
                every_row_data["url"] = every_row_data["url"] + "/" + str(i)

                MyLog().info("我请求的数据内容是***************" + str(every_row_data))

                res = HttpRequest.http_request(every_row_data["method"]
                                               , every_row_data["url"]
                                               , eval(every_row_data["data"])
                                               , headers=header)
                actuality = res.json()
                # 判断如果接口请求返回值不为空时，就从接口相应信息中，将token取出来，放入token中
                MyLog().info("我是接口请求的结果***************" + str(res.text))
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
        else :
            MyLog().info("我请求的数据内容是================" + str(every_row_data))
            res = HttpRequest.http_request(every_row_data["method"]
                                           ,every_row_data["url"]
                                           ,eval(every_row_data["data"])
                                           ,headers = header)
            actuality = res.json()
            # 判断如果接口请求返回值不为空时，就从接口相应信息中，将token取出来，放入token中
            MyLog().info("我是接口请求的结果============"+str(res.text))

            try:
                if str(actuality).find("token") != -1:
                    token = actuality["data"]["token"]
                    MyLog().info("我是token值===="+token)
                    setattr(PojoList,"TOKEN",token)

                # 2.根据表名来判断是否收集返回的结果ID
                if every_row_data["sheet_name"] == "register" and str(actuality).find("id") != -1:
                    id = actuality["data"]["id"]
                    delete_id_list.append(id)
                    MyLog().info("创建用户执行完，获取到的managerId列表是：{}".format(delete_id_list))
                    setattr(PojoList, "DEKETE_ID_LIST", delete_id_list)
            except Exception as e:
                MyLog().info("我是对pojo类赋值的报错信息===="+str(e))
                raise e

            # 断言部分新增校验，校验数据库查询前后，是否条数有变化，或者是查询某个字段是否与数据中插入的字段相同
            try:
                # 断言
                # 如果断言通过就返回PASS，如果失败就返回Failed
                self.assertEqual(every_row_data["expected"],res.json()['meta']['status'])
                testResult = "Pass"
            except AssertionError as e:
                print(e)
                testResult = "Failed"
                raise e
            finally:
                # 根据表单名，将对应用例执行的结果回写进Excel
                LoadExcel.write_back(every_row_data["sheet_name"],every_row_data["caseId"] + 1 ,"result",testResult)
                LoadExcel.write_back(every_row_data["sheet_name"],every_row_data["caseId"] + 1, "actuality", str(actuality))

    def tearDown(self):
        pass
