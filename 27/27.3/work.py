import time


def my_timer(funk):
    def wrapped_func(*args, **kwargs):
        start_time = time.time()
        result = funk(*args, **kwargs)
        finish_time = time.time()
        run_time = round(finish_time - start_time, 4)
        print(f'Функция работала {run_time} секунд')
        return result
    return wrapped_func

@my_timer
def squares_sum():
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum(i**2 for i in range(10000))
    return result

@my_timer
def qubes_sum(number):
    result = 0
    for _ in range(number + 1):
        result += sum(i**3 for i in range(10000))
    return result

sq_summ = squares_sum()
print(sq_summ)

q_summ = qubes_sum(100)
print(q_summ)