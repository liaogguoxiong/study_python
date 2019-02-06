#时间：    2018/12/27 20:50
#作者：    lgx
#文件名：  socket_client2
'''
客户端不断向客户发送信息
'''
import socket
client=socket.socket()
client.connect(('localhost', 6969))
while True:
    s_date=input("send>>>")
    client.send(s_date.encode("utf-8"))
    r_date=client.recv(1024)
    print("recv>>",r_date.decode())
client.close()