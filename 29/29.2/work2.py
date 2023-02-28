import time
from contextlib import contextmanager
#
# class Timer:
#     def __init__(self):
#         print('Время работы кода: ')
#         self.start = 0
#
#     def __enter__(self):
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(time.time() - self.start)
#         return True

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    except Exception as ex:
        print(ex)
    finally:
        print(time.time() - start)


with timer() as t1:
    print('Первая часть')
    val_1 = 100 * 100 ** 100000

with timer() as t2:
    print('Вторая часть')
    val_2 = 200 * 100 ** 100000
with timer() as t3:
    print('Третья часть')
    val_3 = 300 * 100 ** 100000