class MyOwnErr(ZeroDivisionError):
    pass


try:
    b = int(input('Введите числитель: '))
    c = int(input('Введите знаменатель: '))
    if c == 0:
        raise MyOwnErr('Деление на 0')
    a = b / c
except MyOwnErr as e:
    print(e)
else:
    print(a)
finally:
    print('The end')
