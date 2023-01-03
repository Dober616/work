import os

# def print_dirs(project):
#     print('\nСодержимое директории', project)
#     if os.path.exists(project):
#         for element in os.listdir(project):
#             path = os.path.join(project, element)
#             print('       ', path)
#     else:
#         print(f'Каталога {project} в проекте не существует')
#
# projects_list = ['Repeat', 'work', 'dpo_python_basic']
# for some_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join('..', '..', '..', some_project))
#     print_dirs(path_to_project)

def find_file(current_path, my_file):
    print(f'Переходим  {current_path}')

    for element in os.listdir(current_path):
        path = os.path.join(current_path, element)
        print(f'      смотрим {path}')
        if my_file == element:
            return path
        if os.path.isdir(path):
            print(f'это директория')
            result = find_file(path, my_file)
            if result:
                break
    else:
        result = None

    return result


file_path = find_file(os.path.abspath(os.path.join('..', '..', '..', '..', 'PycharmProjects')), 'work.py')
if file_path:
    print(f'абсолютный путь к файлу {file_path}')
else:
    print('Путь к файлу не найден')