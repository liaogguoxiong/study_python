#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-22 10:09
#!@Filename:timeout参数.py

'''
timeout参数用于设置超时时间,单位为秒
如果超过了设置的时间,还没有响应,就会
抛出异常,如果不指定,就是用全局默认
'''

import socket
import urllib.error
import urllib.request

# respond=urllib.request.urlopen("http://httpbin.org/post",timeout=0.1)
# print(respond.read())

'''上面设置了超时时间为0.1s,服务器没有反应过来,
    抛出了URLError异常,因此捕获这个异常,并给出错误提示'''

try:
    respond=urllib.request.urlopen("http://httpbin.org/post",timeout=0.1)
    print(respond.read())
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("网页超时")

