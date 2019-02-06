#时间：    2018/12/5 23:32
#作者：    lgx
#文件名：  多继承的继承顺序

'''
多继承的子类继承是有顺序的,
一般来说,py2的经典类是按照
深度优先来继承的,新式类是按
按照广度优先来继承的
py3的经典类或者新式类都是按
照广度优先来继承的
经典类:class hello()
新式类:class hello(object)
'''
class A(object):

    def __init__(self):
        print('A')
class B(A):

    def __init__(self):
        print('B')
class C(A):
    # pass
    def __init__(self):
        print('C')
class D(C,B):
    pass
m=D()
