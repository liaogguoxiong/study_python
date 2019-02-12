#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-30 11:16
#!@Filename:111111111.py
import requests,re,json
url_list=[]
base_url='https://maoyan.com/board/4?offset='
for i in range(10):
    url=base_url+str(i*10)
    url_list.append(url)

for url in url_list:
    headers={
            'user - agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
        }
    res=requests.get(url,headers=headers)
    html=res.text
    pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?<img data-src="(.*?)".*?alt="(.*?)".*?/>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?class="integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    moive_info=re.findall(pattern,html)
    for i in moive_info:
        #print(i[0],i[1],i[2],i[3].strip(),i[4],i[5]+i[6],sep="\t")
        dir={
            "排名":i[0],
            "封面地址":i[1],
            '电影名字':i[2],
            '主演':i[3].strip()[3:],
            '上映时间':i[4].strip()[5:],
            '评分':i[5]+i[6]
        }
        print(dir)
        with open('result.txt','a',encoding='utf-8') as f:
            f.write(json.dumps(dir,ensure_ascii=False)+'\n')




