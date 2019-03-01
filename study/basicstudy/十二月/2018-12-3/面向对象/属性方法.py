#时间：    2018/12/20 21:05
#作者：    lgx
#文件名：  属性方法
'''
属性方法:把一个方法变成静态属性
'''
class Dog(object):
    def __init__(self,name):
        self.name=name
        self.__food=None
    # #普通方法
    # def eat(self,thing):
    #     print("%s吃%s"%(self.name,thing))

    #属性方法
    @property
    def eat(self):
        print("%s吃%s"%(self.name,self.__food))
    #给属性方法赋值的话需要重新一个复制方法
    @eat.setter
    def eat(self,food):
        print("set to %s"%food)
        self.__food=food
    #而删除属性也是一样,不能够直接删除
    @eat.deleter
    def eat(self):
        del self.__food
        print("变量删除成功")



d1=Dog("小明")
#因为eat()是属性方法,是静态属性,就没有括号了
#也无法传值进去了
# d1.eat(d1,"gutou")
#只能给属性赋值,但是不能够直接给类中的属性方法赋值
d1.eat
d1.eat='骨头'
d1.eat
del d1.eat
d1.eat


