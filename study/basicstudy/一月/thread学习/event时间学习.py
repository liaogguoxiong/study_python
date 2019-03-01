# @Author  :lgx
# @Time    :2019/2/20 23:19
# @File    :event时间学习.py
'''
红绿灯实例,绿灯亮20s,红灯亮10s.
0-20s为绿灯,20-30s为红灯
'''
import threading
import time
event=threading.Event()
def light():
    count = 1
    event.set()    #开始就是绿灯
    while True:
        if count > 20 and count <= 30:   #红灯
            event.clear()
            print("\033[41;1m(红灯===>>%d)\033[0m"%(30-count))
        elif count > 30:  #绿灯
            event.set()
            count=0

        else:
            print("\033[42;1m(绿灯===>>%d)\033[0m" % (20 - count))
        time.sleep(1)
        count +=1
def car(name):
    while True:
        if event.is_set():
            print("现在是绿灯,%s可以通行"%(name))
        else:
            print("现在是红灯,%s不可以通行" %(name))
        time.sleep(1)

def main():
    t=threading.Thread(target=light,)
    t.start()
    car1=threading.Thread(target=car,args=("大众",))
    car1.start()
if __name__ == '__main__':
    main()