#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-01 14:56
#!@Filename:homework2.py

"""
~~~多级菜单
1.三级菜单
2.可依次选择进入各子菜单
3.所需新知识点：列表、字典

"""
muen={
    "广西":{"南宁":{"宾阳县":["新宾镇","芦圩镇"]}},
    "广东":{"深圳":{"龙华":["沙元埔"]}},
}
print("----------欢迎来到城市查看系统-----------")
while True:
    for m1 in muen:
        print(m1)
    c1=input("请输入您的选择：")
    if c1 in muen:
        while True:
            for m2 in muen[c1]:
                print(m2)
            c2 = input("请输入您的选择：")
            if c2 in muen[c1]:
                while True:
                    for m3 in muen[c1][c2]:
                        print(m3)
                    c3 = input("请输入您的选择：")
                    if c3 in muen[c1][c2]:
                        while True:
                            for m4 in muen[c1][c2][c3]:
                                print(m4)
                            c4 = input("请输入您的选择：")
                            if c4 == "q":
                                print("您选择了退出程序")
                                exit()
                            elif c4 == "b":
                                print("您选择了返回上一级")
                                break
                            else:
                                print("无效的命令，请重新输入:")
                    elif c3 == "b":
                        print("您选择了返回上一级！！")
                        break
                    elif c3 == "q":
                        print("您选择了退出程序！")
                        exit()
                    else:
                        print("无效的命令，请重新输入")
            elif c2 == "b":
                print("您选择了返回上一级！！")
                break
            elif c2 == "q":
                print("您选择了退出程序！")
                exit()
            else:
                print("无效的命令，请重新输入")
    elif c1 == "q":
        print("您选择了退出程序！")
        exit()
    else:
        print("无效的命令，请重新输入")