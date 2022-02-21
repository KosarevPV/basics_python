range_numbers = list(range(1, 1001, 2))
range_numbers_3 = []
for i in range_numbers:
    range_numbers_3.append(i ** 3)

plus_number = [0, 17]
index_plus_number = 0

while index_plus_number < len(plus_number):
    sum_list = []
    for r in range_numbers_3:
        r = r + plus_number[index_plus_number]
        r_list = []
        g = 0
        while g < len(str(r)):
            h = int((str(r)[g:g + 1]))
            r_list.append(h)
            g += 1
        sum_figure = 0
        for k in r_list:
            sum_figure += k

        sum_numbers = 0
        if sum_figure % 7 == 0:
            sum_list.append(r)
    index_plus_number += 1
    print(sum(sum_list))
