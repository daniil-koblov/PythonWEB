pwd = 'text'
res = input('Введите пароль: ')
if res == pwd:
    print('Доступ разрешен.')
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('Вы в нормальном мире.')
    else:
        print('Будьте осторожны.')
else:
    print('Доступ запрещен.')
print('Работа звершена.')