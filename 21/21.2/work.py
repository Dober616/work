# def fact(num):
#     if num == 0:
#         return 1
#     factorial = num * fact(num - 1)
#     return factorial
# print(fact(5))


site = {
    'html': {
        'head': {
            'title': 'Мой сайт',
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(struct, some_key):
    if some_key in struct:
        return struct[some_key]
    for substruct in struct.values():
        if isinstance(substruct, dict):
            result = find_key(substruct, some_key)
            if result:
                break
    else:
        result = None
    return result


user_key = input('Какой ключ ищем? ')
value = find_key(site, user_key)
if value:
    print(value)
else:
    print('Такого ключа в нашей структуре нет')