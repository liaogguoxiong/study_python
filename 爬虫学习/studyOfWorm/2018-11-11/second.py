#时间：    2018/11/11 21:59
#作者：    lgx
#文件名：  second

#爬取新浪网的文章标题、链接、时间
import requests
from bs4 import BeautifulSoup

res=requests.get("http://mil.news.sina.com.cn/roll/index.d.html?cid=57918")
res.encoding="utf-8"
#print(res.text)
soup=BeautifulSoup(res.text,'html.parser')
for news in soup.select("li"):
    if len(news.select('.time')) > 0:
        time=news.select('.time')[0].text
        title=news.select('a')[0].text
        if len(title) > 5:
            a=news.select('a')[0]['href']
            print(time,title,a)




