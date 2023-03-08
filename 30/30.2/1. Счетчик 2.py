

def counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        nonlocal count
        count += 1
        print(f'Функция {func.__name__} вызывалась {count} раз')
        return result
    return wrapper
@counter
def my_func():
    print('Привет, как дела')

my_func()
my_func()
my_func()
my_func()