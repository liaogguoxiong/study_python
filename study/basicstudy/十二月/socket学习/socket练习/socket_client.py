#时间：    2018/12/26 20:56
#作者：    lgx
#文件名：  socket_client

'''
socket把各种协议封装起来,然后提供
发送信息和接受信息的功能

'''

#这是客户端代码
import socket
#声明socket类型,并生成socket连接对象
client=socket.socket()
#连接的ip地址和端口
client.connect(('localhost',6969))
#发送数据,中文变成unicode需要编码(encode)并且加上原编码
client.send('向服务器发出请求'.encode("utf-8"))
#接收数据,并限定接收数据的大小为1kb
data=client.recv(1024)
print("接收的数据为:",data.decode())
client.close()