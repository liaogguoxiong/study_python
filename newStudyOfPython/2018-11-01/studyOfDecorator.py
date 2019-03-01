#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-01 8:55
#!@Filename:studyOfDecorator.py

#装饰器=高阶函数+函数嵌套，装饰别的函数的函数。
#装饰器满足的二个条件：①不改变原函数的源代码②不改变原函数的调用方式
#先写下不改变源代码，改变调用方法
# import time
# def deco(func):#装饰器
#     time_start=time.time()
#     func()
#     time_end=time.time()
#     print("the function running time is:%s"%(time_end-time_start))
#
# def test1():#原函数
#     time.sleep(3)
#     print("i am test1 function")
# def test2():#原函数
#     time.sleep(3)
#     print("i am test2 function")
#
# deco(test1)#没改变原函数的源代码，但是改变的调用方式，之前的调用方式是test1()
# deco(test2)

#
import time

def decorator(func):
    def decor(*args,**kwargs):
        time_start=time.time()
        func(*args,**kwargs)
        time_end=time.time()
        print("the function running time is：%s"%(time_end-time_start))
    return decor()

@decorator
def test1(a):
    time.sleep(3)
    print("i am test1,%s"%a)
@decorator
def test2():
    time.sleep(3)
    print("i am test2")
test1("helllo")
test2

