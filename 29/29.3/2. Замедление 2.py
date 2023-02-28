import functools
import time
def choose_time(_func=None, *, some_time=2):
    def freeze(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            print('Начинаю выполнение функции. Подождите немного...')
            time.sleep(some_time)
            result = func(*args, **kwargs)
            return result
        return wrapped_func
    if _func is None:
        return choose_time
    return freeze(_func)

@choose_time(some_time=10)
def print_name(name):
    print(name)

print_name('Kirill')
