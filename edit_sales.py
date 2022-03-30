import sys

command = sys.argv

with open('bakery.csv', 'r+', encoding='utf-8') as f1, open('bakery_cursor.csv', encoding='utf-8') as f2:
    cursor = [i.strip() for i in f2]
    for i in range(len(cursor)):
        f1.seek(int(cursor[i]))
        a = f1.readline()
        if a.strip() == command[1]:
            f1.seek(int(cursor[i]))
            f1.write(command[2])
            sys.exit()

# остаток первого числа сохранился, не смог исправить