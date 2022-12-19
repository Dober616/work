def factorial(my_num):
    if my_num == 1:
        return 1
    result = my_num * factorial(my_num - 1)
    return result

my_num = 5
print(factorial(my_num))