#时间：    2019/1/16 20:17
#作者：    lgx
#文件名：  paramiko_sftp
'''
使用paramiko模块来做ftp服务器
'''
import os
import paramiko
import tkinter
import tkinter.filedialog
#调用paramiko中的Transport类,创建对象
transport=paramiko.Transport(('192.168.235.128',22))
#建立链接通道
transport.connect(username="root",password="li@o0121")
#真正的传输使用的SFTPClient
sftp=paramiko.SFTPClient.from_transport(transport)

default_path=r"文件路径"
# fname=tkinter.filedialog.askopenfilename(title=u'选择要传送的文件',
#             initialdir=(os.path.expanduser((default_path))))
#传文件,传的文件需要重新命名
#sftp.put(fname,"/root/test")
#用弹窗的方式来确定保存路径
save_path=tkinter.filedialog.asksaveasfilename(title=u"选择保存文件的路径",
                                               initialdir=(os.path.expanduser(default_path)))
sftp.get("/root/pythonCode/socket_ssh_client.py",save_path)


transport.close()