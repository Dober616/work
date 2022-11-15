# user_name = input('Введите имя пользователя: ')
# file_name = input('Введите имя файла: ')
#
# path = 'C:/{user}/docs/folder/{new_file}.txt'.format(
#     user=user_name,
#     new_file=file_name
# )
# path_2 = 'C:/{0}/docs/folder/{1}.txt'.format(
#     user_name,
#     file_name
# )
#
# path_3 = f'C:/{user_name}/docs/folder/{file_name}.txt'
#
#
# print(path)
# print(path_2)
# print(path_3)

while True:
    congratulations = input('Введите шаблон поздравления, '
                            'в шаблоне нужно использовать конструкцию {name}: ')
    if '{name}' in congratulations:
        break
    else:
        print('Отсутствует конструкция {name}.')

print('Введите список имен (заканчивается на "end": ')
names_list = []
while True:
    name = input('Имя: ')
    if name != 'end':
        names_list.append(name)
    else:
        break

for i_name in names_list:
    print(congratulations.format(name=i_name))