import os

way_to = input('Путь к объекту: ')
if os.path.isdir(way_to):
    print('Объект является папкой')
elif os.path.isfile(way_to):
    print(f'Объект является файлом. Его размер {os.path.getsize(way_to)}')
else:
    print('Такого пути не существует')