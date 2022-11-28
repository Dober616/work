# phonebook = {
#     'Ваня': 123456,
#     'Петя': 123457,
#     'Коля': 123458
# }
# name = input('Введите имя: ')
# print(phonebook)
# if name in phonebook:
#     print(name, '-', phonebook[name])
# else:
#     print('Ошибка. Человек с именем {0} не найден'.format(name))

# example = dict()
# while True:
#     name = input('Введите имя: ')
#     phone = input('Введите номер телефона: ')
#     example[name] = phone
#     print(example)

# student = dict()
# student_info = input('Введите данные ученика\n(Фамилия, Имя, Город, ВУЗ, оценки): ')
# student_data = student_info.split()
# student['Имя'] = student_data[0]
# student['Фамилия'] = student_data[1]
# student['город'] = student_data[2]
# student['ВУЗ'] = student_data[3]
# student['Оценки'] = []
# for mark in student_data[4:]:
#     student['Оценки'].append(mark)
# print(student)


