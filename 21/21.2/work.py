# def factorial(num):
#     if num == 1:
#         return 1
#     fact_minus_1 = factorial(num - 1)
#     return num * fact_minus_1
#
#
# num_fact = factorial(5)
# print(num_fact)
def find_key_value(data, some_key):
    if some_key in data:
        return data[some_key]
    for subsruct in data.values():
        if isinstance(subsruct, dict):
            result =  find_key_value(subsruct, some_key)
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

value = find_key_value(site, my_key)
if value:
    print(value)
else:
    print('Такого значения в структуре нет')
