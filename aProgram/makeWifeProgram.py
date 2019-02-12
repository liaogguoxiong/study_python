#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-27 15:25
#!@Filename:makeWifeProgram.py
'''
一个随机生成各种参数的小功能
'''

import random

def randomWife():
    _bodycolor = bodycolor[random.randint(0, 2)]
    _hairtype = hairtype[random.randint(0, 3)]
    _haircolor = haircolor[random.randint(0, 4)]
    _eyescolor = eyescolor[random.randint(0, 2)]
    _jobs = jobs[random.randint(0, 4)]
    _character = character[random.randint(0, 3)]
    _superpower = superpower[random.randint(0, 3)]
    output = '''
           身高:%dcm
           体重:%d斤
           腹肌:%d块
           SIZE:%dcm
           肤色:%s
           发型:%s
           发色:%s
           瞳色:%s
           工作:%s
           性格:%s
           超能力:%s       
           ''' % (random.randint(170, 190), random.randint(120, 180), random.randint(0, 8),
                  random.randint(10, 20), _bodycolor, _hairtype, _haircolor, _eyescolor, _jobs,
                  _character, _superpower
                  )
    print(output)

bodycolor=['白色','黑色','黄色']
hairtype=['平头','圆寸','飞机头','光头']
haircolor=['白色','黑色','黄色','绿色','奶奶灰']
eyescolor=['黑色','金瞳色','蓝色']
jobs=['IT男','医生','警察','农民','教师']
character=['温和','霸道','懦弱','呆呆']
superpower=['透视','读心术','第六感','想得美']

print('''
#############################################################
#                                                           #
#           欢迎来玩一键制作老公生成器v1.0                   #                                
#                                                           #
#############################################################
'''.strip())
print('''
##########################  y:开始玩  ##########################
##########################  n:退出游戏  ##########################
    ''')
ch=input("请输入您的选择:")
while True:
    if ch == 'y':
        randomWife()
        print('''
        ##########################  n:退出游戏  ##########################
        ##########################  y:继续玩  ##########################
            ''')
        ch=input('请输入您的选择:')
        continue
    elif ch == 'n':
        print("游戏结束,谢谢!!!!")
        exit()
    else:
        ch=input("无效的选择!请重新输入:")
        continue






