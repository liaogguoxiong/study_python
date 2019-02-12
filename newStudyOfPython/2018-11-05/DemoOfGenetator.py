#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-05 15:02
#!@Filename:DemoOfGenetator.py

#写一个生成器的并发运算实例

import time
def consumer(name):
    print("%s准备吃包子!"%name)
    while True:
        baozi=yield
        print("包子[%s]来了，被[%s]吃了"%(baozi,name))
def producer():
    c=consumer('A')
    c2=consumer("B")
    c.__next__()
    c2.__next__()
    print("准备开始做包子")
    for i in range(10):
        time.sleep(1)
        print("做了%s个面包la!"%(i+1))
        c2.send(i+1)#把值传给yield
        c.send(i+1)
producer()