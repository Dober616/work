from contextlib import contextmanager
import time

@contextmanager
def timer():
    print('Начинаем отсчет времени...')
    start = time.time()
    try:
        yield
    except Exception as exc:
        print(exc)
    finally:
        print(f'Время выполнения функции {time.time() - start}')

with timer() as t1:
    result = 0
    for i in range(100):
        result += i**3
