phonebook = dict()
while True:
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    contact = (name, surname)
    if contact in phonebook:
        print('Такой контакт уже есть в справочнике')
    else:
        phone_number = input('Номер телефона: ')
        phonebook[contact] = phone_number
    print(phonebook)
