#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-21 9:51
#!@Filename:txt文本存储.py

'''
爬取知乎上的问题,作者以及答案,并
写入txt文本中
'''
import requests
from pyquery import  PyQuery as pq

url='https://www.zhihu.com/explore'
headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
res=requests.get(url,headers=headers)
print(res.status_code)
doc=pq(res.text)
items=doc('.explore-tab .feed-item').items()
for item in items:
    question=item.find('h2').text()
    print("问题:",question)
    author=item.find('.author-link').text()
    print('回答者:',author)
    answer=item.find('.content').text()
    print(answer)
    with open("explore.txt", 'a', encoding='utf-8') as f:
        f.write('\n'.join([question,author,answer]))
        f.write('\n'+'='*50+'\n')


