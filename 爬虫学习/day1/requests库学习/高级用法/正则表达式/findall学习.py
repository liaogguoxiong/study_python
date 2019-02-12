#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-29 17:16
#!@Filename:findall学习.py

'''
前面search()返回正则表达式的第一个内容,
如果想要获取匹配正则表达式的所有内容,
可以使用findall()
'''

import re
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

#获取超链接,歌手以及歌名
res=re.findall('<li.*?herf="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(res)
for i in res:
    print(i[0],i[1],i[2],sep='\t')