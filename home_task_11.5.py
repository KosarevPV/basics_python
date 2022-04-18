import re


class ComplexNumber:
    def __init__(self, c_num):
        self.c_num = c_num
        if not re.search(r'^(\d+)[+](\d+)[i]$', c_num):
            raise ValueError('Введено не комплесное число')

    def __add__(self, other):
        num_1 = str(self.c_num).split('+')
        num_2 = str(other.c_num).split('+')
        num_3 = f'{(int(num_1[0]) + int(num_2[0]))}+{(int(num_1[1][:-1]) + int(num_2[1][:-1]))}i'
        return ComplexNumber(num_3)

    def __mul__(self, other):
        num_1 = str(self.c_num).split('+')
        num_2 = str(other.c_num).split('+')
        a = int(num_1[0])
        b = int(num_1[1][:-1])
        c = int(num_2[0])
        d = int(num_2[1][:-1])
        num_3 = f'{(a * c) - (b * d)}+{(b * c) + (a * d)}i'
        return ComplexNumber(num_3)


n_1 = ComplexNumber('3+9i')
n_2 = ComplexNumber('12+2i')
n_3 = n_1 + n_2
print(n_3.c_num)
n_4 = n_1 * n_2
print(n_4.c_num)
