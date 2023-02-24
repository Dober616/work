import time


def freeze(func):
    def wrapped_func(*args, **kwargs):

        print('Долго думаю')
        time.sleep(3)
        result = func(*args, **kwargs)
        return result
    return wrapped_func

@freeze
def summ(a, b):
    return a + b

print(summ(2, 2))
