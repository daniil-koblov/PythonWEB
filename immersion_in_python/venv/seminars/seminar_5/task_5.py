# var 1
answer = []
for num in range(100):
    if not num % 15:
        num = "FizzBuzz"
    elif not num % 5:
        num = "Buzz"
    elif not num % 3:
        num = "Fizz"
    answer.append(num)

# var 2
res = (
    "fizzbuzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i
    for i in range(1, 101)
)
print(*res)


# var 3
def num_print_friz_buzz(num):
    for n in range(1, num + 1):
        if not n % 3 and not n % 5:
            yield "FizzBuzz"
        elif not n % 3:
            yield "Fizz"
        elif not n % 5:
            yield "Buzz"
        else:
            yield n


for i in num_print_friz_buzz(100):
    print(i)