import time

def timer(func, *args, **kwargs):
    started_at = time.time()
    func(*args, **kwargs)
    finished_at = time.time()
    run_time = finished_at - started_at
    return f'Функция {func.__name__} работала {run_time} секунд\n' \
           f'Результат функции {func(*args, **kwargs)}'
def squares_sum():
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([each_number**2 for each_number in range(10000)])
    return result

def qubes_sum(number):
    result = 0
    for _ in range(number + 1):
        result += sum([some_numm**3 for some_numm in range(10000)])
    return result

print(timer(squares_sum))
print(timer(qubes_sum, 100))
