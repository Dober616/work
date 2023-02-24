import datetime
import functools

def logging(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except BaseException:
            with open('errors.txt', 'a') as file:
                file.write(f'{datetime}: Ошибочка вышла')
    return wrapped_func

@logging
def count():
    my_list = [i for i in range(10)]
    return my_list[11]

count()