#时间：    2018/12/24 23:01
#作者：    lgx
#文件名：  反射
'''
hasattr(obj,name_str):判断obj对象中是否有name_str方法,有返回true
getattr(obj,name_str)获取obj对象中的name_str内存对象,然后再上括号调用
'''

class Dog(object):
    def __init__(self,name):
        self.name=name

    def eat(self):
        print("%s在吃骨头"%self.name)

d1=Dog("不加拉多")
#根据用户的输入,去调类的方法
choice=input("请输入您要调用的对象的名字:")
#不能够直接调用
#d.choice()

#使用getattr方法,找到内存对象,然后再加上括号即可调用
# print(getattr(d1,choice))
# getattr(d1,choice)()

#用hasattr来判断是否有这个方法
if hasattr(d1,choice):
    #用getattr调用这个方法
    getattr(d1,choice)()
else:
    print("不存在%s方法"%choice)
    