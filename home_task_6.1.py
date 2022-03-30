with open('nginx_logs.txt', encoding='utf-8') as f:
    f_lines = [(f_line.split(' ')[0], f_line.split(' ')[5][1:], f_line.split(' ')[6]) for f_line in f.readlines()]
    print(f_lines)
