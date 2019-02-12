#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-28 12:17
#!@Filename:基本用法.py

import requests
#使用requests库中的get()方法获取一个response对象
r=requests.get('https://www.baidu.com/')
print(type(r))
#状态码
print(r.status_code)
print(type(r.text))
#response的内容
print(r.text)
print(r.cookies)

