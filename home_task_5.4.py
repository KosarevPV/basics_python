src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 56, 60, 38]

result = [num for num in src if num > src[src.index(num) - 1] and src.index(num) != 0]

print(result)
