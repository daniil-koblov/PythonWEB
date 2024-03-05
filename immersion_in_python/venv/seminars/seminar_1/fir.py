
def num(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i +1))

num(5)

height = int(input('Введите высоту елки: '))

for i in range(height):
    print(f'{"*" * (2 * i + 1):^{2 * height + 1}} ')

