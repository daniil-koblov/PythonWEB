# var 1
print(
    list(num for num in range(0, 101, 2) if sum(int(digit) for digit in str(num)) != 8)
)

# var 2

gen_even = (i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8)
print(*gen_even)

# var 3
gen_even = (i for i in range(0, 101, 2) if (i // 10 + i % 10) != 8)
print(*gen_even)