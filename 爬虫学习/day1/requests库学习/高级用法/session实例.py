#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-29 9:48
#!@Filename:session实例.py

import requests


headers={
    'cookie':'_xsrf=NkuQJjtmIs7XpQ6yULTIRVS10hWYBqAJ; d_c0="AGBms07c4A2PThM_Hvg0j5RdH00dXr8bDvE=|1531208437"; _zap=91c50891-cf08-4d6f-bc0f-8948662c20e3; l_n_c=1; q_c1=77ea157517fd4991a333aef8c900184d|1548656757000|1531208437000; r_cap_id="MDY3Y2U4MDQ5MmQxNDBmZmE5MDc1YjViNDJlNGU4ZTY=|1548656757|b14de56b99e2abf569eb51750c570211b529e354"; cap_id="OWEwZDUxYjEyNjg1NGEzMTg0ZTQ4NDdmN2VjY2U2MTk=|1548656757|7e9c539adc19bfd71284a7a0902ea901e5dfe397"; l_cap_id="N2FkZTZmNTA0ZTdkNGE0YmIzM2ZjYjdiMjM0NjZhZTA=|1548656757|3b261aaae0b016162bcc876220f6de597efcbc32"; n_c=1; __utma=51854390.12114136.1548656761.1548656761.1548656761.1; __utmc=51854390; __utmz=51854390.1548656761.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20180710=1; tgw_l7_route=116a747939468d99065d12a386ab1c5f; capsion_ticket="2|1:0|10:1548664090|14:capsion_ticket|44:NDZlNTkxOWJkOWVkNDNiOWExYmM5YWUzYjJjNWFkMDk=|ba2c82d1fc2bb3d73f80e471316e16499260072cf5d777a1cbf3a2005a2ea190"; z_c0="2|1:0|10:1548664100|4:z_c0|92:Mi4xNUQ5NEF3QUFBQUFBWUdhelR0emdEU1lBQUFCZ0FsVk5KQXM4WFFCT0xFLTJlNDFDTkFLbXItV3BrZmU3WmFUYzJB|269f0c3f87d822a4ab9641158855bcecfdcde42d790365fbb8c262b01eaa16ae"; tst=r',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url='https://www.zhihu.com/people/ggboy-27/activities'

s=requests.Session()
s.get(url=url,headers=headers)
r=s.get(url)
print(r.status_code)
