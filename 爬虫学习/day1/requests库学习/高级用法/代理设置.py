#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-29 10:37
#!@Filename:代理设置.py

'''
如果我们同一个ip多次访问一个网站的话,
可能会被弹出验证码,或者跳出登录验证
'''
import requests
url='https://www.taobao.com'
r=requests.get(url)
print(r.status_code)