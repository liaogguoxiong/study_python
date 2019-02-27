#时间：    2018/11/12 22:51
#作者：    lgx
#文件名：  emjoyBar


import os
import urllib.request

# 本程序实现的功能：爬取斗图网上面的表情包，并下载下来
import requests
from bs4 import BeautifulSoup

BASE_URL='http://www.doutula.com/photo/list/?page='
imageCount=0
def download(url):
    global imageCount
    imageCount += 1
    filename=url.split('/').pop()
    path=os.path.join('images',filename)
    urllib.request.urlretrieve(url,filename=path)
    print(imageCount)

def getPageUrl():
    global BASE_URL
    for i in range(1,100):
        page_url=BASE_URL + str(i)
        getImageUrl(page_url)

def getImageUrl(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.content,'html.parser')
    image_url_list=soup.find_all('img',attrs='img-responsive lazy image_dta')
    for image_url in image_url_list:
        url=image_url['data-original']
        download(url)



getPageUrl()

