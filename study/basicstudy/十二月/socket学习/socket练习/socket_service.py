#时间：    2018/12/26 21:15
#作者：    lgx
#文件名：  socket_service
'''
这个服务端的代码,一般来说,
先有服务端再有客户端,如果没有
服务端,客户端的请求没有响应,
服务端监听,如果有客户端的请求,则
响应,也可以发送数据给客户端
'''
import socket
#规定使用的协议,可以默认
service=socket.socket()
#先绑定监听端口,也就是监听那个端口
service.bind(('localhost',6969))
#开始监听
service.listen()
print("服务器开始监听")
#等待,service.accept()这样写的话
#代表只能够接受一个客户端的请求连接,
#如果有多个客户端请求,就会出错,
#service.accept()会返回一个实例对象
#和一个地址,这样就可以识别不同的客户端了
#conn就是客户端连接过来而服务器为其生成
#的一个连接实例,有多少个客户端连接,就生成多少实例
#就不要用service.accept(),它只能建立一个实例

conn,addr=service.accept()
print("连接建立了!!!")
while True:
    #限定接收数据的大小
    data=conn.recv(1024)
    print("接受的数据为:",data.decode())
    #发送数据
    conn.send(data.upper())


service.close()