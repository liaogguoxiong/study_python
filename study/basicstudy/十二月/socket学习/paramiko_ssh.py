#时间：    2019/1/15 22:29
#作者：    lgx
#文件名：  paramikoDemo

'''
今天来学习paramiko模块,
该模块基于ssh用于连接远程服务器并执行相关操作
'''

import paramiko

#调用paramilo中的SSHClient类.创建ssh对象
ssh=paramiko.SSHClient()
#如果know_hosts中没有要连接的主机,就自动添加进去
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#和远程主机连接,输入主机名,端口号,用户名和密码
ssh.connect(hostname='192.168.235.128',port=22,
            username='root',password='li@o0121')
#输入命令之后,服务器可能返回三个结果,标准输入,标准输出,标准错误
#标准输出和标准错误只会输出一个
stdin,stdout,stderr=ssh.exec_command("pwd")
res=stdout.read()
print(res.decode())
ssh.close()