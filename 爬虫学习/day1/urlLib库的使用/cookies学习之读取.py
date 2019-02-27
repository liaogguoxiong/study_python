#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-23 12:00
#!@Filename:cookies学习之读取.py

'''
从保存cookies的文件中读取cookie
'''

import http.cookiejar
import urllib.request

cookie=http.cookiejar.MozillaCookieJar()
cookie.load('cookies.txt',ignore_expires=True,ignore_discard=True)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('https://www.baidu.com/')
print(response.read().decode())