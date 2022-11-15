file_path = input('Введите путь к файлу: ')
disk_choose = input('Выберите диск: ')
file_format = input('Введите формат файла: ')
if file_path.startswith(disk_choose) == False:
    print('Ошибка диска')
elif file_path.endswith(file_format) == False:
    print('Ошибка расширения')
else:
    print('Путь корректен')
