import os


# def print_dirs(some_project):
#     print(f'\nСодержание директории {some_project}')
#     if os.path.exists(some_project):
#         for element in os.listdir(some_project):
#             way = os.path.join(some_project, element)
#             print(f'        {way}')
#     else:
#         print('Такого каталога в проекте не существует')
#
#
# projects_list = ['work', 'dpo_python_basic', 'nothing_project']
# for project in projects_list:
#     way_to_project = os.path.abspath(os.path.join('..', '..', '..', project))
#     print_dirs(way_to_project)


def find_my_file(current_path, file_name):
    print(f'Переходим {current_path}')
    for element in os.listdir(current_path):
        path = os.path.join(current_path, element)
        print(f'    смотрим {path}')
        if file_name == element:
            return path
        if os.path.isdir(path):
            print('это директория')
            result = find_my_file(path, file_name)
            if result:
                break
    else:
        result=None
    return result

file_path = find_my_file(os.path.abspath(os.path.join('..', '..', '..', '..', 'pycharmprojects')), '1. Иконки.py')
if file_path:
    print(file_path)
else:
    print('Файл не найден')

