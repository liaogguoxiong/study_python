#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-05 12:13
#!@Filename:ListGeneration2.py

#斐波拉契数列
def fib(num):
    n,a,b=0,0,1
    while n < num:
        n += 1
        print(b)
        a,b=b,a+b
f=fib(5)



"""
上面的fib函数和generator仅一步之遥。
要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
"""
def generator(num):
    n,a,b=0,0,1
    while n < num :
        yield b
        a,b = b,a+b
        n += 1
    return "我是生成器的返回结果"

g=generator(10)
# print(g)#打印内存地址
# # print(next(g))#由于生成器并没有像列表那样把元素全部生成好，而且调用的时候再生成
# # print(next(g))
# for i in g:
#     print(i)

"""
但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
"""
while True:
    try:
        x=next(g)
        print('g',x)
    except StopIteration as e:
        print('Generator return value',e.value)
        break



