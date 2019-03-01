#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-23 11:28
#!@Filename:登录验证.py
from urllib.error import URLError
from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
url="https://open.jss.com.cn/authorize?client_id=184607B0132642A3&response_type=code&redirect_uri=http://efp.szhtxx.cn/apiv3/applyToken/companyinfo/callback&appKey=yRB4b7No"

username='914403005571508822'
password='508822'

p=HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auto_handler=HTTPBasicAuthHandler(p)
opener=build_opener(auto_handler)

try:
    result=opener.open(url)
    html=result.read().deconde("utf-8")
    print(html)
except URLError as e:
    print(e.reason)
    '''
    不过url的网址不是验证窗口,而是帐号登录的,
    所以报错说找不到
    '''
