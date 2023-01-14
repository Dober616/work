names_list = []

while True:
    try:
        name = input('Введите имя: ')
        if name.lower() == 'error':
            raise BaseException('Ты сломал программу')
        if not name.isalpha():
            raise TypeError('Имя должно состоять из букв')
        names_list.append(name)
        if len(names_list) == 5:
            print('Место в списке закончилось')
            break
    except TypeError:
        print('Ты чего ввел?')
    except BaseException:
        names_list = []
        print('Введено стопслово')
        raise ValueError('Пожалуйста не вводите стоп-слово')

names_file = open('names.txt', 'w')
names_file.write('\n'.join(names_list))
names_file.close()
print('Программа закончена, запись завершена')