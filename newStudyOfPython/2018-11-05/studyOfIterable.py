#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-05 15:51
#!@Filename:studyOfIterable.py

"""
我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：

"""

from collections import Iterable #Iterable 属于collections
isinstance([],Iterable)#判断数组是不是可迭代对象
print(isinstance([],Iterable))
print( (i*i for i in range(10)),Iterable)


