# Решение

def fibonacci():
    value1 = 0
    value2 = 1
    counter = 0
    temp = 0
    while True:
        if counter < 3:
            yield value1
            counter += 1
            value1 = value2
        else:
            temp = value1 + value2
            yield temp
            value1 = value2
            value2 = temp


# Эталонное решение

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci()
for i in range(10):
    print(next(f))
