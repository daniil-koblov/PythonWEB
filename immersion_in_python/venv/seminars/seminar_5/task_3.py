# var 1
text = {'f': 102, 'h': 104, 'r': 114, 'y': 121}
ans = iter(text.items())
for _ in range(5):
    print(next(ans, "пар больше нет"))

# var 2
print(dictionary := {i: ord(i) for i in "Самостоятельно сохраните "})
a = iter(dictionary.items())
print(*(next(a) for _ in range(5)))