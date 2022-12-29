import os
file_name = 'admin.bat'
simple_way = os.path.join('pycharmprojects', 'dpo_python_basic', file_name)
absolute_way = os.path.abspath(file_name)


print(simple_way)
print(absolute_way)