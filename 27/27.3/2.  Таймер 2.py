import time


def timer(func):
    def wrapped_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        finish = time.time()
        run_time = finish - start
        return f'Время работы функции {func.__name__} составило {run_time}'
    return wrapped_func

@timer
def calculate(number):
    result = 0
    for _ in range(number + 1):
        result += sum([numm ** 2 for numm in range(100000)])
    return result

print(calculate(100))
