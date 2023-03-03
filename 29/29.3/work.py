import time
import functools
from collections.abc import Callable
def timer_with_presision(_func=None, *, presision=10):
    def timer(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)
            finish_time = time.time()
            runtime = finish_time - started_at
            print(f'Функция выполнялась {round(runtime, presision)} секунд')
            return result
        return wrapped_func
    if _func is None:
        return timer
    else:
        return timer(_func)

@timer_with_presision(presision=4)
def squares(number):
    result = 0
    for _ in range(number):
        result += sum([i**2 for i in range(10000)])
    return result
@timer_with_presision
def qubes(number):
    result = 0
    for _ in range(number):
        result += sum([i**3 for i in range(10000)])
    return result
print(squares(100))
print(qubes(100))
