import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        finish = time.time()
        run_time = finish - start
        print(f'Функция выполнялась {run_time} секунд')
        return func(*args, **kwargs)
    return wrapped_func


def logging(func):
    def wrapped_func(*args, **kwargs):
        print(f'Начинаю записывать лог к функции {func.__name__}')
        result = func(*args, **kwargs)
        print('Закончил записывать лог')
        return result
    return wrapped_func

@logging
@timer
def squares():
    number = 100
    result = 0
    for _ in range(10000):
        result += sum([i**2 for i in range(number + 1)])
    return result


@timer
@logging
def qubes(number):
    result = 0
    for _ in range(10000):
        result += sum([i**3 for i in range(number + 1)])
    return result


print(squares())
print(qubes(100))