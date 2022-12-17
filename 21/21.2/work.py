# def factorial(num):
#     if num == 1:
#          return 1
#     fact_n_minus_1 = factorial(num - 1)
#     return num * fact_n_minus_1
#
#
# num_fact = factorial(5)
# print(num_fact)

def find_key(structure, key):
    if key in structure:
        return structure[key]
    for substructure in structure.values():
        if isinstance(substructure, dict):
            result = find_key(substructure, key)
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
user_key = input('Какой ключ ищем?: ')
value = find_key(site, user_key)
if value:
    print(value)
else:
    print('Такого ключа на сайте нет')