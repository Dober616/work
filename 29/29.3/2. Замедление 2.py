from time import time
import functools
import time

def seconds(_func=None, *, count=5):
    def freezer(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            print(f'Выполняю вашу функцию, подождите {count} секунд')
            time.sleep(count)
            result = func(*args, **kwargs)
            return result
        return wrapped_func
    if _func is None:
        return freezer
    else:
        return freezer(_func)


@seconds(count=3)
def my_square(number):
    return number ** 2

print(my_square(3))