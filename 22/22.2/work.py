import os


def find_file(current_way, my_file_name):
    print(f'Переходим в {current_way}')
    for element in os.listdir(current_way):
        way = os.path.join(current_way, element)
        print(f'Смотрим {way}')
        if my_file_name == element:
            return way
        if os.path.isdir(way):
            print('это директория')
            result = find_file(way, my_file_name)
            if result:
                break
    else:
        result = None
    return result

file_way = find_file(os.path.abspath(os.path.join('..', '..', '..', 'work')), 'admin.bat')
if file_way:
    print(f'Абсолютный путь к файлу: {file_way}')
else:
    print('Такого файла в структуре нет')
