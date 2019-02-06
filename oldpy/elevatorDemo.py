def str():
    print('###################################################')
def str1(cont):
    print('***********',cont,'**************')
def str2(num):
    print('现在电梯在',num,'层')
    str()
def run(num):
    elenum=[1,2,3,4]
    for i in elenum:
                if i == num:
                    print(num,'楼到了')
                    break
                str2(i)
                time.sleep(2)
    
    
import time
str1('欢迎来到摩天电梯')
str()
elenum=[1,2,3,4]
for i in elenum:
    str2(i)
    time.sleep(0)
str()
print('请输入y,进行搭乘')
str()
c=input('选择：')
str()
if c=='y':
    print('请稍等，电梯正在下行')
str()
for j in reversed(elenum):
    str2(j)
    time.sleep(0)
print('电梯已到达，欢迎搭载')
num=int(input('请输入要到达的层数：'))
run(num)

    
    
    
