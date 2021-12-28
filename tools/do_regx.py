# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 4:06 下午
# @Author  : Alen
# @Email   : 16621710374@163.com
# @File    : do_regx.py
# @Software: PyCharm
import re

class DoRegx:
    @staticmethod
    def do_regx(regx , replaced_str , target_dict , i):
        # d={"normal_tel":"123","pwd":"7777"}
        # s = "{'mobilephone':'${normal_tel}','pwd':'${pwd}'}"
        # 思想是，首先声明两个字典a,b
        # a字典中的变量值（value），为另外一个字典的key，
        # 然后将a字典中的变量值根据正则匹配取出来， 并且作为获取b字典value的key值
        # 然后将a字典对应key的value值更换为取到的对应b字典key的value值

        while re.search(regx,replaced_str):
            # 取出目标字符串中需要替换的内容
            res = re.search(regx,replaced_str)
            key = res.group()#取出数据是"${}"
            value = res.group(1)#取出数据是花括号里面的内容

            print(res)
            print(res.group())
            print(res.group(1))

            # 从参数化字典中提取需要替换的字符串信息,并且加i
            replace_data = target_dict[value] + str(i)

            # 进行字符串的替换
            replaced_str = replaced_str.replace(key, replace_data)
            print(replaced_str)
        return replaced_str


if __name__ == '__main__':
    # d={"normal_tel":"123","pwd":"7777"}
    # s = "{'mobilephone':'${normal_tel}','pwd':'${pwd}'}"
    every_row_column_value = str({"username":"${username}","password":"123456","mobile":"12345678901","email":"12345678901@163.com","role_id":"111"})
    init_data = {'username': 'magaoge_', 'sheet_name': 'init'}

    after_replace = DoRegx.do_regx("\$\{(.*?)}", every_row_column_value, init_data , 1)
    print(after_replace)