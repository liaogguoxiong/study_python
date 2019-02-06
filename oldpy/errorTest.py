#判断输入的是不是一个正数，如果不是继续输入
while True:
    try:
        x=int(input('Please enter a int number:'))
        break
    except ValueError:
        print('Oops! That was no valid number.Try again')
