#学习字典
info = {
    'stu1':'lgx',
    'stu2':'zsy',
    'stu3':'GGbond'
}
'''查操作
'''
#第一种
print(info['stu1'])
#第二种
print(info.get('stu2'))#建议使用这种方法，因为如果key是不存在的，第一种会报错，而第二种不会
print(info.get('hello'))
#判断key是否在字典中
print('stu1' in info)

'''
增操作
'''
info['stu4']='dababab'
print(info)

'''
删操作
'''
#第一种
del info['stu1']
print(info)
#第二种
info.pop('stu2')
print(info)
#第三种
#info.popitem()#随机删除
print(info)
'''
改操作
'''
info['stu4']='lgx'
print(info)
