import  time

def my_timer(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    finish_time = time.time()
    result = finish_time - start_time
    return f'Время работы функции {func.__name__} составило {result} секунд\n' \
           f'Результат работы функции {func.__name__}: {func(*args, **kwargs)}'

def calculate(number):
    result = 0
    for _ in range(number + 1):
        result += sum([some_numm ** 2 for some_numm in range(10000)])
    return result

print(my_timer(calculate, 100))