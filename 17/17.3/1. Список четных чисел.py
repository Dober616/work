a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
numm_list = [x for x in range(a, b+1) if x % 2 == 0]
print(numm_list)
