def factorial(my_number):
    if my_number == 1:
        return 1
    return my_number * factorial(my_number - 1)



my_number = int(input('Введите число: '))
print(factorial(my_number))