#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-25 14:42
#!@Filename:解析链接.py

'''
parse模块定义了URL的标准处理
urlparse()方法将url分为了6个部分,
解析时有特定的分隔符
://前面的是schme,代表协议
第一个/符号前面的是netloc,代表域名
分号前面的是path,即访问路径
分号后面的是params,代表参数
?号后面的是查询条件,一般用作get类型的URL
#后面是锚点,用于直接定位页面内部的下拉位置
#
'''

######urlparse()实现URL的识别和分段

from urllib.parse import urlparse
print('######urlparse()实现URL的识别和分段')
url="https://www.cnblogs.com/panhongyin/p/5603508.html"
result=urlparse(url)
print(type(result),result,sep="\n")

######urlparse()实现URL的识别和分段

'''
urlparse()的api用法
urllib.parse.urlparse(urlstring,scheme="",allow_fragments=True)
urlstring:必填项,待解析的url
scheme:默认的协议(比如http,https),假如
传入的链接没带协议信息,会将这个作为默认的
协议
allow_fragments:是否忽略fragment,置为false
fragment部分就会被忽略,会被解析为path,parameters
或者query的一部分,fragment为空
'''
#######传入的url中没带协议

print("#######传入的url中没带协议")
result=urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(result)

#######传入的url中没带协议

#######传入的url带协议

print("#######传入的url带协议")
result=urlparse('http://www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(result)

#######传入的url带协议

#######allow_fragments

print("#allow_fragments=True")
result=urlparse('http://www.baidu.com/index.html;#comment',allow_fragments=True)
print(result)
print("#allow_fragments=False")
result=urlparse('http://www.baidu.com/index.html;#comment',allow_fragments=False)
print(result)
'''
ParseResult实际上返回的是一个
元组,可以使用索引顺序来获取,也
可以使用属性名来获取
'''

print("#####获取ParseResult返回结果中的属性")
print(result[0],result.scheme,sep="\n")

#######allow_fragments


#######urlunparse(),url的构造

'''
有了urlparse(),就有它对应的方法urlunparse()
它接受的是可迭代对象,它的长度必须是6,负责会
抛出参数数量不足以及过多的问题
'''
print("#######urlunparse()")
from urllib.parse import urlunparse
data=['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))

#######urlunparser

#######urlsplit()

'''
这个方法和urlparse()方法非常类似,
只不过它不再单独解析params这一部分,
只返回5个结果
'''
from urllib.parse import urlsplit
print("#######urlsplit()")
url="http://www.baidu.com/index.html;user?id=5#comment"
result=urlsplit(url)
print(type(result),result,sep="\n")

'''
SplitResult返回的结果也是元组,
也可以使用下标和属性名来获取对
应的元素
'''
print(result[1],result.netloc,sep="\n")

#######urlsplit()

#######urlunsplit,构造方法

'''
它和urlunparse()类似,但是传入的参数为5个
'''
from urllib.parse import urlunsplit
data=['https','www.baidu.com','index.html','a=6','comment']
result=urlunsplit(data)
print(result)
#######urlunsplit,构造方法

#######urljoin()

'''
生成链接的还有另一个方法,那就是urljoin方法,
我们可以提供一个base_url(基础链接)
作为第一个参数,然后将新的链接作为第二个参数,
该方法会分析base_url的scheme,netloc和path
这3个内容并对新的链接缺失的部分就行补充.base_url
中的其他内容不会如此
'''
print('#######urljoin()')
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com','index.html'))
print(urljoin('http://www.baidu.com','https://cuiqingcai.com/index.html'))
print(urljoin('http://www.baidu.com;user?id=8','https://cuiqingcai.com/index.html'))

#######urljoin()

#######urlencode()

'''
urlencode()在构造GET请求参数的时候非常有用

'''
from urllib.parse import urlencode
print('#######urlencode()')
params={'name':'lgx','age':'22'}
base_url='www.baidu.com?'
url=base_url+urlencode(params)
print(url)

#######urldeconde()

#######parse_qs,反序列化

'''
有了序列化,就会有反序列化
'''
print('#######parse_qs,反序列化')
from urllib.parse import parse_qs
query='name=lgx&age=22'
print(parse_qs(query))

#######parse_qs,反序列化

#######parse_qsl,将参数转化为元组组成

from urllib.parse import parse_qsl
print('#######parse_qsl,将参数转化为元组组成')
query='name=lgx&age=22'
print(parse_qsl(query))

#######parse_qsl,将参数转化为元组组成

#######quote(),该方法可以将内容转化为url编码的格式

'''
url中带中文参数时,有时可能会导致乱码
此时使用该方法可以将中文转化为url编码
'''
from urllib.parse import quote
print('#######quote(),该方法可以将内容转化为url编码的格式')
keyword="壁纸"
url='https://www.baidu.com/s?wd='+quote(keyword)
print(url)
#######quote(),该方法可以将内容转化为url编码的格式

#######unquote(),该方法可以进行url解码

from urllib.parse import unquote
print('#######unquote(),该方法可以进行url解码')
url='https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))

#######unquote(),该方法可以进行url解码



