
import sys

data = [1, 'suk', 3.14, True, -1 , 'io']
for index, value in enumerate(data, 1):
    print(f'Порядковый номер: {index}')
    print(f'Значение: {value}')
    print(f'Адрес в памяти: {id(value)}')
    print(f'Размер: {value.__sizeof__()} байт')
    print(f'Хэш: {hash(value)}')

    if isinstance(value, int):
        print(f'Результат проверки на целое число: True')

    print(f'Результат проверки на целое число: ', 'True' if isinstance(
            value, str) else 'False')
    print('\n','=='*40, '\n')
