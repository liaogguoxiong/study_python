#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-21 10:21
#!@Filename:timeAndDatetime.py

'''
study the module of time and datetime,学习常用模块中的time和datatime模块
'''
import datetime
import time

#返回处理器时间
print(time.process_time())

#返回时间戳，也就是从1970年1月1日到现在的秒数
print(time.time())

#返回与utc（时间标准时间，我们比标准时间快了8个小时）
print(time.timezone/3600)

#返回时间格式"Fri Aug 19 11:14:16 2016"
print(time.asctime())

#返回本地时间的struct time对象格式，返回的是元组
#time.struct_time(tm_year=2018, tm_mon=11, tm_mday=21, tm_hour=10, tm_min=28, tm_sec=13, tm_wday=2, tm_yday=325, tm_isdst=0)
#其中，tm_wday=2（0-6，一周的第3天，）, tm_yday=325（一年的第325天）, tm_isdst=0（是否是夏令时，0为否）
print(time.localtime())
print('------------------------')

#时间字符串 转成 时间戳
#先把时间字符串转成struct-time格式（time.strptime() ），再转化为时间戳格式
string_2_struct=time.strptime('2018年11月21日','%Y年%m月%d日')#时间字符串转成struct-time格式
print(string_2_struct)
string_2_stamp=time.mktime(string_2_struct)#struct-time转成时间戳
print(string_2_stamp)

#讲时间戳换为字符串格式

print(time.localtime(time.time()))#把时间戳转为struct-time格式
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))#struct-time时间格式转化时间字符串


'''
datetime
'''
#返回现在的日期和时间
print(datetime.datetime.now())

#时间戳直接转化为日期格式
print(datetime.date.fromtimestamp(time.time()))
print(datetime.datetime.now() + datetime.timedelta(3))#当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))#当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=-4))#当前时间-4小时，years不行
print(datetime.datetime.now() + datetime.timedelta(minutes=23))#当前时间+23分钟

c_time=datetime.datetime.now()
print(c_time.replace(minute=0,hour=0))#替换当前时间的小时和分钟的数值