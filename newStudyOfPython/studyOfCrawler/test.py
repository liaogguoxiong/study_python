#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-08 14:56
#!@Filename:test.py


#写一个爬虫,爬取一个斗图网站的表情包。

import os
import urllib.request

import requests
from bs4 import BeautifulSoup

'''
分页处理：通过分析网页的链接发现，链接的前部分是是相同的，区别在最后
一个数字，这个数字就是数字的页面。由此我们就可以通过循环得出每个分页的
链接。
'''
BASE_PAGE_URE='http://www.doutula.com/photo/list/?page='#分页链接公共部分
imageAcont=0
#通过循环输出页码，这是获取分页链接函数
def page_url():
    global  PAGE_URL_LIST  #需要定义下，不然识别不出来
    global  BASE_PAGE_URE
    for x in range(1,101):
        url=BASE_PAGE_URE + str(x)#字符串拼接，x为int类型，使用str转化string类型
        imageUrl(url)#调用获取图片链接函数方法
'''
获取图片链接函数
'''
def imageUrl(url):#传入的值为分页的链接
    res=requests.get(url)#获取链接的源码
    content=res.content#获取源码的内容
    soup=BeautifulSoup(content,'html.parser')#使用BeautifulSoup分写网页内容
    image_list=soup.find_all('img',attrs={'class':'img-responsive lazy image_dta'})#获取图片的相关信息
    for image in image_list:#循环输出图片信息
        image_url=image['data-original']#图片的链接的key是data-original，相当于字典
        download(image_url)#调用下载图片方法
'''
此函数用来下载图片、
'''
def download(url):#传入图片的链接，这是图片的真实链接
    global imageAcont#需要定义，函数才能够识别
    name=url.split('/')[-1]#下载的图片需要取名，去图片链接的以'/'划分的最后一段
    path=os.path.join('image',name)#把image文件的路径和name拼接起来
    urllib.request.urlretrieve(url,filename=path)#下载图片
    imageAcont +=1#记录下载的图片数量
    print(imageAcont)

page_url()
