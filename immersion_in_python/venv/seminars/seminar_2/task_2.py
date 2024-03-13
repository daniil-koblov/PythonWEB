# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

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