import requests

class HttpRequest:
    @staticmethod
    def http_request(method,url,data = None,headers = None ,verify=False):
        try:
            if method.upper() == "GET":
                res = requests.get(url,params=data,verify=verify)
                return res
            elif method == "POST":
                res = requests.post(url,data=data,headers=headers,verify=verify)
                return res
            elif method.upper() == "DELETE":
                res = requests.delete(url,headers = headers,verify=verify)
                return res
            else:
                print("没有该请求方式的方法！！！")
        except Exception as e:
            print("请求信息错了===="+ str(e))
            raise e

