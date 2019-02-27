#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-22 9:25
#!@Filename:csv文件储存.py

'''
csv,全称为comma-separated values,中文叫做
逗号分隔值或者字符分隔值,其文件以纯文本形式存储
表格数据.该文件是一个字符序列,可以由任意数目的记录
组成,记录间以某种换行符分隔,每条记录由字段组成,字段间
的分隔符是其他字符或者字符串,最常见的是逗号或制表符.
不过所有记录都有完全相同的字段序列,相当于一个结构化的
纯文本形式
'''

import csv

import pandas

'''
一个简单的例子
'''
with open('data.csv','w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(['id','name','age'])
    writer.writerow(['1', 'lgx', '22'])
    writer.writerow(['2', 'zsy', '21'])

'''
如果想修改列与列之间的分隔符,
可以传入delimiter参数
'''
with open('data.csv','a',newline='',encoding='utf-8') as f:
    f.write('_'*50)
    f.write('\n')
    writer=csv.writer(f,delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1', 'lgx', '22'])
    writer.writerow(['2', 'zsy', '21'])

'''
writerows()方法可以同时写入多行,
此时参数就需要二维列表
'''
with open('data.csv','a',newline='',encoding='utf-8') as f:
    f.write('_' * 50)
    f.write('\n')
    writer=csv.writer(f)
    writer.writerows([['id', 'name', 'age'],['1', 'lgx', '22']])


'''
一般情况下,爬虫爬取的都是
结构化的数据,一般是字典,在csv库中也
提供了字典的写入方式
'''
with open('data.csv','a',newline='',encoding='utf-8') as f:
    f.write('_' * 50)
    f.write('\n')
    fn=['id','name','age']
    writer=csv.DictWriter(f,fieldnames=fn)
    writer.writeheader()
    writer.writerow({'id':'1','name':'lgx','age':'22'})
    writer.writerow({'id': '2', 'name': 'zsy', 'age': '21'})

'''
读取
我们同样可以使用csv库来csv文件
'''
with open('data.csv','r',newline='',encoding='utf-8') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)

'''
使用pandas库中的read_csv方法将
数据从csv中读取出来
'''
df=pandas.read_csv('data.csv')
print(df)