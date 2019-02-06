#时间：    2018/11/2 21:09
#作者：    lgx
#文件名：  studyOfDecotator2

#今天来学习基本的装饰器

#装饰器
import time
def decotator(func):#装饰器
    def deco(*args,**kwargs):
        time_start=time.time()
        func(*args,**kwargs)
        time_end=time.time()
        print("the function's running time is:%s"%(time_end-time_start))
    return deco#实际返回了deco函数的内存地址
@decotator #相当于test1=decotator(test1)，python把其简单话之后才是@decotator
def test1():
    time.sleep(2)
    print("i am test1")
@decotator
def test2(name):
    time.sleep(2)
    print("name")

test1()#把原函数放入装饰器中加工（更新功能），实际调用的是deco函数
#test2("helloWorld")