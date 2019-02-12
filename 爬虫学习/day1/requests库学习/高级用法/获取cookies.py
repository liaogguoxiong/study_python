#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-28 16:02
#!@Filename:获取cookies.py
import requests
url='https://www.baidu.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
r=requests.get(url,headers=headers)
print(r.cookies)
for key,value in r.cookies.items():
    print(key+'='+value)