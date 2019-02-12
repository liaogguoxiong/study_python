#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-30 9:37
#!@Filename:sub()学习.py

'''
sub()可以用来修改文本,
传入三个参数,第一个为正则表达式,第二个
为替换的字符,第三个为原字符串
'''
import re
#提取字符串中的所有字母,第二个参数为空
content="324kjhsjakdh332jkhkjfhf333h2jk4h32kj432"
res=re.sub('\d+',"",content)
print(res)

res=re.sub('\d+','hello',content)
print(res)

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
</div>
'''

#获取歌名
res=re.sub('<a.*?>|</a>','',html)
print(res)
res=re.findall('<li.*?>(.*?)</li>',res,re.S)
for i in res:
    print(i.strip())