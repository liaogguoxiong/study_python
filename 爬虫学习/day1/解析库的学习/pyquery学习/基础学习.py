#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-18 11:01
#!@Filename:基础学习.py

'''
如果你对web有所涉及,且比较喜欢使用ccs选择器,那
pyquery是一个更适合你的解析库
'''
html='''
<div>
<ul>
    <li class="item-0"><a href="link1.html">first time</a><span></span></li>
<li class="item-1"><a href="link2.html">second time</a></li>
<li class="item-inactive"><a href="link3.html">thrid time</a></li>
<li class="item-1 item-2"><a href="link4.html">fourth time</a></li>
<li class="item-0 item-2" name="lgx"><a href="link5.html">fifth time</a>
</ul>
</div>

'''
from pyquery import PyQuery as pq
#doc=pq('test.html')
doc=pq(html)            #把html字符串传给PyQuery类,完成初始化
print(doc('li'))

print('______________________________________________________')
'''
url初始化
初始化的参数不仅可以以字符串的形式传递,还可以传入
网页url,只需要指定参数为url即可,PyQuery对象首先
请求这个URL,然后用得到的HTML内容完成初始化,这就
相当于用网页的源代码以字符串的形式传递给ptQuery类
来初始化
'''

# doc=pq('https://cuiqingcai.com/')
# print(doc('title'))
#
# #类似于下面的方法
# print('______________________________________________________')
# import requests
#
# doc=pq(requests.get('https://cuiqingcai.com/').text)
# print(doc('title'))

'''
文件初始化
除了传递url,还可以传递本地的文件,此时将参数指定为filename即可
'''
print('______________________________________________________')
doc=pq(filename='test.html')
print(doc('li'))


print('______________________________________________________')
'''
以上3种初始化方法均可,但最常用的初始化方式还是
以字符串形式传递

基于ccs选择器
'''
doc=pq(filename='test.html')
print(doc('#container .list li'))                   #选择id为container的节点,在其内部选class为list节点内部的所有li节点
print(type(doc('#container .list li')))             #类型为PyQuery类型

print('______________________________________________________')
'''
查找节点,需要用到find()方法,此时传入
的参数是CSS选择器.find()查找的是节点的所有子孙节点
'''

doc=pq(filename='test.html')
items=doc('.list')              #选择class='list'的节点
print(items)
print(type(items))
print('______________________________________________________')
lis=items.find('li')
print(lis)
print(type(lis))
print('______________________________________________________')

'''
如果只想查找子节点,可以使用children()方法
'''
lis=items.children()
print(type(lis))
print(lis)
print('______________________________________________________')

'''
如果要筛选所有子节点中符合条件的节点,比如
筛选出class="item-1"的节点
'''

lis=items.children('.item-1')
print(lis)
print('______________________________________________________')

'''
获取某个节点的父节点使用parent()方法,此方法获取的是父亲节点
如果想要获取祖宗节点,使用parents()方法.
'''
doc=pq(filename='test.html')      #把test.html传入PyQuery类中,完成初始化
items=doc('.list')                #选择class='list'的节点
print(items)
print('______________________________________________________')
parent=items.parent()             #选择class='list'节点的父亲节点
print(parent)
print('______________________________________________________')
parents=items.parents()           #选择class='list'节点的祖宗节点
print(parents)
print('______________________________________________________')
'''
筛选某个祖先节点的话,可以向parents()方法传入css选择器
'''
print("筛选某个祖先节点")
parents=items.parents('.wrap')
print(parents)

print('______________________________________________________')
'''
兄弟节点
'''
li=doc('.list .item-inactive')
print(li.siblings())

print('______________________________________________________')

'''
筛选兄弟节点
'''
print(li.siblings('.item-1.item-2'))

