small_storage = {
    'гвозди':500,
    'шурупы':600,
    'саморезы':700
}
big_storage = {
    'доски':50,
    'балки':20,
    'рейки':100
}
big_storage.update(small_storage)
for i in big_storage:
    print(i, ':', big_storage[i], end='; ')
print()
supply = input('Введите наименование: ')
print('Остаток {0}'.format(supply), ':', big_storage.get(supply), 'штук')

