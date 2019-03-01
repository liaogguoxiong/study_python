#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-10-31 16:36
#!@Filename:studyOfList.py
#列表的操作

name_list=["alex","lgx","zsy","wyl"]
#列表的增操作
name_list.append("dakuxiong")#插入，只能插入在列表的最后面
name_list.insert(0,"dayan")#可以指定插入的位置
print(name_list)
age_list=[10,20,30,40]
#列表的删操作
name_list.pop()#删除最后一个，如果list为空则会报错
name_list.remove("alex")#删除指定的列表中的元素
del name_list[0]
name_list.reverse()#反转列表，即列表中元素的位置反过来
print(name_list)

#列表的查操作

print(age_list)#打印整个列表
print(age_list[0])#按照索引来查找列表
print(age_list[0:3])#欺骗

#列表的改操作
age_list[0]=88
print(age_list)

#列表的循环输出

for l in name_list:
    print(l)
print("_________________")
for l_1 in name_list[0:3]:  #指定要循环几个
    print(l_1)

#判断一个元素是否在列表中

if "lgx" in name_list:
    print("lgx是我们的老大")

#列表合
print("------------")
name_list.extend(age_list)
print(name_list)

#拷贝
cp_name=name_list.copy()
print(name_list)
print(cp_name)
name_list[0]="liaoguoxiong"
print(name_list)
print(cp_name)