#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-22 13:49
#!@Filename:studyOfParamiko.py

import paramiko
'''
paramiko是一个用于做远程控制的模块，使用该模块可以对远程服务器进行命令或文件操作，
值得一说的是，fabric和ansible内部的远程管理就是使用的paramiko来现实。

'''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.128',22,'lgx','liao0121')
stdin,stdout,stderr=ssh.exec_command('df')
print (stdout.read())
ssh.close()

