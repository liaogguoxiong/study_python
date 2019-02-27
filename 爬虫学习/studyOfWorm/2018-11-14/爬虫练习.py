#时间：    2018/12/16 23:42
#作者：    lgx
#文件名：  爬虫练习
'''
练习一些小知识
'''
import requests
from bs4 import BeautifulSoup
def getHtmlText(url):
    try:
        r=requests.get(url,timeout=10)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        #print(r.text)
        soup=BeautifulSoup()

    except:
        print("无法获取到信息!")
if __name__ == "__main__":
    url="https://item.jd.com/30906175682.html"
    getHtmlText(url)
