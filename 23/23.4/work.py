# sym_sum = 0
# line_count = 0
# try:
#     people_file = open('people.txt', 'r')
#     for line in people_file:
#         line_count += 1
#         lenght = len(line)
#         if line.endswith('\n'):
#             lenght -= 1
#         if lenght < 3:
#             raise BaseException(f'Длина {line_count} строки меньше трех символов')
#         sym_sum += lenght
#     people_file.close()
# except FileNotFoundError:
#     print('Такой файл не найден')
# finally:
#     print(f'Найденная сумма символов: {sym_sum}')p

names_list = []


while True:
    try:
        name = input('Введите имя: ')
        if name.lower() == 'error':
            raise BaseException('Ты сломал программу')
        if not name.isalpha():
            raise TypeError
        names_list.append(name)
        if len(names_list) == 5:
            print('Места закончились')
            break
    except TypeError:
        print('Ты чего ввел?')
    except BaseException:
        names_list = []
        print('Введено стоп-слово')
        raise ValueError('Пожалуйста не вводите больше эту хрень')

names_file = open('names.txt', 'w')
names_file.write('\n'.join(names_list))
names_file.close()
print('Программа завершена, запись закончена')