'''
Program:介绍if-else流程
History：lgx     2018-10-14      First release
'''
f=open("test","r",encoding="utf-8")
#_username="lgx"
#_passwd="hello"
username=f.readline()
print(username)
"""
username = input("username:")
#pw=getpass.getpass("passwd:") #密文
pw=input("passwd:")            #明文
print(username,pw)
if username==_username and _passwd==pw:
    print("Welcome user \"{user}\" logining.....".format(user=username))
else:
    print("Invalid username or passwd!")
"""