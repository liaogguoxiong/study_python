#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-28 14:27
#!@Filename:testDemo.py
'''
正则表达式
re.match 从头开始匹配
re.search 匹配包含
re.findall 把所有匹配到的字符放到以列表中的元素返回
re.splitall 以匹配到的字符当做列表分隔符
re.sub      匹配字符并替换
'''
import re
print(re.match('.','hello'))#默认匹配除\n之外的所有字符,若指定flag DOTALL,则匹配任意字符，包括换行
print(re.match('^1.','11hello111'))#匹配以1开头的
print(re.match('abc*','abcccccdkjabkjabcf'))#匹配*号前的字符0次或者多次,c可以不出现,或者出现多次
print(re.findall('abc*','abcccccdkjabkjabcf'))
print("======================================")
print(re.search("11o$","nihaohell11o").group())#
'''
match顺序查找,只找出一个,而findall匹配字符串中所有的项
'''
print(re.match('ab+','abbbddabhhhahhddab'))#匹配+号的前一个字符一次或者多次
print(re.findall('ab+','abbbddabhhhahhddab'))
print(re.match('ab?','abbbddabhhhahhddab'))#匹配前一个字符一次或者0次
print(re.findall('ab?','abbbddabhhhahahddab'))
print(re.findall('ab{3}','abbbddabhhhahahddab'))#匹配前一个字符3次
print(re.findall('ab{0,3}','abbbddabhhhahahddab'))#匹配前一个字符1-3次
print(re.findall('ab{3}|ab','abbbddabhhhahahddab'))#相当于或,匹配到左右两遍都行
print(re.search('ab{3}|ab','abbbddabhhhahahddab').group())
print(re.findall('(ab){2}a(123|456)c','1111ababa456chellop'))
print(re.search('(ab){2}a(123|456)c','1111ababa456chellop').group())


print(re.search('\Ahello1','helloddddd'))#^只是匹配一个字符,而\A匹配的是所有的
print(re.search('HELLO\Z','11111HELLO'))#和$功能一样,匹配以什么结尾的
print(re.match('\dhello','你好啊99hello'))#\d匹配数字0-9
print(re.findall('\dhello','你好啊99hello'))
print(re.search('\dhello','你好啊99hello'))
print(re.findall("\s+","ab\tc1\n3"))
