#时间：    2018/12/4 21:28
#作者：    lgx
#文件名：  继承

'''
面向对象三大特性之继承
'''

#父类
class Person():
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
    def eating(self):
        print("%s在吃饭"%self.Name)
    def talking(self):
        print("%s今天%d岁了"%(self.Name,self.Age))

#子类
class Man(Person):
    #先别做其他,只继承Person这个父类
    #pass

    #除了传入父类需要的参数,如果子类也需要传入参数
    #先把参数传入子类,再把属于父类的参数传入父类进行初始化
    #在子类初始化属于子类的参数
    def __init__(self,name,age,eyes):
        #Person.__init__(self,name,age)
        super(Man,self).__init__(name,age)
        self.eyes=eyes

    #写子类自己的方法
    def smoking(self):
        print("%s在吸烟"%self.Name)

    #重构父类的方法,只运行子类的方法,不运行父类的方法
    def eating(self):
        print("%s在大口吃饭"%self.Name)

    #相同的子类和父类方法都运行
    def talking(self):
        Person.talking(self)
        print("%s在大声说话"%self.Name)

    #看看属于子类的参数是否生效
    def _eyes(self):
        if self.eyes == 'hasclasses':
            print("一个带眼镜的人")
        else:
            print("不带眼镜")

#实例化子类,虽然man类没有传参数,
#但是父类有参数且继承了父类,所以必须要传参数
m1=Man('廖国雄',22,'hasclasses')
# m1.talking()
# m1.smoking()
# m1.eating()
# m1.talking()
m1._eyes()