# Создать 2 матрицы вида 10x10
# Чтобы заполнить матрицы различными значениями - воспользуйтесь модулем random
# Cложитe эти две матрицы в третью

import random

def prn(a):
    for i in range( len(a) ):
        print(*a[i])

# Исходные данные - число строк и столбцов любое. 
n = 10 # кол-во строк
m = 10 # кол-во столбцов

# инициализация генератора случайных чисел
random.seed(version=2)
# объявить матрицы-слагаемые и заполнить случ значениями в диапазоне -100 100 
matrix_1 = [[random.randint(-100, 100) for j in range(m)] for i in range(n)]
matrix_2 = [[random.randint(-100, 100) for j in range(m)] for i in range(n)]
# объявить матрицу - результат
matrix_3 = [[0 for j in range(m)] for i in range(n)]

# сложение - складываются соотвествующие элементы каждой матрицы
for i in range(n):
    for j in range(m):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]

print('Первая матрица')
prn(matrix_1)
print('Вторая матрица')
prn(matrix_2)
print('Сумма матриц')
prn(matrix_3)





