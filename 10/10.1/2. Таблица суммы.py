n = int(input('Введите число: '))
n += 1
for row in range(n):
    for col in range(n):
        print(row + col, end='\t')
    print()