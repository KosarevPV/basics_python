import os, json

ROOT = os.getcwd()

with open('config.json', encoding='utf-8') as f:
    a = json.load(f)

for key, values in a.items():
    root_1 = os.path.join(ROOT, key)
    os.makedirs(root_1, exist_ok=True)
    for value in values:
        with open(os.path.join(root_1, value), 'x', encoding='utf-8'):
            pass
