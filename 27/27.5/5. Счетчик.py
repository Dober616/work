import functools

def counter(func):

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} выполнялась {wrapped_func.count} раз')
        return result

    wrapped_func.count = 0
    return wrapped_func
@counter
def my_func():
    pass

@counter
def some_func():
    pass

my_func()
my_func()
my_func()
my_func()
my_func()

some_func()
