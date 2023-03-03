import time
from datetime import datetime
import functools

def create_time(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(f'Время создания инстанса класса: {datetime.utcnow()}')
        return instance
    return wrapper

def timer(func):
    start = time.time()
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        run_time = time.time() - start
        print(f'Функция выполнялась {run_time} секунд')
        return result
    return wrapper

def for_all_methods(decorator):
    @functools.wraps(decorator)
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                cur_method = getattr(cls, method)
                decorated_method = decorator(cur_method)
                setattr(cls, method, decorated_method)
        return cls
    return decorate

@create_time
@for_all_methods(timer)
class Functions:
    def __init__(self, max_num):
        self.max_num = max_num

    def squares_sum(self):
        number = 100
        result = 0
        for _ in range(self.max_num):
            result += sum([i**2 for i in range(10000)])
        return result

    def qubes_sum(self, number):
        self.number = number
        result = 0
        for _ in range(self.number):
            result += sum([i**3 for i in range(10000)])
        return result

my_func_1 = Functions(max_num=1000)
# time.sleep(2)
# my_func_2 = Functions(max_num=2000)
# time.sleep(5)
# my_func_3 = Functions(max_num=3000)

my_func_1.squares_sum()
my_func_1.qubes_sum(100)

