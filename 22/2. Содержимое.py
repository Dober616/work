import os

def dir_content(dir):
    print(f'Содержимое папки {dir}: ')
    for i in os.listdir(dir):
        folder_path = os.path.join(dir, i)
        print(folder_path)



dir_name = 'pycharmprojects'  #input('Имя папки: ')

print(dir_content(dir_name))

path_to_project = os.path.abspath(os.path.join('..', '..', dir_name))
print(path_to_project)