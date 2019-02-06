#时间：    2019/1/8 19:03
#作者：    lgx
#文件名：  sshClient
import socket
client=socket.socket()
client.connect(('192.168.235.128',9627))
data_recv=client.recv(1024)
print(data_recv.decode())
while True:
    cmd_s=input('>>:')
    if len(cmd_s)==0:continue
    if cmd_s == 'q':break
    client.send(cmd_s.encode('utf-8'))
    res_size=client.recv(1024)
    print(res_size.decode())
    res_size=int(res_size.decode())
    recv_size=0
    data=''
    while res_size > recv_size:
        res_data=client.recv(1024)
        if len(res_data.decode())==0:continue
        print(len(res_data.decode()))
        data +=res_data.decode()
        recv_size += len(res_data.decode())
    print(data)
    print("返回结果接收完毕!!")
client.close()