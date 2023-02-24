def debugger(func):
    def wrapped_func(*args, **kwargs):
        print(f'Вызывается {func.__name__}, {args}, {kwargs}')
        print(f'{func.__name__} вернула значение {func(*args, **kwargs)}')
        return func(*args, **kwargs)
    return wrapped_func


@debugger
def greeting(name, age=None):
    if age:
        return f'Ого {name}! Тебе уже {age} лет, ты быстро растешь!'
    else:
        return f'Привет, {name}! Сколько тебе лет?'


print(greeting('Tom'))
print()
print(greeting('Misha, 100'))
print()
print(greeting(name='Katya', age=16))