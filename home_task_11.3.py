import re


class MyOwnErr(Exception):
    list_num = []

    @staticmethod
    def __init__(number):
        if re.search(r'^\d+$|^\d+.\d+$', number):
            MyOwnErr.list_num.append(number)
        elif number == 'stop':
            print(MyOwnErr.list_num)
            exit()
        else:
            print('Введено не число')


while True:
    MyOwnErr(input('Введите число: '))
