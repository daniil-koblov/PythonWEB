MAX_NUM = 1000
MIN_NUM = 1
TENS = 10

while True:
    num = int(input('Введите число: '))
    if MIN_NUM < num < MAX_NUM:
        if num < TENS:
            result = num**2
        elif num < TENS**2:
            result = num // TENS + num % TENS
        else:
            result = (num % TENS * TENS**2 + num % TENS**2 - num % TENS\
            + num // TENS**2)
        break
    else: continue

print(result)
