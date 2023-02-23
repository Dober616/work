n = int(input('Введите размер матрицы: '))
n += 1
for row in range(1, n):
    for col in range(1, n):
        if row % 2 == 0:
            print(row, end=' ')
        else:
            print(col, end=' ')
    print()