import time
import functools
def timer(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        run_time = finish - start
        print(f'Время выполнениня функции {func.__name__} составило {run_time} секунд')
        return result
    return wrapped_func

@timer
def squares():
    result = 0
    for _ in range(100):
        result += sum([i**2 for i in range(100000)])
    return result
@timer
def qubes(number):
    result = 0
    for _ in range(number):
        result += sum([i**3 for i in range(100000)])
    return result


print(squares())
print(qubes(100))
