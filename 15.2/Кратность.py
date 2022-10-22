numm_list = []
n = int(input('Введите количество чисел: '))
for i in range (n):
    number = int(input('Введите число: '))
    numm_list.append(number)
print()
print(numm_list)
print()
deliver = int(input('Введите делитель: '))
summ = 0
x = -1
for y in numm_list:
    if y % deliver == 0:
        print('Индекс числа ', y,  ':', numm_list.index(y))
        summ += numm_list.index(y)
print('Сумма индексов =', summ)
