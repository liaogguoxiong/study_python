#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-21 11:02
#!@Filename:JSON文件存储.py

'''
json全称为javaScript object notation也就是
JavaScript对象标记,通过对对象和数组的组合来表示
数据写入:dumps()方法,将JSON对象转为文本字符串
数据读取:loads()方法,将文本字符串转为JSON对象

注意,json格式的key和value需要用双引号括起来

'''
import json

str='''
[{
    "name":"lgx",
    "gender":"man",
    "birthday":"1996-09-27"
},
    {
    "name":"zsy",
    "gender":"female",
    "birthday":"1997-06-21"
    }

]
'''
# print(type(str))
# data=json.loads(str)            #把字符类型转为json对象
# print(data)
# print(type(data))
# print(data[0]['name'])          #获取对应key的值
# print(data[0].get('name'))      #获取对应key的值,如果key不存在,不会报错
# print(data[0].get('age',22))
# print(data)

'''
把str字符串写入文本中
'''
print('__'*50)
with open('jsonText','w',encoding='utf-8') as f:
    f.write(str)
'''
从json文本中读取内容

'''
print('__'*50)
with open('jsonText','r',encoding='utf-8') as f:
    data1=json.loads(f.read())                      #把文件中的内容读出来,并转为json对象,一般读完文件只能读一次,再读的内容就是空了,因为光标已经在最后面了
    print(data1)
    print(type(data1))

with open('jsonText1','w',encoding='utf-8') as f:
    f.write(json.dumps(data1,indent=2))     #indent参数代表缩进字符个数

'''
如果JSON含中文,
'''
info='''
[{
    "name":"廖国雄",
    "gender":"男",
    "birthday":"1996-09-27"
},
    {
    "name":"郑诗雨",
    "gender":"女",
    "birthday":"1997-06-21"
    }

]
'''
# with open('jsonText','a',encoding='utf-8') as f:
#     f.write(json.dumps(info))                   #中文字符变成了unicode字符
with open('jsonText','a',encoding='utf-8') as f:
    f.write(json.dumps(info,ensure_ascii=False))

