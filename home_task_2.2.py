temp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0

while i < len(temp):
    if temp[i].isdigit():
        temp[i] = f'{int(temp[i]):02d}'
        temp.insert(i, '"')
        temp.insert(i + 2, '"')
        i += 2
    if temp[i][1:].isdigit():
        temp[i] = f'{temp[i][:1]}{int(temp[i]):02d}'
        temp.insert(i, '"')
        temp.insert(i + 2, '"')
        i += 2
    i += 1

print(' '.join(temp))
