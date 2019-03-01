#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-28 16:27
#!@Filename:gameOfSanGong.py

'''
小时候常玩的游戏三公
'''
import random
game1=0
game2=0
count1=0
count2=0
count=0
sum1=0
sum2=0
kase=random.randint(1,13)
print("卡色的牌是%d"%kase)
if kase%2 == 1:
    print("先拿牌的是玩家1")
    for i in range(6):
        count +=1
        if count % 2 ==1:
            count1 +=1
            p1=random.randint(1,13)
            print("玩家1的第%d张牌是%d"%(count1,p1))
            if p1 > 10:
                p1=10
                sum1 +=count1
        else:
            count2 +=1
            p2 = random.randint(1, 13)
            print("玩家2的第%d张牌是%d" %(count2,p2))
            if p2 > 10:
                p2=10
                sum2 +=count1

    print("玩家1的点数为%d" % (sum1 % 10))
    print("玩家2的点数为%d" % (sum2 % 10))
    if sum1 >= sum2 :
        print("玩家1获胜!!!")
    else:
        print("玩家2获胜!!!")
else:
    print("先拿牌的是玩家2")
    for i in range(6):
        count +=1
        if count % 2 ==1:
            count2 +=1
            p2=random.randint(1,13)
            print("玩家2的第%d张牌是%d"%(count2,p2))
            if p2 > 10:
                p2=10
                sum2 +=count1
        else:
            count1 +=1
            p1 = random.randint(1, 13)
            print("玩家1的第%d张牌是%d" %(count1,p1))
            if p1 > 10:
                p1=10
                sum1 +=count1
    print("玩家2的点数为%d" % (sum2 % 10))
    print("玩家1的点数为%d" % (sum1 % 10))
    if sum2 >= sum1 :
        print("玩家2获胜!!!")
    else:
        print("玩家1获胜!!!")