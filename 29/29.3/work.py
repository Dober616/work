import time
import functools
def timer_precision(_func=None, *, precision=10):
    def timer_decorator(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            start = time.time()
            print('Начинаем выполнять функцию')
            result = func(*args, **kwargs)
            finish = time.time()
            run_time = round(finish - start, precision)
            print(f'Функция выполнялась {run_time}')
            return result
        return wrapped_func
    if _func is None:
        return timer_decorator
    return timer_decorator(_func)

@timer_precision
def squares():
    result = 0
    for _ in range(100):
        result += sum([i**2 for i in range(100000)])
    return result

@timer_precision(precision=3)
def qubes(number):
    result = 0
    for _ in range(number):
        result += sum([i**3 for i in range(100000)])
    return result

s = squares()
print(f'Результат выполнения функции:{s}')
print()
q = qubes(100)
print(f'Результат выполнения функции: {q}')
