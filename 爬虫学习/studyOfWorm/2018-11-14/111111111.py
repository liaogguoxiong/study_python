#时间：    2018/12/17 22:20
#作者：    lgx
#文件名：  111111111
import requests
from bs4 import BeautifulSoup
import re
def getIpHtml(url):
    try:
        hd={"User-Agent":"Mozilla/5.00"}
        r=requests.get(url,timeout=10,headers=hd)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        soup=BeautifulSoup(r.text,"html.parser")
        data1=soup.select("p")
        for i in data1[0:4]:
            print(i.text)
    except:
        print("输入的信息不正确,请重新输入!!!!")
url="https://www.ip.cn/index.php?ip="
ip=input("请输入您要查询的ip地址:")
url=url+ip
print(url)
getIpHtml(url)
