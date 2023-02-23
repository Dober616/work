
def do_twice(func):
    def wrapped_func(*args, **kwargs):
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapped_func

@do_twice
def greeting(name):
    print(f'Привет, {name}')

greeting('Кирилл')
