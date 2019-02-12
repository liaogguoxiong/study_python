#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-29 14:14
#!@Filename:Preview.py

'''
讲解非面对对象方法的缺点,
'''

def person(name,age,sex,job):
    data = {
        'name':name,
        'age':age,
        'sex':sex,
        'job':job
    }
    return data

def dog(name,dog_type):
    data = {
        'name':name,
        'type':dog_type
    }
    return data

def bark(d):
    print("dog %s:wang wang wang "%d['name'])

def walk(p):
    print("person %s is walking..." %p['name'])


d1 = dog("李磊", "京巴") #实例化

p1 = person("严帅", 36, "F", "运维")

p2 = person("林海峰", 27, "F", "Teacher")


walk(p1)
bark(d1)
bark(p1)#人调用了狗的方法