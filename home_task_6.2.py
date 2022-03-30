spam_finder_1 = {}

with open('nginx_logs.txt', encoding='utf-8') as f:
    for ip in f.readlines():
        if ip.split(' ')[0] in spam_finder_1:
            spam_finder_1[ip.split(' ')[0]] += 1
        else:
            spam_finder_1[ip.split(' ')[0]] = 1

sorted_keys = sorted(spam_finder_1, key=spam_finder_1.get, reverse=True)

print(f'Пользователь с IP: {sorted_keys[0]} отправил {spam_finder_1[sorted_keys[0]]} запросов')
