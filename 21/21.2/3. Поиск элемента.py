site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А здесь новый абзац'
        }
    }
}
def my_function(data, some_key):
    if some_key in data:
        return data[some_key]
    for substruct in data.values():
        if isinstance(substruct, dict):
            result = my_function(substruct, some_key)
            if result:
                break
    else:
        return None
    return result



my_key = input('Введите искомый ключ: ')

if my_function(site, my_key):
    print(my_function(site, my_key))
else:
    print('Такого ключа в структуре нет')
