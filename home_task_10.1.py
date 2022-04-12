class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        if (len(self.data) == len(other.data)) and (len(self.data[0]) == len(other.data[0])):
            return Matrix([map(sum, zip(*i)) for i in zip(self.data, other.data)])
        else:
            msg = 'Складывать можно только матрицы одинаковых размеров.'
            raise ValueError(msg)

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.data])


matrix_1 = Matrix([[1, 2, 4], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[9, 8, 6], [7, 5, 4], [3, 2, 1]])
print(matrix_1)
print('________________')
print(matrix_1 + matrix_2)
