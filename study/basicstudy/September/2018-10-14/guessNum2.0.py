'''
Program:猜字谜，每个玩家一次有三次机会，用完机会后程序会提示是否继续玩，输入n结束游戏。
Hitory：lgx      2018-10-14      第二个版本
'''
count=0
_kw=8 #keyword
while (count < 3):
    kw=int(input("请输入您想猜的整数数字，在1-10之间："))
    if kw > 10 or kw < 1:
        print("您输入的数字不在范围内")
        count+=1
        continue
    elif _kw==kw:
        print("恭喜您猜对了！！！！")
        exit(0)
    elif _kw > kw:
        print("您猜的数字小了,您还有{counts}次机会".format(counts=2-count))
    else:
        print("您猜的数字大了,您还有{counts}次机会".format(counts=2-count))
    count+=1
    if count==3:
        print("您的机会已经用完了，是否继续玩，如果不玩输入n结束游戏，按任意键继续游戏")
        ck=input("confirmKey:") #confirmKey 确认码
        if ck !="n":
            count=0 #重置机会次数，本来是3的，重置为0
            print("--------继续游戏-------")
        else:
            print("------游戏结束-------")





