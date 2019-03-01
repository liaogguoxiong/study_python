#时间：    2018/12/9 14:50
#作者：    lgx
#文件名：  选课系统
'''
需求:1:学生通过学号和密码登录选课系统
     2:需要系统有二个列表,选课列表和已选课列表
'''
'''
2018年12月13日 21:49:42 忘记是第几次修改了,还有很多逻辑问题没有写完
比如,选课的时候,读出已选的课程,做了判断,如果选的课程中已经有了,就无法
选择了.如果选了最后一门,还继续选择课程就会造成死循环,应该加上个退出的
功能.其他的等以后再看吧
'''
import json
import os
#账号注册的方法
def enroll():
    while True:
        print("""
              1:注册
              2:退出
        """)
        c=input("请输入您的选择:")
        if c == '1':
            #判断存储账号的文件是否为空,因为为空的文件
            #用json.loads出来会报错
            if os.path.getsize("account") ==0:
                #用account字典来存储账号密码
                account={}
                uname=input("请输入您的学号:".strip())
                passwd=input("请输入您的密码:".strip())
                #key为用户名,密码为值存入字典中
                account[uname]=passwd
                with open("account","w",encoding="utf-8") as f:
                    data=json.dumps(account)
                    f.write(data)
                print("%s注册成功"%uname)
            #文件中存有账号密码的情况
            else:
                with open("account", "r", encoding="utf-8") as f:
                    account = json.loads(f.readline())
                    uname = input("请输入您的学号:".strip())
                    if uname in account:
                        print("该账号已注册过!!!")
                        continue
                    else:
                        uname = input("请输入您的学号:".strip())
                        passwd = input("请输入您的密码:".strip())
                        account[uname] = passwd
                with open("account","w",encoding="utf-8") as f:
                    data=json.dumps(account)
                    f.write(data)
                print("%s注册成功"%uname)
        elif c == '2':
            break
        else:
            print("无效的选择!")

def logging():
    n=0
    while n < 3:
        n +=1
        print("=============欢迎进入选课系统=============")
        uname=input("请输入学号:")
        if os.path.getsize("account") == 0:
            print("账号不存在!!!!!")
        else:
            with open("account","r",encoding="utf-8") as f:
                account=json.loads(f.readline())
                if uname in account:
                    passwd=input("请输入密码:")
                    if passwd == account[uname]:
                        print("欢迎%s进入选课界面:"%uname)
                        while True:
                            print('''
                                               1:选课
                                               2:已选课程
                                               3:退出
                                       ''')
                            c1 = input("请输入您的选择:")
                            if c1 == "1":
                                choiceLesson(uname)
                            elif c1 == "2":
                                userslesson(uname)
                            elif c1 == '3':
                                exit()
                            else:
                                print("无效的选择!")
                    else:
                        print("密码不正确!!!!!")
                else:
                    print("账号不存在,请重试!!")
def choiceLesson(uname):
    yclist=[]
    lessonList=["语文","数学","英语","高数","c语言","java","网络编程"]
    if os.path.getsize("lessonList") ==0:
        userlesson = {}
        while True:
            print('''
                1:语文
                2:数学
                3:英语
                4:高数
                5:c语言
                6:java
                7:网络编程
            ''')
            yc=input("请输入选择您想选择课程的名称:")
            if yc in lessonList:
                yclist.append(yc)
                print("%s选择了%s"%(uname,yc))
                print("""
                1:继续选课
                2:退出选课
                """)
                c=input("请输入您的选择:")
                if c == "2":
                    userlesson[uname]=yclist
                    with open("lessonList","w",encoding="utf-8") as f:
                        data=json.dumps(userlesson)
                        f.write(data)
                    break
                elif c == "1":
                    continue
                else:
                    print("无效的选择!!")
            else:
                print("课程不存在,请重新输入")
    #文本中已经存在选课内容的情况
    else:
        with open("lessonList", "r", encoding="utf-8") as f:
            userlesson=json.loads(f.readline())
        #已经选过课的情况
        if uname in userlesson:
            ulesson=userlesson[uname]
            while True:
                print('''
                    1:语文
                    2:数学
                    3:英语
                    4:高数
                    5:c语言
                    6:java
                    7:网络编程
                    q:退出
                ''')
                yc = input("请输入选择您想选择课程的名称:")
                if yc in lessonList:
                    if yc in ulesson:
                        print("%s您已经选过了,请重新选择!")
                        continue
                    else:
                        ulesson.append(yc)
                        print("%s选择了%s" % (uname, yc))
                        print("""
                                    1:继续选课
                                    2:退出选择
                                    """)
                        c = input("请输入您的选择:")
                        if c == "2":
                            userlesson[uname] = ulesson
                            with open("lessonList", "w", encoding="utf-8") as f:
                                data = json.dumps(userlesson)
                                f.write(data)
                            break
                        elif c == '1':
                            continue
                        else:
                            print("无效的选择!")
                elif yc == "q":
                    break
                else:
                    print("课程不存在,请重新输入")
        else:
            ulesson=[]
            while True:
                print('''
                    1:语文
                    2:数学
                    3:英语
                    4:高数
                    5:c语言
                    6:java
                    7:网络编程
                ''')
                yc = input("请输入选择您想选择课程的名称:")
                if yc in lessonList:
                    ulesson.append(yc)
                    print("%s选择了%s" % (uname, yc))
                    print("""
                                1:继续选课
                                2:退出选择
                                """)
                    c = input("请输入您的选择:")
                    if c == "2":
                        userlesson[uname] = ulesson
                        with open("lessonList", "w", encoding="utf-8") as f:
                            data = json.dumps(userlesson)
                            f.write(data)
                        break
                    elif c == '1':
                        continue
                    else:
                        print("无效的选择!")
                else:
                    print("课程不存在,请重新输入")





def userslesson(uname):
    print("=====%s的课程表====="%uname)
    if os.path.getsize("lessonList") == 0:
        print("%s没有选择课程"%uname)
    else:
        with open("lessonList","r",encoding="utf-8") as f:
            lessondic=json.loads(f.readline())
            if uname in lessondic:
                for i in lessondic[uname]:
                    print(i)
            else:
                print("%s没有选择课程")

def main():
    print("欢迎登录选课系统")
    while True:
        print("""
              1:登录
              2:注册
              3:退出
        """)
        c=input("请输入您的选择:")
        if c == "1":
            logging()
        elif c == "2":
            enroll()
        elif c == "3":
            break
        else:
            print("无效的选择!请重新输入!")

if __name__ == '__main__':
    main()

