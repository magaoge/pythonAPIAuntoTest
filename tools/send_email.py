# -*- coding: utf-8 -*-
# @Time    : 2021/12/20 5:57 下午
# @Author  : Alen
# @Email   : 16621710374@163.com
# @File    : send_email.py
# @Software: PyCharm

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from tools.mylog import MyLog

# 邮件发送的用户名和密码
# 需要第三方授权码，所谓第三方授权码，就是在非自有平台登录邮箱所需
from tools.path_maneger import test_report_path, test_config_contrl_path
from tools.read_config import ReadConfig

email_config_dict = eval(ReadConfig.readConfig(test_config_contrl_path,"EMAIL","email_config"))

_user = email_config_dict["_user"]#发信人
_qqcode = email_config_dict["_qqcode"]#这里的密码是邮箱smtp设置的授权码
email_to = email_config_dict["email_to"] #收信人
smtp_server = email_config_dict["smtp_server"]
smtp_port = email_config_dict["smtp_port"]

# 获取时间戳
now = time.strftime("%Y-%m-%d_%H_%M_%S")

class SendEmail:
    # email_to收件方
    # filepath 要发送的附件的路径

    def send_email(self,email_to,filepath):

        # 配置连接smtp的邮件服务器
        stmp = smtplib.SMTP_SSL(smtp_server,smtp_port)
        # 登录邮箱
        stmp.login(_user,_qqcode)

        # Multipart是指分邮件的多个部分
        msg = MIMEMultipart()
        # 发送邮件的主题
        msg["Subject"] = now + "高歌的测试报告"
        msg["From"] = _user
        msg["To"] = email_to

        # -------这是正文部分，正文部分也可以写成HTML
        part = MIMEText("这是测试报告，请查收！")
        msg.attach(part)

        # 附件 ----一次只能添加一个附件文件，如果需要添加多个，那么将该部分代码放入遍历所需添加附件的路径列表就好
        part = MIMEApplication(open(filepath,"rb").read())
        part.add_header("Content-Disposition","attachment",filename = filepath)
        msg.attach(part)

        try:
            stmp.sendmail(_user,email_to,msg.as_string())#发送邮件
            MyLog().info("邮件发送成功！" + str(now))
        except Exception as e:
            MyLog().debug(e)
        stmp.close()

if __name__ == '__main__':

    filepath = test_report_path
    SendEmail().send_email(email_to,filepath)