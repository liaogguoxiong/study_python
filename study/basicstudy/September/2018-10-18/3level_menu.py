#Program:制作一个三级菜单,能够逐级进入和退出,以及在每级菜单都能够退出
#History:lgx    2018/10/19      First release
game={
    'grandfather':{"father":{"son":'他们是一家人'}}
}
while True:
    for i in game:
        print(i)
    choice1=input("---------请输入您的选择-----------:")
    if choice1 == 'q':
        exit()
    elif choice1 in game:
        while True:
            for j in game[choice1]:
                print("\t\t",j)
            choice2 = input("---------请输入您的选择-----------:")
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit()
            elif choice2 in game[choice1]:
                while True:
                    for k in game[choice1][choice2]:
                        print(k)
                    choice3 = input("---------请输入您的选择-----------:")
                    if choice3 in game[choice1][choice2]:
                        print(game[choice1][choice2][choice3])
                    elif choice3 == 'b':
                        pass
                    elif choice3 == 'q':
                        exit()
                    else:
                        print("无效的操纵!!!!!!")
            else:
                print("无效的操纵!!!!!!")
    else:
        print("无效的操纵!!!!!!")