while True:
    try:
        x=int(input('Please enter a int number:'))
        break
    except ValueError:
        print('Oops! That was no valid number.Try again')
