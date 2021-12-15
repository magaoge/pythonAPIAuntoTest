import requests
from tools.http_request import HttpRequest
from tools.excel_load import *

# login_url = "http://127.0.0.1:8888/api/private/v1/login"
# login_data = {"username":"admin","password":"123456"}
#
# register_url = "http://127.0.0.1:8888/api/private/v1/users"
# register_data = {"Content-Type":"application/json",
#                 "username":"magaoge",
#                  "password":"123456",
#                  "mobile":"12345678901",
#                  "email":"12345678901@163.com",
#                  "rid":"111"}
#
# del_url = "http://127.0.0.1:8888/api/private/v1/users/"
#
# head = {}

httpRequest = HttpRequest()

class RequestApi:

    def test(self):
        print("")
    # def login(self):
    #
    #     res = httpRequest.http_request("POST",login_url,login_data)
    #     # res = requests.request("POST", login_url, params=login_data, verify=False)
    #
    #     # print(res.headers)
    #     print(res.json())
    #     # print(res.status_code)
    #
    #     response_body = res.json()
    #     token = response_body["data"]["token"]
    #     # print(token)
    #
    #     head["Authorization"] = token
    #     token采用反射来获取
    #     return head
    #
    # def register(self):
    #
    #     res = httpRequest.http_request("POST",register_url,register_data,headers=head)
    #     # res = requests.request("POST", register_url, data=register_data,headers=head,verify=False)
    #
    #
    #     response_body = res.json()
    #
    #     # print(res.request.body)
    #     #
    #     # print(res.headers)
    #     # print(response_body)
    #     # print(res.status_code)
    #
    #     new_manager_id = response_body["data"]["id"]
    #     print(new_manager_id)
    #     return new_manager_id
    #
    # def del_manager(self,new_manager_id):
    #     new_register_url = register_url + "/" +str(new_manager_id)
    #     print(new_register_url)
    #     # data是用来做请求体的，这里也是插入的sql，看源码，params是用来查询的sql
    #     res = httpRequest.http_request("DELETE",new_register_url,headers=head)
    #
    #     # res = requests.request("DELETE", new_register_url, headers=head,verify=False)
    #     response_body = res.json()
    #
    #     # print(res.headers)
    #     print(response_body)
    #     # print(res.status_code)

if __name__ == '__main__':

    filePath = "../test_data/apiTestData.xlsx"
    sheetName = "login"
    db = LoadExcel(filePath, sheetName)
    db.get_header()
    # 获取到列表数据
    all_sheet_data = db.load_excel()

    # 遍历列表数据，记得取出data的时候，要转换数据格式
    for item in all_sheet_data:
    # 并且在遍历的同时，进行接口请求
        res = httpRequest.http_request(item["method"], item["url"], eval(item["data"]))
    # 并且将请求得到的相应结果，回写进excel
        result = str(res.json())
        print(result)
        # 这里取值是从1开始，但是表格中需要从第二行开始写入，第一行是行头
        db.write_back(item["caseId"]+1 ,result)



    # RequestApi().login()
    # new_manager_id = RequestApi().register()
    # RequestApi().del_manager(new_manager_id)
