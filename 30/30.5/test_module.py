def func():
    print(f'Я функция func() из test_module.py, и я что-то делаю')
if __name__ == '__main__':
    print('Здесь какой-то основной код')
    func()
else:
    print('Импортирван модуль', __name__)