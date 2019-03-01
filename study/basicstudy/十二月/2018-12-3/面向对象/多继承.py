#时间：    2018/12/5 22:10
#作者：    lgx
#文件名：  多继承

'''
继承可以分为单继承和多继承,现在来说说多继承,即
一个子类继承多个父类
'''
class Person(object):
    #初始化子类传入的参数
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
        #定义一个列表,用来存makeFriends方法的对象
        self.friendsList=[]
    def walk(self):
        print("%s有行走的能力"%self.name)

class Relation(object):

    #由于子类继承本类和Person类且Person
    #已经对子类传入的参数进行初始化,本类中
    #就无须初始化了,直接使用

    #传入2个实例化对象
    def makeFriends(self,obj):
        print("%s和%s是好朋友"%(self.name,obj.name))
        #把传入的对象存在列表中
        self.friendsList.append(obj)

class Man(Relation,Person):
#子类,只传入父类Person的参数,需要看
#也传入子类对象的可以看继承.py
#其实Man(Person,Relation)中父类的顺序
#也是有影响的,这个以后遇到了再说吧,因为
#这里调换位置也是可以,解释为:在Relation
#中找不到初始化方法之后,去就Person类找了
      pass
m1=Man("小明","男")
m2=Man("小刚",'男')
m1.makeFriends(m2)
print(m1.friendsList[0].name)

