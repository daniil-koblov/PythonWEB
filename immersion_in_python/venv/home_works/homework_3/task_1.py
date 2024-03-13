items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

#  Решение

weight_backpack = 0
backpack = {}

for item in items:
    weight_backpack += items[item]
    if weight_backpack <= max_weight:
        backpack[item] = items[item]

#  Эталонное решение

backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight