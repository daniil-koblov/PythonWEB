e = int(input('Введите число E: '))
n = int(input('Введите число N: '))


def func_sum(num, limit):
    result = 0
    i = 1
    while i <= limit:
        # i % num - проверка наличия остатка от деления т.е. проверка кратности
        if i % num:
            result += i
        i += 1
    return result


print(func_sum(e, n))


