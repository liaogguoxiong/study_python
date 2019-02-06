#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-29 15:45
#!@Filename:test1.py

'''
开始接触面对对象,实例化和封装
'''
hurtValues={
        "ak47":20,
        'm47':15,
        "m51":10

}
class Role(object):
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name=name
        self.role=role
        self.weapon=weapon
        self.life_value=life_value
        self.money=money
    def shot(self):
        print('shooting..............')

    def got_shot(self,gunName):
        if gunName in hurtValues:
            self.life_value -=hurtValues[gunName]
        print('%s go a shot by %s,life value is %d'%(self.name,gunName,self.life_value))

    def buy_gun(self):
        print('i buy a gun')

    def __del__(self):
        print("it is dead")
r1=Role('xiaoming','police','ak47')
r2=Role('xiaocai','terrorist','m47')
r1.got_shot('m51')
del r1
r1.got_shot('m51')
