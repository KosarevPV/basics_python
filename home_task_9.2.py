class Road:
    def __init__(self, lenght, widht):
        self._lenght = lenght
        self._widht = widht

    def calc_weight(self, weght_per_sm=25, sm=5):
        print(f'{int((self._widht * self._lenght * weght_per_sm * sm) / 1000)} т.')


r_1 = Road(5000, 20)
r_1.calc_weight()
