#时间：    2018/10/31 23:52
#作者：    lgx
#文件名：  studyOfDecotator
#今天学习装饰器的必需知识
import time

#定义一个函数，需要装饰的函数，在不更改源代码的情况下，算出函数的运行时间

def bar():
    time.sleep(2)
    print("i want to study hard,please go on")

def deco(func):
    time_start=time.time()#记录开始的时间
    func()
    time_end=time.time()#记录结束的时间，二者之差就是函数运行时间
    print("the function running time is %s"%(time_end-time_start))

deco(bar)




