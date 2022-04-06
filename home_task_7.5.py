import os


def stat_folder(folder):
    dict = {}
    file_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            size = os.path.getsize(os.path.join(root, file))
            i = 0
            while True:
                if int(size) == 0:
                    break
                else:
                    size = size / 10
                    i += 1
            if size == 0:
                if 100 not in dict:
                    dict[100] = 1
                else:
                    dict[100] += 1
            else:
                if 10 ** i not in dict:
                    dict[10 ** i] = 1
                else:
                    dict[10 ** i] += 1

    for key, value in dict.items():
        dict[key] = (value, [])

    for root, dirs, files in os.walk(folder):
        for file in files:
            size = os.path.getsize(os.path.join(root, file))
            ext = file.split('.')[-1]
            i = 0
            while True:
                if int(size) == 0:
                    break
                else:
                    size = size / 10
                    i += 1
            if size == 0:
                dict[100][1].append(ext)
            else:
                dict[10 ** i][1].append(ext)

    print(dict)


folder = os.path.join(os.getcwd())
stat_folder(folder)
