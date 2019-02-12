def str(content):
    print('******************',content,'************************')
def str1():
    print('**************************************************')
def str2(heroname):
    print('恭喜你，成功选择了',heroname)
#英雄介绍界面
def thero():
    print('欢迎',hname,'来到英雄介绍界面')
    str('吕布')
    str('刘备')
    str('张飞')
    str('关于')
#英雄选择界面
def chero():
    print('欢迎',hname,'来到英雄选择界面')
    str('英雄列表')
    str('1:吕布')
    str('2:刘备')
    str('3:张飞')
    str('4:关羽')
    str('请输入你想建立的英雄角色的序号')
    heronum=int(input('序号:'))
    if heronum==1:
        heroname='吕布'
        str2(heroname)
        heroatt(heronum)
    elif heronum==2:
        heroname='刘备'
        str2(heroname)
        heroatt(heronum)
    elif heronum==3:
        heroname='张飞'
        str2(heroname)
        heroatt(heronum)
    elif heronum==4:
        heroname='关羽'
        str2(heroname)
        heroatt(heronum)
def str3(hp,att,df,spe):
    str('其属性如下所示：')
    print('血量：',hp)
    print('攻击力:',att)
    print('防御：',df)
    print('速度：',spe)
    
#英雄属性界面
def heroatt(heronum):
    if heronum==1:
        str3(lvbu[0],lvbu[1],lvbu[2],lvbu[3])
    elif heronum==2:
        str3(liubei[0],liubei[1],liubei[2],liubei[3])
    elif heronum==3:
        str3(zhangfei[0],zhangfei[1],zhangfei[2],zhangfei[3])
    elif heronum==4:
        str3(guanyu[0],guanyu[1],guanyu[2],guanyu[3])
      
            
'''
英雄初始化属性列表：血量，攻击力，防御，速度
HP MAX:1OO
ATT MAX:10
DEF MAX:100
SPE MAX:10
'''
lvbu=[80,8,70,5]
liubei=[70,7,60,7]
zhangfei=[98,5,90,6]
guanyu=[80,7,76,8]
##################################################################
str('欢迎来到三国无双')
str('请输入你的召唤师名称')
hname=input('名称：')
if hname=='':
    hname='游客玩家'
    print('恭喜',hname,'成功建立角色')
else:
    print('恭喜玩家',hname,'成功建立角色')
str('进入英雄介绍界面输入1，进入英雄选择界面输入2')
num=int(input('选择：'))
if num==1:
    thero()
    str('输入end，进入英雄选择界面')
    cc=input('选择:')
    if cc=='end':
        chero()
elif num==2:
    chero()
str('确认选择输入1，重新选择输入2')
bo = int(input('选择：'))
if bo == 1:
    print('欢迎',hname,'来到三国无双世界')
elif bo == 2:
    chero()
    str('输入end，进入游戏界面')
    cc=input('选择:')
    if cc=='end':
        print('欢迎',hname,'来到三国无双世界')            
else:
    str('输入错误！！！！请重新输入')
    chero()
    
    

    
    

