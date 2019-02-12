#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-21 11:02
#!@Filename:data参数.py
'''
request的时候带data参数
'''
import urllib.parse
import urllib.request
#data数据需要转化为字节流,用bytes()方法转化
data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding="utf-8")
#加了参数之后,不是get方法了,而是post方法
respond=urllib.request.urlopen('http://httpbin.org/post',data=data,timeout=1)
#从输出结果看出,data参数出现在了form字段中,以post方式传递数据
print(respond.read().decode())

''''''


