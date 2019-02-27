#时间：    2019/1/17 23:45
#作者：    lgx
#文件名：  loginDemo

import requests
from  bs4 import BeautifulSoup

headers={
    'cookie':'',
    'User-Agent':'JSESSIONID=1B5BC5154A71B02AF1BA49537C1A8DD7'
}
url='http://192.168.20.57:9081/zzs_kpfw_manager/index.htm'
respond=requests.get(url,headers=headers)
print(respond.status_code)
soup=BeautifulSoup(respond.text,"html.parser")
print(soup.contents)