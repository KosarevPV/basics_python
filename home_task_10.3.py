class Cell:
    def __init__(self, count_cell):
        self.count_cell = count_cell
        if self.count_cell != int(self.count_cell):
            raise TypeError

    def __str__(self):
        return str(self.count_cell)

    def __add__(self, other):
        return Cell(self.count_cell + other.count_cell)

    def __sub__(self, other):
        if (self.count_cell - other.count_cell) >= 0:
            return Cell(self.count_cell - other.count_cell)
        else:
            raise ValueError

    def __mul__(self, other):
        return Cell(self.count_cell * other.count_cell)

    def __floordiv__(self, other):
        return Cell(self.count_cell // other.count_cell)

    def make_order(self, cell_in_line):
        list_cell = []
        for i in range(self.count_cell):
            list_cell.append('*')
        for i in range(1, (self.count_cell // cell_in_line) + 1):
            if ((i) * cell_in_line) + (i - 1) != len(list_cell):
                list_cell.insert(((i) * cell_in_line) + (i - 1), '\n')
        return list_cell


a = Cell(20)
b = Cell(10)
c = a + b
print(f'c - {c}')
d = a - b
print(f'd - {d}')
e = a * b
print(f'e - {e}')
f = a // b
print(f'f - {f}')

print(c.make_order(7))
print(d.make_order(5))
