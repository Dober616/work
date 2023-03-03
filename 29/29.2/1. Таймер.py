import time
from contextlib import contextmanager

@contextmanager
def my_timer():
    start = time.time()
    try:
        yield
    except BaseException as i:
        print(f'Обнаружена ошибка {i}')
    finally:
        print(f'Программка то все равно выполнится, время ее работы составит {time.time() - start}')

with my_timer() as timer:
    print('Начинаем выполнение функции')
    my_sum = 0
    for i in range(100):
        my_sum += sum([i ** 2 for i in range(100000)])
        my_sum += 'b'
