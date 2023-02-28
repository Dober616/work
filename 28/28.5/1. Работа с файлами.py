class File:
    def __init__(self, file_name: str, mode: str):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print(f'Работа с файлом {self.file} завершена')
        return True

with File('www.txt', 'w') as f_1:
    f_1.write('Всем привет!')



