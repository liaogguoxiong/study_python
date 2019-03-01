#本次学习的是集合
list_1=[1,2,3,4,5,3,1,9]
list_2=[1,3,4,5,9]
list_3=['a','b']
list_1=set(list_1)#把列表变成集合,去重
list_2=set(list_2)
list_3=set(list_3)
print(list_1,type(list_1))
print(list_1.intersection(list_2))#交集
print(list_2 & list_1)#交集
print(list_1.union(list_2))#并集
print(list_2 | list_1)#并集
print(list_1.difference(list_2))#差集,list1有,list2没有的叫差集
print(list_1 - list_2)#差集
print(list_1.issubset(list_2))#判断list1是不是list2的子集
print(list_1.issuperset(list_2))#判断list1是不是list2的子集
print(list_1.symmetric_difference(list_2))#对称差集,输出list1和list2都不共有的
print(list_2 ^ list_1)
print('_____',list_1.isdisjoint(list_3))#如果二个列表没有交集则返回true
'''
集合的操作
'''
#增加
list_1.add(10)
print(list_1)
#增加多个
list_1.update([11,12,13])
print(list_1)
#删除
list_1.remove(13)
print(list_1)
#随机删除
list_1.pop()
print(list_1)
#删除集合中不存在的数据,不会报错,erremove会
print(list_1.discard(8888))
#测试某个值是不是集合中的
print(9 in list_1)
#集合的长度
print(list_1.__len__()  )

