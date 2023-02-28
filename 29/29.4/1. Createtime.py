import functools
def decorator(cls):
    @functools.wraps(cls)
    def wrapped_func(*args, **kwargs):
        print('Начинаем выполнение методов класса')
        result = cls(*args, **kwargs)
        print('Закончили выполнение методов класса')
        return result
    return wrapped_func

def for_all_methods(decorator):
    @functools.wraps(decorator)
    def wrapped_func(cls):
        for each_method in dir(cls):
            if each_method.startswith('__') is False:
                cur_method = getattr(cls, each_method)
                decorated_method = decorator(cur_method)
                setattr(cls, each_method, decorated_method)
        return cls
    return wrapped_func

@for_all_methods(decorator)
class Functions:
    def __init__(self, number=None):
        self.number = number

    def square(self):
        return self.number**2

    def qube(self):
        return self.number**3

ttt = Functions(2)
print(ttt.square())
print(ttt.qube())

