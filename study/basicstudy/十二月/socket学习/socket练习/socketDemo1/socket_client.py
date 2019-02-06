#时间：    2019/1/2 22:18
#作者：    lgx
#文件名：  socket_client
import socket
client=socket.socket()
client.connect(('localhost',8888))
r_data=client.recv(1024)
print(r_data.decode())
while True:
    s_data=input("客户端>>>>")
    client.send(s_data.encode('utf-8'))
    r_data = client.recv(1024)
    print("服务器>>>>%s" % r_data.decode())





client.close()