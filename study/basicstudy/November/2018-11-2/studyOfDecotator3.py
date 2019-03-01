#时间：    2018/11/2 22:02
#作者：    lgx
#文件名：  studyOfDecotator3

#今天继续学习装饰器
username="lgx"
pwd="liao0121"
def login(func):
    def wrapper(*args,**kwargs):
        _username=input("please input your name:").strip()
        _pwd=input("please input your passwd:").strip()
        if _username==username and pwd == _pwd:
            print("User has passed login system")
            return func(*args,**kwargs) #当装饰的函数有返回值的时候，装饰器中的原函数也要加返回值
        else:
            print("Invalid username or passwd")
    return wrapper
def index():
    print("welcome to index page")
@login
def home():
    print("Welcome to my home")
    return "test this return "

#@login
def bbs():
    print("you can say anything in this bbs")

#index()
x=home()
print(x)
#bbs()


