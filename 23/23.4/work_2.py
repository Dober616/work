names_list = []

while True:
    try:
        name = input('Введите имя: ')
        if not name.isalpha():
            raise TypeError('Имя должно состоять из букв')
        names_list.append(name)
        if len(names_list) == 5:
            print('Место в списке закончилось')
            break
    except TypeError:
        print('Ты чего ввел?')

names_file = open('names.txt', 'w')
names_file.write('\n'.join(names_list))
names_file.close()
print('Программа закончена, запись завершена')