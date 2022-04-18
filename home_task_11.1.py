import re


class Date:
    cl_date = None

    def __init__(self, data_date):
        self.data_date = data_date
        if len(data_date) != 10 or not re.search(r'^(\d{2})[\-](\d{2})[\-](\d{4})', data_date):
            raise ValueError('Неправильный формат данных!')
        else:
            Date.cl_date = self.data_date

    @classmethod
    def int_date(cls):
        list_date = [int(data) for data in Date.cl_date.split('-')]
        return list_date

    @staticmethod
    def validator_date():
        d = Date.int_date()[0]
        m = Date.int_date()[1]
        y = Date.int_date()[2]
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and (d < 1 or d > 31):
            raise ValueError('Значение дня неверно')
        if (m == 4 or m == 6 or m == 9 or m == 11) and (d < 1 or d > 30):
            raise ValueError('Значение дня неверно')
        if (d < 1 or d > 29) and (m == 2):
            raise ValueError('Значение дня неверно')
        if m == 0 or m > 12:
            raise ValueError('Значение месяца неверно')
        if y == 0 or y > 2022:
            raise ValueError('Значение года неверно')


d_1 = Date('03-03-1999')
d_1.validator_date()
