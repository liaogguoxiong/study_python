#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-23 11:42
#!@Filename:cookies学习之读取cookie.py

import http.cookiejar,urllib.request
# cookie=http.cookiejar.CookieJar()
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response=opener.open('https://www.baidu.com/')
# for item in cookie:
#     print(item.name+"="+item.value)

############################################
###############用文件来保存cookies###########
filename='cookies.txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
responer=opener.open('https://www.baidu.com/')
cookie.save(ignore_discard=True,ignore_expires=True)
