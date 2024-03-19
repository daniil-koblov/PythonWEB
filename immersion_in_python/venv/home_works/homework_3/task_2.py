text = 'Hello world. Hello Python. Hello again. 3'

#  Решение

import re

text = text.lower()
result = re.split("[ ,;.?!\d']", text)
result_sort = sorted(result, reverse=True)
text_dict = {}

for i in result_sort:
    if i == "":
        continue
    else:
        count = 0
        for j in result_sort:
            if j == i:
                count += 1
        text_dict.setdefault(i, count)

# print(result_sort)
text_dict_sort = dict(
    sorted(text_dict.items(), key=lambda item: item[1], reverse=True))
print(list(text_dict_sort.items()))

#  Эталонное решение

import re
from collections import Counter

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]

print(top_words)
