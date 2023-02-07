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



print(say_hello('Tom'))
for i in PLUGINS.keys():
    print(f'{i}: {PLUGINS[i]}')