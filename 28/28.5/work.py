import time

class Timer:
    def __init__(self):
        print('Время работы кода')
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.start)
        if exc_type:
            print(exc_type)
            return True

with Timer() as t1:
    print('Первая часть')
    val_1 = 100 * 100 ** 1000
    val_1 += 'abc'
    # и еще какой-то код

with Timer() as t2:
    print('Вторая чать')
    val_2 = 200 * 200 ** 1000
    # и еще какой-то код
with Timer() as t3:
    print('Третья часть')
    val_3 = 300 * 300 ** 1000
    # и еще какой-то код

