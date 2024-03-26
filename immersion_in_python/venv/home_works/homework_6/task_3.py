# Решение

from random import randint as rni
from task_2 import check_queens
def generate_boards():
    board_list = []
    while len(board_list) < 4:
        q_list = []  # список для положений ферзей
        counter = 0  # счетчик для остановки цикла
        while len(q_list) < 8:
            queen = (rni(1,8), rni(1,8))  # формируем позицию ферзя
            q_list.append(queen)  # добавляем ферзя в список
            if not check_queens(q_list):  # проверяем пары функцией из предыдущей задачи
                q_list.pop() # если пара неподходит, удаляем её
            counter += 1
            if counter == 64:  # если счетчик достиг 64, вариант не найден, начинаем заново
                break
        if len(q_list) == 8:  # если в списке 8 ферзей добавляем наш список в итоговый список
            board_list.append(q_list)
    return board_list

# Эталонное решение
import random
from itertools import combinations

def generate_board():
    # Генерируем случайную доску
    board = []

    for i in range(1, 8+1):
        queen = (i, random.randint(1, 8))
        board.append(queen)
    return board

def generate_boards():
    # Генерируем доски, пока не получим 4 успешные расстановки
    count = 0
    board_list = []
    while count < 4:
        board = generate_board()
        if check_queens(board):
            count += 1
            board_list.append(board)
    return board_list

print(generate_boards())
