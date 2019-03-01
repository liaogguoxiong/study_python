#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-14 11:31
#!@Filename:threadTest.py
import threading
import time


def test():
    # startTime=time.time()

    time.sleep(0.5)
    print("hello,ni hao")
    # endTime=time.time()
    # runTime=endTime-endTime
    # print(runTime)
def threadtest():
    for i in range(3):
        th=threading.Thread(target=test)
        th.start()
threadtest()

