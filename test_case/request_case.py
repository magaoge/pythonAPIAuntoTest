import unittest

from pojo.token_setter import GetToken
from tools.http_request import HttpRequest
from ddt import ddt,data
from tools.excel_load import LoadExcel
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
        header["Authorization"] = getattr(GetToken, "TOKEN")

        print(every_row_data["data"])

        res = HttpRequest.http_request(every_row_data["method"]
                                       ,every_row_data["url"]
                                       ,eval(every_row_data["data"])
                                       ,headers = header)
        actuality = res.json()
        # 判断如果接口请求返回值不为空时，就从接口相应信息中，将token取出来，放入token中
        if actuality["data"]:
            token = actuality["data"]["token"]
            setattr(GetToken,"TOKEN",token)
        print(actuality)

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
            LoadExcel.write_back(every_row_data["sheet_name"],every_row_data["caseId"]+1 ,"result",testResult)
            LoadExcel.write_back(every_row_data["sheet_name"],every_row_data["caseId"] + 1, "actuality", str(actuality))

    def tearDown(self):
        pass
