#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-29 15:18
#!@Filename:search()学习.py

'''
match()方法是从开头开始匹配的,
一旦开头不匹配,那么整个匹配就失败了,
它适合用来检测某个字符串是否符合某个正则
表达式的规则.
search()在匹配时会扫描整个字符串,然后返回
第一个成功匹配的结果,正则表达式可以是字符串的
一部分,在匹配时,search()会依次扫描字符串,直到
找到第一个符合规则的字符串,然后返回匹配内容,如果搜索
完了还没有找到,就返回None
'''
import re
content='hello,i am lgx,my phoneNum is 999999,www.baidu.com'
res=re.search('(\d+)',content)
print(res)
print(res.group())

html='''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路有你</li>
<li data-view="7">
<a herf="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a herf="/3.mp3" singer="廖国雄">大王叫我来巡山</a>
</li>
<li data-view="6"><a herf="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a herf="/5.mp3" singer="陈惠桥">记事本</a></li>
<li data-view="5">
<a herf="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

res=re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(res.group(1),res.group(2))

res=re.search('<p.*?"introduction">(.*?)</p>',html,re.S)
print(res.group(1))


