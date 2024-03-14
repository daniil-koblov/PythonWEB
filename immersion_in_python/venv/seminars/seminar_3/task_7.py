## var 1
friends = {
    "Ivan": ("matches", "food", "games", "umbrella"),
    "Bob": ("food", "games", "tent"),
    "Jack": ("food", "tent",  "phone"),
    # "Tom": ("tent", "shovel"),
}

# task 1 Какие вещи взяли все три друга
things = set()
for i in friends.values():
    things.update(set(i))  # наполняем множество уникальных наименований
print('В поход взяли:', *things)

# task 2 Какие вещи уникальны, есть только у одного друга
diff_things = []  # список для уникальных вещей
things = []  # список для перебора всех вещей
for value in friends.values():
    for i in value:
        if i not in diff_things:
            diff_things.append(i)  # добавляем вещь в уникальный список
        if i in things:
            diff_things.remove(i)  # если такая вещь есть в общем списке, удаляем её
        if i not in things:
            things.append(i)  # наполняем список всех вещей
print('Вещи которые взял кто-то один:', *diff_things)  # выводим список уникальных вещей

# task 3 Какие вещи есть у всех друзей кроме одного и имя того,
# у кого данная вещь отсутствует
all_things = []  # список для всех вещей и сколько их взяли
things = set()  # множество уникальных наименований как в task 1
for i in friends.values():
    things.update(set(i))  # наполняем множество уникальных наименований

for value in friends.values():
    for i in value:
        all_things.append(i)  # наполняем список для всех вещей и сколько их взяли

for k, v in friends.items():
    for i in things:
        if (  # проверка, если вещь взяли все кроме одного
            all_things.count(i) == len(friends) - 1
        ):
            if i not in v:
                print(f"{k} не взял {i}")  # выводим кто не взял вещь

## var 2
max_things = {
    "maksim": ("Телефон", "Бритва", "Галстук", "Шорты", "Рубашка"),
    "sergey": ("Телефон", "Шорты", "Зонтик", "Ключи", "Бритва"),
    "shamil": ("Телефон", "Бритва", "Рубашка", "Шорты", "Галстук"),
}

# 1 что взяли общего
all_things = set()
spisok = []
for value in max_things.values():
    all_things.update(set(value))
    for i in value:
        spisok.append(i)


# 2 Какие вещи уникальны, есть только у одного друга
one_thing = {}
for item in all_things:
    one_thing[item] = spisok.count(item)

for k, v in one_thing.items():
    if v == 1:
        print(f"{k}")

# 3 Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
dict_len = len(max_things)
for k, v in one_thing.items():
    if v == dict_len - 1:
        for name, values in max_things.items():
            if k not in values:
                print(f"{name} не взял {k}")

## var 3 (от Stone)
friends = {
    "Максим": ("топор", "вода", "еда", "палатка"),
    "Шамиль": ("топор", "вода", "закуска", "карты"),
    "Сергей": ("топор", "водка", "еда", "карты"),
}


all_things = set()
for friend_item in friends.values():
    all_things.update(set(friend_item))

have_all_friends = all_things.copy()
for friend_item in friends.values():
    have_all_friends.intersection_update(friend_item)
print("Вещи, которые есть у всех:")
print(*have_all_friends)
print()

only_one_friend = {}
for friend in friends:
    friend_backpack = set(friends[friend])
    for other_friend in friends:
        if friend != other_friend:
            friend_backpack.difference_update(friends[other_friend])
    if friend_backpack:
        only_one_friend[friend] = friend_backpack
print(
    "Есть только у одного:",
    *[f'{name}: {", ".join(back)}' for name, back in only_one_friend.items()],
    sep="\n",
)
print()

all_except_one_friend = {}
for friend in friends:
    friend_backpack = friends[friend]
    friends_backpacks = all_things.copy()
    for other_friend in friends:
        if friend != other_friend:
            friends_backpacks.intersection_update(friends[other_friend])
    friends_backpacks.difference_update(friend_backpack)
    if friends_backpacks:
        all_except_one_friend[friend] = friends_backpacks
print(
    "Есть у всех, кроме одного:",
    *[
        f'{name} не взял: {", ".join(back)}'
        for name, back in all_except_one_friend.items()
    ],
    sep="\n",
)
