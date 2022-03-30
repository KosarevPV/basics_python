import sys

command = sys.argv

with open('bakery.csv', encoding='utf-8') as f1, open('bakery_cursor.csv', encoding='utf-8') as f2:
    if len(command) == 1:
        print(f1.read())
    elif len(command) == 2:
        cursor = [i.strip() for i in f2]
        f1.seek(int(cursor[int(command[1]) - 1]))
        print(f1.read())
    elif len(command) == 3:
        cursor = [i.strip() for i in f2]
        for i in range(int(command[1]), int(command[2])):
            f1.seek(int(cursor[i - 1]))
            print(f1.readline(), end='')
    else:
        print('Подсказка:'
              ' 1)просто запуск скрипта — выводить все записи'
              ' 2)запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца'
              ' 3)запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.')
