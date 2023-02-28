from contextlib import contextmanager
import os

@contextmanager
def in_dir(path: str):
    current_path = os.getcwd()
    print(f'Текущая папка: {current_path}\n'
          f'Переключаю рабочую папку на {path}')
    try:
        yield
    finally:
        os.chdir(path)

with in_dir(''):
    print(os.listdir('//'))
