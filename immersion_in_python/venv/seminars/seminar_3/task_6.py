data_text = input('Введите строку:\n')

result = {}
for item in set(data_text):
    result[item] = data_text.count(item)
print(result)

for item in data_text:
    result[item] = result.get(item, 0) + 1
print(result)
