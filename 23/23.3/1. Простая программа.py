new_file = None
try:
    new_file = open('Fraze.txt', 'w')
    my_text = input('Введите какой-нибудь текст')
    number = int(input('Введите цифры'))
    new_file.write(my_text)
    new_file.write(str(number))
except (FileNotFoundError):
    print('Файл не найден')
except (PermissionError):
    print('Ошибка чего-то там еще')
except (TypeError):
    print('Ошибка данных')
else:
    print('Запись данных прошла без ошибок')
finally:
    if new_file and not new_file.closed:
        new_file.close()