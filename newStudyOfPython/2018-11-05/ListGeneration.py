#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-05 9:59
#!@Filename:ListGeneration.py


#学习列表生成式

"""现在有个需求，看列表[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],我要求你把列表里的每个值加1"""
a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b=[]
#第一种方式
for i in a:
    b.append(i+1)
print(b)

#第二种
c=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a=c
print("-------------")
print(a)

#第三种原值修改

for index,i in enumerate(a):
    print(index)
    print(i)
    a[index] += 1
print("第三种：")
print(a)

#第四种，列表生成式

_a=[i+1 for i in range(10)]
print(_a)

L=[i * i for i in range(10)]#列表
print(L)
G=(i * i for i in range(10))#生成器
print(G)
# print(next(G)) 很少用next()方法
# print(next(G))  一般使用的是for循环
# print(next(G))
# print(next(G))
# print(next(G))
for i in G:
    print(i)

