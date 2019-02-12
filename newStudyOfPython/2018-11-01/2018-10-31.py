#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-10-31 11:54
#!@Filename:.py
#今天说的是数据的格式输出以及字符串的操作,字符串是 %s;整数 %d;浮点数%f
name="lgx"
age=22
salar=8000.05
str="zhengshiyushiiygedabenzhu,tadishengrishi0613"
print("%s"%name)
print("%d"%age)
print("%d"%salar)
print(str.count("z"))#统计一个字符在字符串中的个数
print(str.capitalize())#让字符串的首字母大写
print(str.casefold())#把字符串中的大写变成小写
print(str[8])#字符串的索引
print(str[0:44])#字符串的切片
print(len(str))#字符串的长度
