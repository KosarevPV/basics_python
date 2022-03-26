def nums_gen(n):
    for num in range(1, n + 1):
        if num % 2 != 0:
            yield num


add_to_15 = nums_gen(15)

print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
