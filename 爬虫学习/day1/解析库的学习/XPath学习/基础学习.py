#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-30 15:26
#!@Filename:基础学习.py


from lxml import etree
text='''
<div>
<ul>
<li class="item-0"><a href="link1.html">first time</a></li>
<li class="item-1"><a href="link2.html">second time</a></li>
<li class="item-inactive"><a href="link3.html">thrid time</a></li>
<li class="item-1"><a href="link4.html">fourth time</a></li>
<li class="item-0"><a href="link5.html">fifth time</a>
</ul>
</div>
'''
#调用HTML类进行初始化,成功构建了XPath解析对象
html=etree.HTML(text)
#因为text文本中最后一个li节点是没有闭合的
#使用etree模块中的tostring()方法修正
res=etree.tostring(html)
#输出的HTML代码是bytes类型的
#print(res)
#使用decode()转成string类型
print(res.decode())



#####################直接读取文本进行解析
print('#############直接读取文本进行解析')
html=etree.parse('./test.html',etree.HTMLParser())
res=etree.tostring(html)
print(res.decode("utf-8"))


######################选取所有符合要求节点
'''
我们一般会用//开头的XPath规则来选择所有符合要求的节点
'''
print('#########选取所有符合要求节点')
html=etree.parse('test.html',etree.HTMLParser())
res=html.xpath('//*')
print(res)
#获取所有的li节点,输出的结果类型为列表
res=html.xpath('//li')
print(res)
print(res[0])

#########选择li节点的所有直接a子节点
print('##选择li节点的所有直接a子节点')
res=html.xpath('//li/a')
print(res)

########获取ul节点下的所有子孙节点a

print('##获取ul节点下的所有子孙节点a')
res=html.xpath('//ul//a')
print(res)

##########父节点
'''
首先选中href属性为link4.html的a节点,
然后再获取其父节点,然后再获取其class属性
'''
res=html.xpath('//a[@href="link4.html"]/../@class')
print(res)

###同时我们也可以通过parent::来获取父节点

res=html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(res)


#######属性匹配
'''
在选取的时候,我们可以使用@符号进行
属性过滤,比如要选取class为item-1的li节点
'''
print('###属性匹配')
res=html.xpath('//li[@class="item-inactive"]')
print(res)

#####文本获取
'''
我们用xpath()中的text()方法来获取节点中的文本
'''
print('#####文本获取')
'''
二种获取文本的写法:
'''
#这种写法是要获取子孙节点中的所有文本
#能够得到最全面的文本信息,但是会包含
#一些换行符等特殊符号
res=html.xpath('//li[@class="item-0"]//text()')
print(res)
'''
获取某些子孙节点下的所有文本且获取的结果比较整洁,
可以先选定到特定的子孙节点,然后再调用text()方法获取文本
'''
res=html.xpath('//li[@class="item-inactive"]/a/text()')
print(res)