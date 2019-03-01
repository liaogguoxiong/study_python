#时间：    2019/1/2 22:06
#作者：    lgx
#文件名：  socket_service
'''
写一个简单的计算器,客户端负责输入
服务端返回结果
'''
import socket
#wordList=["虎虎生威","卓尔不凡","小赌怡情"]
service=socket.socket()
service.bind(('localhost',8888))
print("连接中.......")
service.listen()
conn,addr=service.accept()
conn.send('连接服务器成功'.encode('utf-8'))
print("客户端连接成功.......")
while True:
    r_data=conn.recv(1024)
    r_data=r_data.decode()
    print("客户端>>>>%s"%r_data)
    s_data=input("服务端>>>>")
    conn.send(s_data.encode("utf-8"))
    # for word in wordList:
    #     if r_data in word:
    #         conn.send(word.encode('utf-8'))
    #     else:
    #         conn.send("词库中无包含此关键词的成语!!!".encode())

service.close()