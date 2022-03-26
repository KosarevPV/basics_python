src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 99]
dict_src = {}

for n in src:
    if n not in dict_src:
        dict_src[n] = 1
    else:
        dict_src[n] += 1

result = [key for key, value in dict_src.items() if value == 1]

print(result)
