#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-05 16:35
#!@Filename:DemoOfDecorator.py

#在不修改源代码和调用方式的情况下，实现功能拓展

"""
源代码
"""




"""
现在需要对一些专区进行收费，实现思想，先判断是否登录，登录后再判读是否是vip
"""
def logining(func):
    def login(*args,**kwargs):
        userStatus = False
        uname = "lgx"
        pwd = "liao0121"
        if userStatus == False:  # 用户没有登录
            _uname = input("username:")
            _pwd = input("passwd:")
            if _uname == uname and _pwd == pwd:
                print("Welcome to login....")
                userStatus = True
            else:
                print("Invaild username or Passwd!!")
        if userStatus == True:  # 用户登录了
            c2 = input("您是否是vip会员,y or n:")
            if c2 == "n":
                print("不是vip，请进行充值！")
                c = input("是否进行充值，y or n：")
                if c == "y":
                    print("恭喜您，成为了高贵的vip会员！")
                else:
                    print("退出充值界面")
            else:
                print("进入vip区")
                func(*args,**kwargs)
    return login#返回内存地址
def home():
    print("---------home---------")
@logining
def America(name):
    # login()
    print("---------美国------%s---"%name)
def japen():
    # login()
    print("---------日本---------")
def shenzhen():
    print("----------深圳--------")
# home()
America("hello,test")
# japen()
# shenzhen()