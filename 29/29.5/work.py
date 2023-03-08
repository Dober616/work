import functools
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f'Вызов номер {self.calls} функции {self.func.__name__}')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello, Peter!')

say_hello()
say_hello()
say_hello()