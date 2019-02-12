#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-22 11:30
#!@Filename:Request学习.py

import urllib.request
# request=urllib.request.Request("https://python.org")
# #传入Request类型的对象,
# respone=urllib.request.urlopen(request)
# print(respone.read().decode('utf-8'))

'''
下面来构造带参数的请求
'''

from urllib import request,parse

url="http://httpbin.org/post"
headers={

    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    'Host':"httpbin.org"
}

dic={
    'name':'liaoguoxiong'
}

data=bytes(parse.urlencode(dic),encoding="utf-8")
# req=request.Request(url=url,data=data,headers=headers,method='POST')
# respond=urllib.request.urlopen(req)
# print(respond.read().decode())
#######################################################
#还可以这样添加headers

req=request.Request(url=url,data=data,method='POST')
req.add_header('User-Agent','1/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
respond=urllib.request.urlopen(req)
print(respond.read().decode())
