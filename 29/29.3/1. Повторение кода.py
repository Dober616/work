import functools

def repeat(_func=None, *, number=10):
    def do_twice(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            for _ in range(number):
                func(*args, **kwargs)
            result = func(*args, **kwargs)
            return result
        return wrapped_func
    if _func is None:
        return repeat
    return do_twice(_func)

@repeat(number=2)
def name_print(name):
    print(name)

name_print('Кирилл')
