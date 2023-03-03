import time
from contextlib import contextmanager
from collections.abc import Iterator

@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except BaseException as exc:
        print(f'Обибка {exc}')
    finally:
        print(f'Время работы функции: {time.time() - start}')

# class Timer:
#     def __init__(self):
#         self.start = None
#
#     def __enter__(self):
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f'Время работы кода: {time.time() - self.start}')
#         return True

with timer() as t1:
    print('Первая часть')
    val_1 = 100 * 100 ** 1000000


with timer() as t2:
    print('Вторая часть')
    val_2 = 200 * 200 ** 1000000

with timer() as t3:
    print('Третья часть')
    val_3 = 300 * 300 ** 1000000
    val_3 += 'и'