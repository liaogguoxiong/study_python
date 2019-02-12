#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-18 17:18
#!@Filename:urlLib学习.py

import urllib.request
respond=urllib.request.urlopen('https://www.python.org')
#print(respond.read().decode("utf-8"))
print(type(respond))
#状态码
print(respond.status)
#输出响应头信息
print(respond.getheaders())
#调用getheader方法
print(respond.getheader('Content-Type'))