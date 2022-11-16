disc_letter = input('Введите диск: ')
user_name = input('Введите пользователя: ')
file_name = input('Введите имя файла: ')
aloowed_format = '.txt'

path = '{disc}:/{user}/docs/folder/{new_file}'.format(
    disc=disc_letter,
    user=user_name,
    new_file=file_name
)

if not path.endswith(aloowed_format):
    print('Ошибка: неверное расширение файла.')
elif not path.startswith('C'):
    print('Ошибка: выбран неверный диск.')
else:
    print(path)

#
# words_list = []
#
# for i_num in range(3):
#     print('Введите', i_num + 1, 'слово:', end=' ')
#     # word = input().lower()
#     word = input().upper()
#     words_list.append(word)
# # text = input('Введите текст: ').lower().split()
# text = input('Введите текст: ').upper().split()
#
# print('\nПодсчет слов в тексте')
# for index in range(3):
#     print(words_list[index], ':', text.count(words_list[index]))
