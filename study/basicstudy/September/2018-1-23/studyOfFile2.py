#今天继续学习文件的知识
#2018年10月23日 22:59:37
import sys,time
f=open('study','a',encoding='utf-8')
'''
#实时刷新,写入内容到文件的时候,并不是实时写入的,因为这样会造成卡顿.所以
会先把内容写入一个缓存区,等缓存区满了之后再写入文件中,
而f.flush()方法就是把缓存区的内容实时写入而不用等待缓存区满了再写入
'''
f.flush()

'''
使用f.flush实时刷新做有一个进度条

print("进度条:")
for i in range(20):
    sys.stdout.write("*")#标准输入,write就相当于写入屏幕
    sys.stdout.flush()#
    time.sleep(0.5)
'''
f.truncate(10)#括号里面填数字,代表保留从0字符到此字符之间的内容,其他的删除.需要改为a模式
