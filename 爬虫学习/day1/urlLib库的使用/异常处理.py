#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-23 16:42
#!@Filename:异常处理.py

'''
URLError
'''
from urllib import request,error

####URLError################

# try:
#     response=request.urlopen("https://www.cnblogs.com/panhongyin/p/5ddddddd")
# except error.URLError as e:
#     print(e.reason)

####URLError################

#########HTTPError##########

# try:
#     response=request.urlopen('https://www.cnblogs.com/panhongyin/p/5ddddddd')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep="\n")

#########HTTPError##########

'''
URLError是HTTPError的父类,会先捕获子类的错误
再去捕获父类的错误.
下面的写法,相当于if-else
'''

# try:
#     response=request.urlopen('https://www.cnblogs.com/panhongyin')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print(response.status)
#     print('Request Successfully!')


'''
有时候,reson返回的不一定是字符串,
也有可能是一个的对象
'''

import socket
import urllib.error
try:
    response=urllib.request.urlopen("https://www.baidu.com",timeout=0.01)
except urllib.error.URLError as  e:
    print(e.reason)
    if isinstance(e.reason,socket.timeout):
        print("TIME OUT!")


