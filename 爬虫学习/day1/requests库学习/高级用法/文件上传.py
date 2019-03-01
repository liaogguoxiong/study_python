#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-28 15:48
#!@Filename:文件上传.py

'''
requests可以模拟提交一些数据,
假如有的网站需要上传文件,我们也可以
用它来实现
'''

import requests
files={'files':open('icon.ico','rb')}
r=requests.post('http://httpbin.org/post',files=files)
print(r.text)