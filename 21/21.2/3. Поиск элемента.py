def find_key(data, key):
    if key in data:
        return data[key]
    for content in data:
        if isinstance(content, data):
            result = find_key(content, key)
            if result:
                break
    else:
        result = None
    return result




site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой загловок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

my_key = input('Введите искомый ключ: ')
if find_key(site, my_key):
    print(f'Значение: {find_key(site, my_key)}')
else:
    print('Такого ключа нет.')