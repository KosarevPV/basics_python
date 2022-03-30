import sys

command = sys.argv

with open('bakery.csv', 'a', encoding='utf-8') as f1, open('bakery_cursor.csv', 'a', encoding='utf-8') as f2:
    f2.write(str(f1.tell()))
    f2.write('\n')
    f1.write(command[1])
    f1.write('\n')
