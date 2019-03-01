import getpass
name="lgx"
pw="liao0121"
i=0
uname=input("please input your name:")
if uname==name:
    while i < 3:
        i+=1
        upw=getpass.getpass("please input your passwd:")
        if upw==pw:
            print("Welcome to my system!!!!")
            break
        else:
            print("your passws is mistake!please input again and your only have %s chances".format((3-i)))
    print("your account is locked")
        
else:
    print("your username is mistake and yout have 2 chances!!!")

