#时间：    2018/11/11 18:45
#作者：    lgx
#文件名：  First

#今天第一天来学习网络爬虫
from bs4 import BeautifulSoup

html_sample=' \
<html> \
<body> \
<h1 id ="title">helloWorld</h1>\
<a href="#" class="link">This is link1</a>\
<a href="#" class="link">This is link2</a>\
</body> \
</html> '

"""
#print(res.encoding)
#print(res.text)
soup=BeautifulSoup(html_sample,"html.parser")#从标签中抓取文字出来
print(soup.text)
"""


"""
找出特点标签中的html元素
找出select找出含有a标签的元素
soup=BeautifulSoup(html.sample)
header=soup.select('h1')找出h1标签
print（header）

找出select找出含有a标签的元素
soup2=BeautifulSoup(html.sample)
alink=soup.select('a')
print(alink)
"""

soup=BeautifulSoup(html_sample,'html.parser')
header=soup.select('h1')
print(header)#把目标标签存入列表
print(header[0])#把目标标签取出
print(header[0].text)#把标签中的文字取出，用text方法


soup2=BeautifulSoup(html_sample,'html.parser')
alink=soup.select("a")
#循环输出标签中的文字
for link in alink:
    print(link.text)
#因为存在列表中，可以使用下标取出
print(alink)
print(alink[1].text)#取出第二个元素中的值

"""
取得含有特定ccs属性的元素

使用select找出所有id 为title的元素（id前面需要加#）
alink=soup.select('#title')
print(alink)

使用select找出所有class为link的元素（class前面需要.）
soup=BeautifulSoup（html.sample）
link=soup.select('.link')
"""
alink=soup.select('#title')
print(alink[0].text)

link=soup.select('.link')
print(link)
for l in link:
    print(l.text)

'''
取得所有a标签中的超链接
使用select找出所有a标签中的超链接
alinks=soup.select('a')
for link in alinks:
    print(link['href'])
'''
print("===================")
alinks=soup.select('a')
for link in alinks:
    print(link['href'])
