import time

def timer(func):
    def wrapped_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        run_time = finish - start
        print(f'Функция {func.__name__} выполнялась {run_time} секунд')
        return result
    return wrapped_func

def logging(func):
    def wrapped_func(*args, **kwargs):
        print(f'\nВызывается функция {func.__name__}\t'
              f'Позиционные аргументы: {args}\t'
              f'Именованные аргументы: {kwargs}')
        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} успешно завершила работу')
        return result
    return wrapped_func

@timer
@logging
def squares(number):
    result = 0
    for _ in range(number + 1):
        result += sum([i ** 2 for i in range(100000)])
    return result
@logging
@timer
def qubes():
    result = 0
    for _ in range(100):
        result += sum([i**3 for i in range(100000)])
    return result

print(squares(100))
print(qubes())