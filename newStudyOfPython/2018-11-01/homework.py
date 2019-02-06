# #！/usr/bin/env python
# #！@Author：lgx
# #！@时间：2018-11-01 13:40
# #!@Filename:homework.py
# """
# 作业二：编写登陆接口
#
# 1.输入用户名密码
# 2.认证成功后显示欢迎信息
# 3.输错三次后锁定
#
#
# """
# username="lgx"
# psw="liao0121"
# i=0
# j=0
#
# while i < 10:
#     i+=1
#     _username=input("please input your username:")
#     if _username ==username:
#         while j < 3:
#             j+=1
#             _pwd=input("please input your passwd:")
#             if _pwd == psw:
#                 print("welcome to our system.....")
#                 break
#             else:
#                 print("invail passwd,please input again,you have %s change." % (3 - j))
#                 if j == 3:
#                     with open('homeworkTest', 'a', 'utf-8') as f:
#                         f.append(_username)
#                         print("%s had been locked!!"%_username)
#                         break
#     elif _username in lockeduser:
#         print("your account is locked")
#     else:
#         print("invail username,please input again,you have %s change."%(10-i))
#

'''
上面的是刚开始学习的时候学的，
下面的是学了一段时间之后写的
'''

# 作业二：编写登陆接口
#
# 1.输入用户名密码
# 2.认证成功后显示欢迎信息
# 3.输错三次后锁定
#
#
# """

