import sys
list=[1,2,3,4]
#iter迭代器
it=iter(list)
while True:
    try:
        print(next(it))
    #如果没有数值，则退出
    except  StopIteration:
        sys.exit()
