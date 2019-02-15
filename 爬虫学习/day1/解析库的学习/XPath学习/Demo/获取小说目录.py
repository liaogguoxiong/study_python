#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-12 15:23
#!@Filename:获取小说目录.py

'''
使用xpath来获取小说的目录
'''
from lxml import etree
import requests
headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
    }
url='https://www.biqiuge.com/'
res=requests.get(url,headers=headers)
res.encoding = res.apparent_encoding  # 让res.text正确解码网页内容
# print(res.status_code)
book_html=res.text
html=etree.HTML(book_html)
#print(html)
#获取属性
book_type=html.xpath('//div[@class="nav"]//li//a/text()')
print(book_type[2:])
#获取文本
book_type_url=html.xpath('//div[@class="nav"]//li/a/@href')
print(book_type_url[2:])
for i in book_type_url[2:]:
    print(i[1:-1])
