# -*- coding: utf-8 -*-
# @Time    : 2021/12/20 9:28 上午
# @Author  : Alen
# @Email   : 16621710374@163.com
# @File    : mysqls_connecter.py
# @Software: PyCharm

import mysql.connector
from tools.path_maneger import test_config_contrl_path
from tools.read_config import ReadConfig

# # 1.配置信息
connect_config = eval(ReadConfig.readConfig(test_config_contrl_path, "DBCONFIG", "db_config"))
# print(connect_config)


# query_sql = "select * from sp_user where user_id >= 1;"

class MyqslConnect:
    def mysql_connect(self,connect_config,query_sql,count="all"):
        # 2.创建连接
        cnn = mysql.connector.connect(**connect_config)
        # 3.游标cursor
        cursor = cnn.cursor()
        # # 4.写sql语句
        # query_sql = "select * from sp_user where user_id >= 1;"
        # 5.执行sql
        cursor.execute(query_sql)
        # 6.获取结果，打印结果
        if count == 1:
        # fetchone()是查询一条数据，数据返回类型是元祖
            res = cursor.fetchone()
        else:
        # fetchall()是查询多条数据，数据返回类型是列表
            res = cursor.fetchall()
        print(res)

        # 7.关闭游标
        cursor.close()
        # 8.关闭连接
        cnn.close()
#
# if __name__ == '__main__':
#     MyqslConnect().mysql_connect(connect_config,query_sql)