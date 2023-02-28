from datetime import datetime
import functools
import time

def createtime(cls):
    @functools.wraps(cls)
    def wrapped_func(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print('Время создания инстанса', datetime.utcnow())
        return instance
    return wrapped_func

def timer(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print('Начинаю выполнение функции')
        start = time.time()
        result = func(*args, **kwargs)
        run_time = time.time() - start
        print(f'Функция выполнялась {run_time} секунд')
        return result
    return wrapped_func

def for_all_methods(decorator):
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                cur_method = getattr(cls, i_method)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method, decorated_method)
        return cls
    return decorate


@createtime
@for_all_methods(timer)
class Functions:
    def __init__(self, max_num):
        self.max_num = max_num

    def squares_sum(self):
        number = 100
        result = 0
        for _ in range(number):
            result += sum([i**2 for i in range(self.max_num)])
        return result

    def qubes_sum(self, number):
        result = 0
        for _ in range(number):
            result += sum([i**3 for i in range(self.max_num)])
            return result

my_funcs_1 = Functions(max_num=1000)
my_funcs_1.squares_sum()
my_funcs_1.qubes_sum(100)
# time.sleep(3)
# my_funcs_2 = Functions(max_num=2000)
# time.sleep(3)
# my_funcs_3 = Functions(max_num=3000)
