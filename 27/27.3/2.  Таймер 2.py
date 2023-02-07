import time


def My_timer(funk):
    def wrapped_funk(*args, **kwargs):
        start = time.time()
        result = funk(*args, ** kwargs)
        finish = time.time()
        run_time = finish - start
        print(f'Время выполнениня функции: {run_time}')
        return result
    return wrapped_funk

@My_timer
def my_funk():
    result = sum([i for i in range(100)])
    return result

@My_timer
def qubes_sum(number):
    result = 0
    for i in range(10000):
        result += sum([i**3 for i in range(number + 1)])
    return result

@My_timer
def my_summ(x, y):
    for i in range(y + 1):
        x += y
    return x

my_result = my_funk()
print(my_result)
qubes_res = qubes_sum(100)
print(qubes_res)
sum_res = my_summ(2, 1000)
print(sum_res)
