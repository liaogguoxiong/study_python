#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-01 11:46
#!@Filename:1111111111.py
import re

import requests

url='https://www.biqiuge.com/book/3773/429520639.html'
headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
    }
res = requests.get(url, headers=headers)
# 让res.text正确解码网页内容
res.encoding = res.apparent_encoding
reg='<h1>(.*?)</h1>.*?<div id="content" class="showtxt">(.*?)</div>'
#compile()把正则表达式编译成正则表达式对象,
#以便重读使用
pattern = re.compile(reg,re.S)
res1 = re.findall(pattern, res.text)
book_content=res1[0][1]
res2=re.sub('\u3000\u3000','',book_content)
book_content=re.sub('<br /><br />','\n',res2)
print(res2)
