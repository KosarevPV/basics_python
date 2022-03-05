prices = [57.8, 11, 44.99, 56.12, 99.99, 23.1, 86, 11, 0.01, 89.1, 56, 45, 12.34, 44.44, 1.1, 11.03, 11.01, 99.98]

for price_idx in range(len(prices)):
    rubles = int(str(prices[price_idx]).split('.')[0])
    penny = int(str(prices[price_idx]).split('.')[-1])
    if len(str(prices[price_idx]).split('.')) > 1:
        prices[price_idx] = f'{rubles} руб {penny:02d} коп'
    else:
        prices[price_idx] = f'{rubles} руб 00 коп'

print('Цены через запятую в одну строку: ' + ', '.join(prices))
print('Индекс списка до сортировки: ' + str(id(prices)))
prices.sort()
print('Цены, отсортированные по возрастанию: ' + ', '.join(prices))
print('Индекс списка после сортировки по возрастанию: ' + str(id(prices)))
prices = sorted(prices, reverse=True)
print('Цены, отсортированные по убыванию: ' + ', '.join(prices))
print('Индекс списка после сортировки по убыванию: ' + str(id(prices)))
print('Пять самых дорогих товаров: ' + ', '.join(prices[:5]))
print('Пять самых дорогих товаров по возрастанию: ' + ', '.join(sorted(prices[:5])))
print('Пять самых дорогих товаров по возрастанию: ' + ', '.join(prices[4::-1]))