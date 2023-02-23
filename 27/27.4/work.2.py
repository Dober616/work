PLUGINS = dict()

def register(func):
    PLUGINS[func.__name__] = func
    return func
@register
def greeting(name):
    return f'Hello, {name}'
@register
def good_bye(name):
    return f'Goodbye, {name}'

print(greeting('Tom'))
print(good_bye('Tom'))
for i in PLUGINS:
    print(i)