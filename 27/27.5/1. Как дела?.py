def greetings(func):
    def wrapped_func(*args, **kwargs):
        question = input('Как дела? ')
        print('А у меня нормально')
        result = func(*args, **kwargs)
        return result
    return wrapped_func

@greetings
def something():
    return f'Тут что-то происходит...'

print(something())