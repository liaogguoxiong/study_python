#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-10-31 17:21
#!@Filename:studyOfDictionary.py
#字典，无序的，不可重复的

stu_dic={"name":"lgx","stu_num":1400360117,"school":"guet"}
print(stu_dic)
for stu in stu_dic: #循环输出，输出的是键。
    print(stu_dic[stu])
#字典靠键来查找数据
print(stu_dic["name"])

#字典的嵌套
stu={"1400360117":['lgx',"wanglgongcheng"]}
stu1={"1400360117":{"lgx":"wangluogongc"}}
