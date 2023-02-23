size = int(input('Размер квадрата: '))
size += 1
for row in range(1, size):
    for col in range(1, size):
        if row % 2 == 0:
            print(row, end='\t')
        else:
            print(col, end='\t')
    print()
