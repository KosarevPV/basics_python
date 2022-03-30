import sys

with open('hobby.csv', encoding='utf-8') as f1, open('users.csv', encoding='utf-8') as f2:
    with open('users_hobby.txt', 'w+', encoding='utf-8') as f3:
        for user in f2:
            hobby = f1.readline()
            if hobby and hobby[-1] == '\n' and user[-1] != '\n':
                f3.writelines('{a}: {b}{c}'.format(a=user.strip('\n'), b=hobby.strip('\n'), c='\n'))
                sys.exit(1)
            elif hobby:
                f3.writelines('{a}: {b}{c}'.format(a=user.strip('\n'), b=hobby.strip('\n'), c='\n'))
            else:
                f3.writelines('{a}: None{c}'.format(a=user.strip('\n'), c='\n'))
