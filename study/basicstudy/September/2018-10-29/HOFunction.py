#High order function 高阶函数
def add (a,b,f):#其中a,b为参数，f为函数
    return f(a)+f(b)#f为函数，而a，b作为f的参数传入
sum=add(1,-5,abs)#其中abs是当作参数参数add函数，abs是绝对值函数
print(sum)

