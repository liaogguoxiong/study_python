#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-29 11:31
#!@Filename:match学习.py

'''
match(正则表达式,字符串),match()会从
字符串的起始位置匹配正则表达式,如果匹配成功,
则返回成功的结果,不成功,返回None
'''

import re
content='Hello 123 4567 World_This is a Regex Demo'
print(len(content))
'''
^:以Hello开头
\s:匹配空格
\d:匹配数字
{n}:匹配前面字符n次
\w:匹配字母,数字,下划线
'''

res=re.match('(^Hello)\s(\d{3})\s\d{4}\s\w{10}',content)
print(res)
#输出匹配的字符
print(res.group())
#输出匹配字符所有字符串的位置
print(res.span())

'''
如果想从匹配的字符串中提取一部分内容
可以使用()把正则表达式匹配对应的部分表达式(子表达式)
括起来.()实际上标记了一个子表达式的开始和结束为止
被标志的子表达式会依次对应每一个分组,调用group()方法
传入组的索引即可
'''
print(res.group(2))

'''
通过匹配  .:可以匹配任意字符,换行符除外
          *:代表匹配前面字符无限次
'''

res=re.match('^H.*o',content)
print(res.group())


'''
贪恋匹配和非贪婪匹配
.*:匹配0次或者多次,这个属于贪婪匹配,会匹配最多次
.*?:非贪婪匹配,会匹配最少次,即0次
'''
content='Hello 12345678 World_This is a Regex Demo'
#贪婪匹配,本来想匹配数字的,但是贪婪匹配之后,会把
#1234567匹配进去.
res=re.match('^He.*(\d+).*Demo$',content)
print(res.group(1))
res=re.match('^He.*?(\d+).*Demo$',content)
print(res.group(1))

#非贪婪匹配,在下面例子中,匹配了0次
print('#非贪婪匹配')
content='Hello World_This is a Regex Demo'
res=re.match('^Hello.*Regex.*?',content)
print(res.group())
res=re.match('^Hello.*Regex.*',content)
print(res.group())


#######################修饰符
'''
常用的修饰符:
re.I:大小写不敏感
re.L:做本地化匹配
re.M:多行匹配,影响^和$
re.S:使.匹配包括换行符在内的所有字符
re.U:根据Unicode字符集解析字符,影响\w,\W,\b.\B
re.x:该标志通过给与你更灵活的格式以便你将正则表达式写得
更容易理解
'''
print('#######################修饰符')
content='''Hello 12345678 World_This 
        is a Regex Demo'''
#####匹配字符串中有换行符,没添加修饰符
res=re.match('^H.*?(\d+).*Demo$',content)
#没有匹配到
print(res)
#添加修饰符,re.S的作用是使.匹配包括换行符在内的所有字符
res=re.match('^H.*?(\d+).*Demo$',content,re.S)
print(res)
print(res.group())
print(res.group(1))


#############转义匹配

content='(百度)www.baidu.com'
res=re.match('\(百度\).*\..*\..*',content)
print(res.group())



