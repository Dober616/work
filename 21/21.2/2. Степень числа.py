def my_function(my_numm, other_numm):
    if other_numm == 0:
        return 1
    result = my_numm * my_function(my_numm, other_numm - 1)
    return result

my_numm = float(input('Введите вещественное число: '))
other_numm = int(input('Введите степень числа: '))

print(my_function(my_numm, other_numm))