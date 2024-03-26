queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]

# Решение

# Проверяем, бьют ли ферзи друг друга

def is_attacking(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1]:  # вертикаль и горизонталь
        return True
    elif abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):  # диагонали
        return True
    return False


# Проверяем все возможные пары ферзей
def check_queens(queens):
    for i in range(len(queens)):
        for j in range(len(queens) - 1, i, -1):
            if is_attacking(queens[i], queens[j]):
                # print(f'ферзь {queens[i]} и ферзь {queens[j]} бьют друг друга')
                return False
    return True

q = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
print(check_queens(queens = q))

# Эталонное решение

from itertools import combinations

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True
