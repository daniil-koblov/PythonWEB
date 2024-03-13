lst = [1, 1, 2, 3, 3]

#  Решение

new_list = set()

for item in lst:
    if lst.count(item) > 1:
        new_list.add(item)

print(list(new_list))

#  Эталонное решение

duplicates = set()

for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)

result = list(duplicates)
print(result)