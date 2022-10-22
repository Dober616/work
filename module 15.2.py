nums_list = []
n = int(input('Введите количество чисел в списке: '))
for _ in range (n):
    numm = int(input('Введите число: '))
    nums_list.append(numm)
maximum  = nums_list[1]
minimum  = nums_list[1]
for i in nums_list:
    if i >= maximum:
        maximum = i
    elif i < minimum:
        minimum = i
print('Максимальное число: ', maximum)
print('Минимальное число: ', minimum)