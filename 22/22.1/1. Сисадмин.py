import os

abs_path = os.path.abspath(os.path.join('..', '..', '..', 'admin.bat'))
simple_path = os.path.join('PycharmProjects', 'admin.bat')
print(simple_path)
print(abs_path)