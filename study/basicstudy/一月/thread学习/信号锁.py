# @Author  :lgx
# @Time    :2019/2/18 23:23
# @File    :信号锁.py

import threading
import time

def num(n):
    semaphore.acquire()
    time.sleep(1)
    print("我是线程",n)
    semaphore.release()
if __name__ == '__main__':
    semaphore=threading.BoundedSemaphore(5)    #最多运行5个线程同时执行
    for i in range(20):
        t=threading.Thread(target=num,args=(i,))
        t.start()

while threading.active_count() != 1:
    pass
else:
    print("程序结束")