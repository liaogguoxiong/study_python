#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-28 17:00
#!@Filename:session.py

import requests
url='http://httpbin.org/cookies/set/number/123456'
requests.get(url)
r=requests.get('http://httpbin.org/cookies')
print(r.text)
###########################
s=requests.Session()
s.get(url)
r=s.get('http://httpbin.org/cookies')
print(r.text)

