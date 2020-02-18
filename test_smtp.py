#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#把邮件这几个封装成接口,对象,直接调用

"""
# 第三方 SMTP 服务, 如果本机安装 sendmail（邮件传输代理程序）则不用下属设置
mail_host="smtp.163.com"  #设置服务器
mail_user="xiaodong_hn@163.com"    #用户名
mail_pass="xiaodong2314"   #口令
sender = 'xiaodong_hn@163.com'
receivers = ['xiaodong_hn@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
"""
mail_host="smtp.qq.com"  #设置服务器
mail_user="287210106@qq.com"    #用户名
mail_pass="pydopdsggrnccafd"    #授权码
sender = '287210106@qq.com'
receivers = ['xiaodong_hn@163.com']

mail_msg = """
<p>Python  mail send test ...</p>
<p><a href="http://www.runoob.com">this is link</a></p>
<p>image test：</p>
<p><img src="cid:image1"></p>
"""

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
#message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message = MIMEText(mail_msg, 'html', 'utf-8')  #消息体是网页格式,要设置 html格式

message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
message['To'] = Header("测试", 'utf-8')  # 接收者
subject = 'Python SMTP 邮件测试 html'
message['Subject'] = Header(subject, 'utf-8')

try:
    #如果本机安装 sendmail（邮件传输代理程序）
    #smtpObj = smtplib.SMTP('localhost')

    #使用邮件服务商的 SMTP 访问
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)

    smtpObj.sendmail(sender, receivers, message.as_string())
    print "mail send success"
except smtplib.SMTPException:
    print "Error: can't send mail"