text = "Вывести функцией каждое слово с новой строки"

def print_words(text):
    words = text.lower().split()
    max_len = max(len(word) for word in words )

    for i, word in enumerate(sorted(words), start=1):
        line = f'{i}. {word:>{max_len}}'
        print(line)

print_words(text)
