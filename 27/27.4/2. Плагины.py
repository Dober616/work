plagins_dict = dict()

def register(func):
    plagins_dict[func.__name__] = func
    return func


@register
def squares():
    result = 0
    for _ in range(100):
        result += sum([i**2 for i in range(10000)])
    return result

@register
def qubes(number):
    result = 0
    for _ in range(number + 1):
        result += sum([i**3 for i in range(10000)])
    return result

print(f'Сумма квадратов равна {squares()}')
print(f'Сумма кубов равна {qubes(number=100)}')

print(plagins_dict)