duration = int(input('Промежуток времени: '))

if duration < 60:
    print(f'{duration} сек')
elif duration < 60 * 60:
    print(f'{duration // 60} мин {duration % 60} сек')
elif duration < 60 * 60 * 24:
    h = duration // (60 * 60)
    m = (duration // (60)) - (h * 60)
    print(f'{h} час {m} мин {duration % 60} сек')
else:
    d = duration // (60 * 60 * 24)
    h = duration // (60 * 60) - (d * 24)
    m = duration // 60 - (d * 24 * 60) - (h * 60)
    print(f'{d} дн {h} час {m} мин {duration % 60} сек')
