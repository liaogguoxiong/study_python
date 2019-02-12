#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-13 13:51
#!@Filename:PriceOfPhone.py

#爬取京东网站中的手机价钱

import requests
from bs4 import BeautifulSoup
res=requests.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=60&click=0')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
soup.select('.p-name p-name-type-2')
print(soup)