#今天来学习递归，递归就是函数自己调用自己本身
#2018年10月29日 21:38:16   lgx

def recursion_test(n):
    print(n)
    if int (n) < 10 :
        return recursion_test(int(n*2))
    print("递归结束啦~~~~~")


n=int(input("please input a num:"))
recursion_test(n)

