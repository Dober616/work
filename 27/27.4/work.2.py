PLUGINS = dict()


def register(func):
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f'Hello, {name}'

@register
def say_goodbuy(name):
    return f'Goodbuy, {name}'


print(PLUGINS)
print(say_hello('Tom'))