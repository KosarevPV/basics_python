import re


def line_parse(line):
    pattern = re.compile(
        r'(\S+)[\s][-][\s][-][\s][\D](\S+\s\D\d+)[\D][\s][\W](\w+)[\s](\S+)[\s][\S+]{9}[\s](\d+)[\s](\d+)')
    result = pattern.finditer(line)
    for res in result:
        print(res.groups())


with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f.readlines():
        line_parse(line.strip())
