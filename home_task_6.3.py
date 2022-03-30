import json
import sys
from itertools import zip_longest

with open('hobby.csv', encoding='utf-8') as f1, open('users.csv', encoding='utf-8') as f2:
    with open('info.json', 'w+', encoding='utf-8') as f3:
        hobbys = f1.read().split('\n')
        users = f2.read().replace(',', ' ').split('\n')
        if len(users) >= len(hobbys):
            user_info = {user: hobby for user, hobby in zip_longest(users, hobbys)}
        else:
            sys.exit(1)
        f3.write(json.dumps(user_info))
        f3.seek(0)
        dicts_json = f3.read()
        dicts = json.loads(dicts_json)
        print(dicts)
