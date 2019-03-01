# @Author  :lgx
# @Time    :2019/2/18 22:28
# @File    :全局锁.py

'''
多线程执行的时候,公用一个数据的话
可能会造成数据错误.比如2个线程调用一个
全局变量,第一个线程没有返回全局变量,第二个
线程就开始调用全局变量,调用的是最开始的变量,
而不是第一个线程返回的变量,可能会导致出错.
所以需要一个锁来把变量锁住,别的线程调用的时候,
另外的线程不得调用
'''
import threading

num=0
t_list=[]
glock=threading.Lock()  #声明全局变量锁
def add_num():
    global num          #声明成全局变量,否则是局部变量
    #glock.acquire()     #对变量上锁
    num +=1
    #time.sleep(1)
    #glock.release()     #对变量解锁
    print(num)
def main():
    global num
    for i in range(10):
        t=threading.Thread(target=add_num)
        t.start()
        #t_list.append(t)
    # for i in t_list:
    #     i.join()
    print(num)
if __name__ == '__main__':
    main()