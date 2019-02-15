#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-15 10:08
#!@Filename:京东爬虫实例.py

'''
五分钟检查一次是否有货,
有货加入购物车
'''
import requests
from bs4 import BeautifulSoup
class Requests_JingDong():
    '''
    请求京东页面的类
    '''
    def __init__(self,url):
        self.url=url

    def req(self):
        '''
        发送请求的方法
        :return:
        '''
        headers = {
            'user - agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'}
        res=requests.get(self.url,headers=headers)
        res=res.text
        return  res

    def html_analysis(self,ana_text):
        '''
        这个方法用来分析html文本的
        :return:
        '''
        soup=BeautifulSoup(ana_text,'lxml')
        return soup




class JingDong():
    def __init__(self,page_url):
        self.page_url=page_url

    def add_shopping_car(self):
        pass


def main():
    url='https://item.jd.com/100002584142.html'
    JD=Requests_JingDong(url)
    text=JD.req()
    res=JD.html_analysis(text)
    print(res)
if __name__ == '__main__':
    main()