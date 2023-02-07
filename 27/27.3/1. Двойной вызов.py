def do_twice(func):
    def wrapped_func(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapped_func

@do_twice
def greeting(name):
    print (f'Привет {name}')

some = greeting('Кирилл')



