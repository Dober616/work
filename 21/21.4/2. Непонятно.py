data =  [1, 2, 3]
print(type(data))
if isinstance(data, (list, dict, set)):
    print('Изменяемый(mutable)')
else:
    print('Неизменяемый(unmutable)')
print(f'id объекта: {id(data)}')