print('______________________________________________________')
'''
pyquery的选择结果可能是多个节点,也可能是单个节点,类型都是PyQuery类型的,
单个字点,可以直接输出打印,但是多个节点就需要遍历来获取了,可以发现调用item()
方法后,会得到一个生成器,遍历一下,就可以得到li节点的对象了
'''
doc=pq(filename='test.html')
lis=doc('li').items()
print(type(lis))
for li in lis:
    print(li)

'''
获取信息,提取节点中的信息,一种是
获取属性,一种是获取文本
'''
print('______________________________________________________')
'''
获取属性
提取到PyQuery类型的节点之后,就可以调用attr()方法来获取属性
'''
print("~~~~")
doc=pq(filename='test.html')
a=doc('.item-inactive a')
print(type(a))
print(a.attr('href'))       #选择单个节点的时候
print(a.attr.href)          #也可以用写成这个,效果一样

'''
如果选择了多个节点,上面的方法只能够
获取第一个节点的属性,而要获取多个节
点的属性的话,需要进行遍历
'''
print('______________________________________________________')
doc=pq(filename='test.html')       #传入html文件,并进行初始化,得到PyQuery对象
a=doc('.list li a')
for item in a.items():             #items()方法把生成器中的pyquery对象变成一个个
    print(item.attr('href'))
print('______________________________________________________')
'''
获取文本
使用text()方法来获取
'''
doc=pq(filename='test.html')
print(doc('.item-0 a ').text())

'''
text()方法返回的是纯文本,如果想要
选择节点的html文本,使用html()
'''
print(doc('.item-0 a '))
print(doc('.item-0 a ').html())      ####!!!!!??????  书上说调用html方法可以获取到所选择节点的的html文本,但是却得到的是纯文本


'''
选择多个节点,text()方法可以直接输出,
而html()方法不会输出html文本,而且只能
输出第一个,如果想输出多个,需要遍历
'''
print('______________________________________________________')
doc=pq(filename='test.html')
a=doc('li a ')
print(a)
print(a.text())
print(a.html())

for item in a.items():
    print(item.html())
print('______________________________________________________')
'''
节点操作,pyquery提供了一系列方法来对节点进行动态修改,
比如为某个节点添加一个class,移除某个节点等,使用addClass和
removeClass方法可以动态地改变节点的属性
'''

doc=pq(filename='test.html')
li=doc('.item-inactive')
print(li)
li.removeClass('item-inactive')
print(li)
li.addClass('item-inactive')
print(li)
print('______________________________________________________')
'''
修改节点:
attr():可以传入2个参数,第一个参数为属性名,第二个参数为属性值.
如果只传入属性名,是获取属性值.传入属性名和属性值的话,是改变属性值
text()和html()如果不传入值的话,是获取文本,传入参数,是改变文本或者html
'''
li=doc('.item-0')
print(li)
li.attr('class','lgx')
print(li)
print(li.text())
li.text('我是廖国雄')
print(li.text())
print(li.html())
# li.html('<span>change item</span>')               #html方法书上说是输出html代码,但是这里是纯文本
# print(li)

print('______________________________________________________')

'''
remove()方法就是移除
'''
html='''
<div class="wrap">
    hello,world
<p>This is a paragraph.</p>
</div>
'''
doc=pq(html)
print(doc.text())           #如果只想获取hello,world的话,直接使用text()方法不能够实现
doc.remove('p')
print(doc)
print(doc.text())           #先把p节点去掉,然后再使用text()方法

'''
伪类选择器
ccs选择器之所以强大,还有一个重要原因是它
支持多种多样的伪类选择器,例如选择第一个节点,最后一个节点
奇偶节点,包含某一文本的节点
'''
print('______________________________________________________')
doc=pq(filename='test.html')
li=doc('li:first-child')
print(li)
li=doc('li:last-child')
print(li)
li=doc('li:gt(1)')                  #从0开始,大于1的节点
print(li)
li=doc('li:nth-child(2n)')
print(li)
li=doc('li:contains(fourth)')
print(li)