import os

folders = {'my_project': ('settings', 'mainapp', 'adminapp', 'authapp')}

for key, values in folders.items():
    if not os.path.exists(key):
        os.mkdir(key)
    for value in values:
        root = os.path.join(key, value)
        if not os.path.exists(root):
            os.makedirs(root)
