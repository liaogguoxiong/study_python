# @Author  :lgx
# @Time    :2019/2/7 23:04
# @File    :基本用法.py
from bs4 import BeautifulSoup
soup=BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)