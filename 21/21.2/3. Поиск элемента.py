site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(data, key):
    if key in data:
        return data[key]
    for sub_data in data.values():
        if isinstance(sub_data, dict):
            result = find_key(sub_data, key)
            if result:
                break
    else:
        return None
    return result


my_key = input('Какой ключ ищем? ')
if find_key(site, my_key):
    print(find_key(site, my_key))
else:
    print('Такого ключа в структуре нет')
