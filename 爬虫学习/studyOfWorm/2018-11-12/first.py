#时间：    2018/11/12 20:47
#作者：    lgx
#文件名：  first

#今天来爬取新闻的内容

'''
字符串转时间：-strptime
dt=datetime.strptime(str,'%Y年%m月%d日%H%M')
时间转字符串：strftime
dt.strftime(%Y-%m-%d)
'''

import requests
from bs4 import BeautifulSoup
from datetime import datetime
res=requests.get('https://mil.news.sina.com.cn/2018-11-11/doc-ihnstwwq6096324.shtml')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
title=soup.select('.main-title')[0].text
sourcetime=soup.select('.date')[0].text#获取到的时间类型为str
sourcetime=datetime.strptime(sourcetime,'%Y年%m月%d日 %H:%M')
sourceplace=soup.select('.source')[0].text#获取新闻来源
#article=soup.select('#article ')[0].text
for a in soup.select('#article p'):
    print(a.text)
#print(soup.select('#article '))

