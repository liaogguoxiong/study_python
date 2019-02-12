#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-29 10:09
#!@Filename:SSl证书验证.py

'''
requests还提供证书验证的功能,当发送http
请求的时候,它会默认检查SSL证书,我们可以
使用verify参数控制是否检查此证书.
不加verify参数,默认为True,会自动校验
'''

import requests
url='https://10.1.17.15/'
###不加varify参数,默认校验SSL证书
# r=requests.get(url)
# print(r.status_code)

###带varify参数,不校验SSL证书
r=requests.get(url,verify=False)
print(r.status_code)


