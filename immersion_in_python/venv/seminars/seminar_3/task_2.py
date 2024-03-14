my_tuple = (1, 'hello', 3.14, True, [1, 2, 3], 2, {'key': 'value'}, 3, False, 'строка')

result = {}

for item in my_tuple:
    if type(item) in result:
        result[type(item)].append(item)
    else:
        result[type(item)] = [item]

print(result)
