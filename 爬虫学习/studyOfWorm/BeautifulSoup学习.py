#时间：    2018/12/20 19:37
#作者：    lgx
#文件名：  BeautifulSoup学习
import requests
from bs4 import BeautifulSoup

try:
    res=requests.get('https://python123.io/ws/demo.html')
    # print(res.status_code)
    res.raise_for_status()
    res.encoding=res.apparent_encoding
    # print(res.text)
    soup=BeautifulSoup(res.text,"html.parser")
    #使得获取的源代码跟网页一样
    print(soup.prettify())
    print(soup.title)
    print(soup.a.string)
except:
    print("无法获取网页信息")
