import os
file_name = 'admin.bat'
some_path = os.path.join('pycharm_projects', 'work', file_name)
abs_path = os.path.abspath(file_name)

print(f'Относительный путь до файла: {some_path}')
print(f'Абсолютный путь к файлу: {abs_path}')
