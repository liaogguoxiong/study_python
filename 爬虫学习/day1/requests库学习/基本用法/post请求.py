#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-28 14:58
#!@Filename:post请求.py

'''
post请求也是比较常见的请求方式
'''
import requests
url='http://httpbin.org/post'
data={
    'name':'lgx',
    'age':22
}
r=requests.post(url,data=data)
print(r.text)