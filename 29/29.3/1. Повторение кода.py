import functools

def count_do(_func=None, *, count=5):
    def do_twice(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            for _ in range(count - 1):
                print(func(*args, **kwargs))
            return func(*args, **kwargs)
        return wrapped_func
    if _func is None:
        return do_twice
    else:
        return do_twice(_func)

@count_do(count=7)
def greeting(name):
    return f'Привет, {name}'

print(greeting(name='Кирилл'))