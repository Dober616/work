def func_2(func, *args, **kwargs):
    return func(*args, **kwargs) ** 2

def func_1(x):
    return x + 10

print(func_2(func_1, 9))