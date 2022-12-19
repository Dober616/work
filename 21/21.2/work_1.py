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


def find_key(struct, key):
    if key in struct:
        return struct[key]
    for substruct in struct.values():
        if isinstance(substruct, dict):
            result = find_key(substruct, input_key)
            if result:
                break
        print('Такого ключа в структуре нет')
        break
    else:
        return result

input_key = input('Какой ключ ищем? ')
print(find_key(site, input_key))


