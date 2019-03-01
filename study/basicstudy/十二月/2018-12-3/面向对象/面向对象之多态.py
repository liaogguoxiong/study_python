#时间：    2018/12/17 23:28
#作者：    lgx
#文件名：  面向对象之多态
'''
多态是面向对象的三大特性之一,
多态即一个接口,多个实现,实现了
接口的服用
'''
class animal(object):
    def __init__(self):
        pass
    #静态方法,位于类中,但是不由类管理,可以直接被调用
    @staticmethod
    def tell(obj):
        obj.tell()
class cat(animal):
    def __init__(self,name):
        self.name=name
    def tell(self):
        print("%s在叫"%self.name)

class dog(animal):
    def __init__(self,name):
        self.name=name
    def tell(self):
        print("%s在叫"%self.name)
c1=cat("加菲猫")
d1=dog("旺财")
animal.tell(c1)

