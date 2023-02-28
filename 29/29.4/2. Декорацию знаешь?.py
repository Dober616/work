import functools


def logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'a') as file:
            file.write(result)
            print('Результаты функции записаны в лог файл')
        return result
    return wrapper

def decorator(cls):
    for method in dir(cls):
        if not method.startswith('__'):
            result = logging(method)
            return result
    return cls


@decorator
class MyClass:
    def method_1(self):
        return 'Hello, world'
    def method_2(self):
        return 'Hello, world'
    def method_3(self):
        return 'Hello, world'

t = MyClass()

