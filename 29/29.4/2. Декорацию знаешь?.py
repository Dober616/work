import functools
import datetime
# def logging(cls):
#     @functools.wraps(cls)
#     def wrapper(*args, **kwargs):
#         instance = cls(*args, **kwargs)
#         for method in dir(cls):
#             if not method.startswith('__'):
#                 result = getattr(cls, method)
#                 print(f'Логируем {result}')
#
#         return instance
#     return wrapper

def logged(func):
    def wrapped_func(*args, **kwargs):
        print(f'Запуск функции произошел в {datetime.datetime.now()}')
        return func(*args, **kwargs)
    return wrapped_func


def decorator(cls):
    for method in dir(cls):
        if method.startswith('__'):
            pass
        a = getattr(cls, method)
        if hasattr(a, '__call__'):
            decorated_a = logged(a)
            setattr(cls, method, decorated_a)
    return cls

@logged
class MyClass:
    def method_1(self):
        print('Привет, как дела')
    def method_2(self):
        print('Нормально')
    def method_3(self):
        print('А у тебя?')


t = MyClass()
t.method_1()
