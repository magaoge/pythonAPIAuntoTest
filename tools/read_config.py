# -*- coding: utf-8 -*-
# @Time    : 2021/12/15 9:00 下午
# @Author  : Alen
# @Email   : 16621710374@163.com
# @File    : read_config.py
# @Software: PyCharm

import configparser

class ReadConfig:
    @staticmethod
    def readConfig(path,section,option):
        cf = configparser.ConfigParser()
        cf.read(path, encoding='UTF-8')
        value = cf[section][option]
        return value