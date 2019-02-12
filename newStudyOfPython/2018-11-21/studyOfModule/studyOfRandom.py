#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-21 14:54
#!@Filename:studyOfRandom.py

import random
import time
# while True:
#      time.sleep(1)
#      #print(random.randint(1,2))#随机生成1和2的随机数
#      print(random.randrange(0,4))

# '''
# 生成4位数的验证码
# '''
# checkcode=''
# for i in range(4):
#     num=random.randint(0,9)
#     checkcode +=str (num)
# print(checkcode)

'''
另一个生成随机验证码的方法
'''
checkcode=''
for i in range(4):
    current=random.randint(0,4)
    if current != i:
        temp=chr(random.randint(65,90))#获取大写字母
    else:
        temp=random.randint(0,9)
    checkcode += str(temp)
print(checkcode)
