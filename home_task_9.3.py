class Worker:
    def __init__(self, name, surname, position, income_wage, income_bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": income_wage, "bonus": income_bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'Total income: {self._income["wage"] + self._income["bonus"]}')


person = Position('Павел', 'Косарев', 'python developer', 2000, 200)
person_2 = Position('Петя', 'Пупкин', 'с++ developer', 1000, 100)
person.get_full_name()
person.get_total_income()
person_2.get_full_name()
person_2.get_total_income()
