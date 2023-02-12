import time
class Timer:
    def __init__(self):
        print('Время работы кода')
        self.start = None

    def __enter__(self) -> 'Timer':
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.start)
        # if exc_type is TypeError:
        #     return True
        return True



with Timer() as t1:
    print('Первая часть')
    val_1 = 100 * 100 ** 100000
    val_1 += 'qwer'
    #еще какой-то код

with Timer() as t2:
    print('Вторая часть')
    val_2 = 200 * 200 ** 100000
    #еще какой-то код

with Timer() as t3:
    print('Третья часть')
    val_3 = 300 * 300 ** 100000
    #Еще какой-то код

