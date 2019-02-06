#时间：    2018/12/14 23:46
#作者：    lgx
#文件名：  面向对象之选课系统
import json
import os
class Course(object):
    def __init__(self,name,price,teacher):
        self.name=name
        self.price=price
        self.teacher=teacher
    def choiceCourse(self,stu_obj):
        pass
class Student(object):
    def __init__(self,id,name,sex,age):
        self.id=id
        self.name=name
        self.sex=sex
        self.age=age
    def tell(self):
        print("""
                the information of student:%s
                id:%d
                name:%s
                age:%d
                sex:%s
            """ % (self.name, self.id,self.name, self.age, self.sex))
    def enroll(self):
        passwd=123456
        if os.path.getsize("account") == 0:
            accountDic = {}
            with open("account","w",encoding="utf-8") as f:
                accountDic[self.id]=passwd
                data=json.dumps(accountDic)
                f.write(data)
        else:
            with open("account","r",encoding="utf-8") as f:
                accountDic=json.loads(f.readline())
                if self.id in accountDic:
                    print("用户已经注册!!")
                else:
                    accountDic[self.id]=passwd
                    data = json.dumps(accountDic)
                    f.write(data)





