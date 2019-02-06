#今天来学习作用域、局部变量、全局变量
school="guet"#全部变量，函数外函数内都受影响
def changename(name):
    global age#全局变量，能使函数外面受影响,但是不建议用
    age=10
    school="GUET"#如果同时存在局部变量和全局变量，取的是局部变量
    print("函数内的年龄：%s"%age)
    print("函数里面的学校：%s"%school)
    print("your name that your chage before:%s"%name)
    name="liaoguoxiong"#局部变量
    print("your name that your chage before:%s"%name)

name=input("please input your name:")
changename(name)
school="GUET"
print(name)#不受局部变量的影响
print("函数外面的学校：%s"%school)
print("函数内的年龄：%s"%age)