#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-19 14:53
#!@Filename:ps4.py

<<<<<<< HEAD
import requests
from pyquery import PyQuery as pq

=======
from pyquery import PyQuery as pq
import requests
>>>>>>> origin/master
# import selenium.webdriver
#
# driver=selenium.webdriver.Chrome()
url="https://item.jd.hk/8314939.html"
# driver.get(url)
headers = {
            'user - agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'}
res=requests.get(url,headers=headers)
html=res.text
doc=pq(html)
a=doc(' div .item')
print(a)
