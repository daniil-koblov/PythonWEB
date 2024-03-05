
year = int(input('Введите год: '))
result = None
if year % 4 != 0:
    result = 'Обычный'
elif year % 100 == 0:
    if year % 400 == 0:
        result = 'Високосный'
    else: result = 'Обычный'
else: result = 'Високосный'

print(result)
