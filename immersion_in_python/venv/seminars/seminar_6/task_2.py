from random import randint

def guess_number(num1: int, num2: int, num3: int) -> bool:
    print(f"Угадай число от {num1} до {num2}, у тебя {num3} попыток")
    ans_number = randint(num1, num2)
    while num3:
        user_num = int(input("Введите число: "))
        if user_num == ans_number:
            return True
        elif user_num < ans_number:
            print("Больше")
        elif user_num > ans_number:
            print("Меньше")
        num3 -= 1
    return False

def riddles(quesion: str, answers: list[str], tryes: int) -> str:
    print(f"Отгадай загадку: \n{quesion}")
    true_answer = list(map(lambda x: x.lower(), answers))
    while tryes:
        for i in range(1, tryes + 1):
            print(f"Осталось попыток: {tryes}")
            user_answer = input("Введите отгадку: ").lower()
            if user_answer in true_answer:
                return i
            else:
                print("Не угадал! попробуй еще раз")
            tryes -= 1
    return 0
