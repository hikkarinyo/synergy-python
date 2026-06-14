# Урок №13. Двумерные списки
# Задание №1
# С помощью цикла создайте матрицу вида 10x10.
# Чтобы заполнить матрицы различными значениями - воспользуйтесь модулем random.
# Итого у вас должно получиться сперва две матрицы одинаковой размерности.
# Затем нужно сложить эти две матрицы в третью.
# Задание считается выполненным, если вы напишите алгоритм, который будет уметь
# как складывать матрицы, так и генерировать матрицы различных размерностей.
# Будь то матрицы 10х10 или 4х3.

import random

def generate_matrix(rows, cols):
    # генерирует матрицу заданного размера со случайными числами
    return [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

def add_matrices(m1, m2):
    # складывает две матрицы одинаковой размерности
    rows = len(m1)
    cols = len(m1[0])
    return [[m1[i][j] + m2[i][j] for j in range(cols)] for i in range(rows)]

def print_matrix(matrix):
    # выводит матрицу построчно
    for row in matrix:
        print(row)

# генерируем две матрицы 10x10
rows, cols = 10, 10

matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)
matrix_3 = add_matrices(matrix_1, matrix_2)

print("Matrix 1:")
print_matrix(matrix_1)

print("\nMatrix 2:")
print_matrix(matrix_2)

print("\nMatrix 3 (сумма):")
print_matrix(matrix_3)
