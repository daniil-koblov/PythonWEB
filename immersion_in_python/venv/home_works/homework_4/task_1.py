matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

#  Решение

def transpose(matrix):
    transp_matrix = []
    # создаем новую пустую матрицу с обратным количеством строк и столбцов
    for i in matrix:
        for _ in range(len(i)):
            transp_matrix.append([])
        break
    # заполняем новую матрицу значениями из старой
    for i in matrix:
        for j in range(len(i)):
            transp_matrix[j].append(i[j])
    return transp_matrix


print(transpose(matrix))

#  Эталонное решение

def transpose(matrix):
    # определяем количество строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # создаем новую матрицу с размерами, поменянными местами
    transposed = [[0 for row in range(rows)] for col in range(cols)]

    # заполняем новую матрицу значениями из старой матрицы
    for row in range(rows):
        for col in range(cols):
            transposed[col][row] = matrix[row][col]

    return transposed