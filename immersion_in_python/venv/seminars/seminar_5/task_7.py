# var 1
def generat_pr(number):
    num = 2
    count = 0
    while count < number:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num
            count += 1
        num += 1


for i in generat_pr(20):
    print(i, end=" ")


# var 2 бесконечный цикл
def func_gen():
    number = 0
    while True:
        number += 1
        if number in (1, 2, 3):
            yield number
            continue
        if not number % 2:
            continue
        for dev in range(3, int(number**0.5) + 1, 2):
            if not number % dev:
                break
        else:
            yield number


gen = func_gen()

for _ in range(10):
    print(next(gen))


# var 3
def generate_numbers():
    for n in range(2, N):
        if is_number(n):
            yield n


def is_number(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
    return True


primes = generate_numbers()
for _ in range(N):
    print(next(primes))