#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-30 10:16
#!@Filename:compile()学习.py

'''
compile方法可以将正则字符串编译
成正则表达式对象,以便在后面的匹配中重复使用
'''
import re
content1='2019-01-30 12:00'
content2='2020-01-30 12:01'
content3='2012-01-30 9:00'
pattern=re.compile('\d{1,2}:\d{1,2}')
res1=re.sub(pattern,'',content1)
res2=re.sub(pattern,'',content2)
res3=re.sub(pattern,'',content3)
print(res1,res2,res3,sep='\n')