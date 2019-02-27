#时间：    2018/12/17 0:04
#作者：    lgx
#文件名：  ip手机电话查询
'''
输入电话号码,手机号码和ip地址
查出归属
做是做出来了,但是成功率太低
'''
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
def getNumHtml(number):
    try:
        hd={"user-agent":"Mozilla"}
        r=requests.get(number,timeout=10,headers=hd)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        soup=BeautifulSoup(r.text,"html.parser")
        data=soup.select(".well")
        data1=data[0].text
        res1 = re.split('基', data1)
        res=re.split(":",res1[0])
        print("归属地:%s"%res[1])
    except:
        print("输入的信息不正确,请重新输入!!!!")
if __name__ == "__main__" :
    while True:
        url = "https://www.ip.cn/index.php?ip="
        number = "https://www.ip.cn/db.php?num="
        print("""
        1:ip查询
        2:号码归属地查询
        3:退出
        """)
        c=input("请输入您的选择:")
        if c == "1":
            ip=input("请输入要查询的ip或者域名:".strip())
            url=url+ip
            print(url)
            getIpHtml(url)
        elif c == "2":
            num=input("请输入要查询的号码:".strip())
            number=number+num
            print(number)
            getNumHtml(number)
        elif c == "3":
            break
        else:
            print("无效的选择,请重新输入!!!!!")

