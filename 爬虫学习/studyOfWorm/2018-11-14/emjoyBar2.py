#时间：    2018/11/14 21:52
#作者：    lgx
#文件名：  emjoyBar2

"""
上次爬了斗图网，程序并且能够下载图片，但是爬取和下载的效率过低。
本程序进行了升级，采用多线程来爬取下载图片。多线程需要用到线程锁，
因为一个数据会被多个线程使用，如果使用的时候不锁住数据，则会导致数据不
一致，比如说，二个线程同时读取一个数据，一个线程改成了数据，但是另一个
线程读取的还是原来的数据，就容易出错，所以使用线程锁

"""
import os
import threading
import urllib.request

import requests
from bs4 import BeautifulSoup

gLock=threading.Lock()#定义全局锁
PAGE_URL_LIST=[]#用来存取页码的url，提供给生产者获取所有的图片url
IMAGE_URL_LIST=[]#用来存取图片的url，提供给消费者下载图片
BASE_URL='http://www.doutula.com/photo/list/?page='
imageCount=0

for i in range(1, 46):
    page_url = BASE_URL + str(i)
    PAGE_URL_LIST.append(page_url)

def producer():

    while True:
        gLock.acquire()#锁住页码列表，用的时候锁住
        if len(PAGE_URL_LIST) == 0:
            gLock.release()#释放页码列表，用完释放
            break
        else:
            pageUrl=PAGE_URL_LIST.pop()
            gLock.release()#用完后释放
            res = requests.get(pageUrl)
            soup = BeautifulSoup(res.content, 'html.parser')
            image_url_list = soup.find_all('img', attrs='img-responsive lazy image_dta')
            gLock.acquire()#全局变量都要锁住
            for image_url in image_url_list:
                imageUrl = image_url['data-original']
                IMAGE_URL_LIST.append(imageUrl)
            gLock.release()
def customer():
    global imageCount
    while True:
        gLock.acquire()
        if len(IMAGE_URL_LIST) == 0:
            gLock.release()
            continue
        else:
            imageUrl=IMAGE_URL_LIST.pop()
            gLock.release()
            imageCount += 1
            filename=imageUrl.split('/').pop()
            path=os.path.join('images',filename)
            urllib.request.urlretrieve(imageUrl,filename=path)
            print(imageCount)

def main():
    for x in range(3):
        th=threading.Thread(target=producer)
        th.start()
    for x in range(5):
        th=threading.Thread(target=customer)
        th.start()

if __name__ == '__main__':

    main()