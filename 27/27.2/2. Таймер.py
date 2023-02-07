import time
def my_timer(some_function, *args, **kwargs):
    start = time.time()
    some_function(*args, **kwargs)
    finish = time.time()
    result = finish - start
    return result, some_function(*args, **kwargs)

def fibonacci(n):
    current_value = 0
    next_value = 1
    for _ in range(n):
        current_value, next_value = next_value, current_value + next_value
    return current_value


def my_summ():
    return 10 + 3
print(my_timer(fibonacci, 1000))
print(my_timer(my_summ))

