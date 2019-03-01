# @Author  :lgx
# @Time    :2019/1/28 22:52
# @File    :threading基础.py

import threading
import time
def run(n):
    print('task',n,threading.current_thread())
    time.sleep(2)

###############################################
'''
t1=threading.Thread(target=run,args=('t1',))
t2=threading.Thread(target=run,args=('t2',))
t1.start()
t2.start()
'''
################################################
t_objs=[]
s_time=time.time()
for i in range(50):
    t=threading.Thread(target=run,args=('%d'%i,))
    t.start()
    t_objs.append(t)
for t in t_objs:
    #等待线程执行完毕
    t.join()
end_time=time.time()
print("运行时间%s"%(end_time-s_time),threading.current_thread())
print(threading.active_count())


