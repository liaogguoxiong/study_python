# @Author  :lgx
# @Time    :2019/1/31 22:33
# @File    :守护线程.py

'''
守护线程是为主线程服务的,如果主线程结束了,
则守护进程也结束了.在threading基础中的例子,
主线程结束了,但是其他线程不是守护线程,所以
还在执行
'''
import threading
import time
def test(n):
    n=int(n)
    time.sleep(2)
    print('我是线程%d'%n)

#创建十个线程来运行
for i in range(10):
    t=threading.Thread(target=test,args=('%d'%i,))
    #把这十个线程设置为守护线程
    t.setDaemon(True)
    t.start()

time.sleep(1)
print('main threading is over')