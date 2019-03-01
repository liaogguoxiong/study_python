#时间：    2018/11/15 22:37
#作者：    lgx
#文件名：  MultiThreading

#今天来学习多线程

import threading
import random
import time

MONEY=0#需要加上全局锁
gLock=threading.Lock()

def producter():
    global MONEY
    while True:
        time.sleep(0.5)
        produ=random.randint(10,100)
        print("公司盈利了%d元"%produ)
        gLock.acquire()
        MONEY=MONEY+produ
        gLock.release()
        print("公司的账户余额有:%d元"%MONEY)
def customer():
    global MONEY
    while True:
        time.sleep(0.5)
        global MONEY
        cust=random.randint(10,100)
        gLock.acquire()
        if MONEY < cust:
            gLock.release()
            print("公司余额不足,请稍等")

        else:
            print("公司支出了%d元"%cust)
            MONEY=MONEY-cust
            gLock.release()
            print("公司的账户余额为:%d"%MONEY)
def main():
#使用5个线程来生成钱
    for x in range(3):
        th=threading.Thread(target=producter)
        th.start()
#使用3个线程来消耗钱
    for x  in range(5):
        th=threading.Thread(target=customer)
        th.start()
if __name__ == '__main__':#表明这是主函数,不是被调用的函数
    main()


