from decimal import Decimal
import datetime

import requests

def currency_rates(money):
    money = money.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.text
    parts_of_date = content.split('"')[5].split('.')
    date = datetime.datetime(year=int(parts_of_date[-1]), month=int(parts_of_date[-2]), day=int(parts_of_date[-3]))
    date = date.strftime('%Y-%m-%d')
    for el in content.split('<CharCode>')[1:]:
        if el.split('</')[0] == money:
           rate = el.split('</')[3].split('>')[2]
           rate_decimal = Decimal(f'{rate.split(",")[0]}.{rate.split(",")[1]}')
           return f'Дата: {date}, Курс {money}: {rate_decimal}'


if __name__ == '__main__':
    print(currency_rates('usd'))