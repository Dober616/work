def func_2(some_func, *args, **kwargs):
    result = some_func(*args, *kwargs)
    return result

def func_1(x):
    return x * 10

print(func_2(func_1, 10))