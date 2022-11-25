print('Текущие контакты в телефоне\n<Пусто>')
phone_book = dict()
while True:
    name = input('Введите имя абонента: ')
    if name == 'end':
        break
    elif name in phone_book:
        print('Имя {0} уже есть в справочнике'.format(name))
        break
    phone = input('Введите номер телефона: ')
    phone_book[name] = phone
for i in phone_book:
    print(i, '-', phone_book[i])
