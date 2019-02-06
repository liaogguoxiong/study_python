#时间：    2019/1/8 18:57
#作者：    lgx
#文件名：  sshService
'''
做一个ssh器,客户端输入命令
服务器返回结果
'''
import os
import socket
service=socket.socket()
service.bind(('localhost',9627))
service.listen()
print('服务器监听中.....')
while True:
    conn,addr=service.accept()
    print("客户端的ip地址为:",addr)
    conn.send("连接服务器成功".encode())
    while True:
        print("接受新的指令.....")
        recv_data=conn.recv(1024)
        if not recv_data:
            print("客户端已经断开")
            break;
        res=os.popen(recv_data.decode()).read()
        if len(res)==0:
            res="无效的命令"
        conn.send(str(len(res)).encode())
        conn.send(res.encode())
        print("命令%s结果的长度为%s"%(recv_data.decode(),len(res)))
        # print('命令%s结果返回成功'%recv_data.decode())
        print("结果返回完毕")
    conn.close()