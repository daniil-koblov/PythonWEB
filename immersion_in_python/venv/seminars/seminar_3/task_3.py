from random import randint as ri

print(new_list := [ri(1, 5) for _ in range(10)])

# for item in new_list:
#     if new_list.count(item) == 2:
#         new_list.remove(item)
#         new_list.remove(item)

print(my_list := [item for item in new_list if new_list.count(item) != 2])
