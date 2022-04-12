from abc import ABC, abstractmethod


class Clothes(ABC):
    general_consumption = 0

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        self.general_consumption = self.consumption + other.consumption
        return self.general_consumption


class Coat(Clothes):
    def __init__(self, v, name=''):
        self.v = v
        self.name = name

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h, name=''):
        self.h = h
        self.name = name

    @property
    def consumption(self):
        return 2 * self.h + 0.3


clothe_1 = Coat(6.5, name='D&g')
clothe_2 = Suit(1, name='Prada')
print(f'{clothe_1.name} - {clothe_1.consumption}')
print(f'{clothe_2.name} - {clothe_2.consumption}')
print(f'General consumption - {clothe_1 + clothe_2}')
