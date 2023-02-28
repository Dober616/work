from contextlib import contextmanager

@contextmanager
def next_num(num):
    yield num + 1

with next_num(-1) as next:
    print('Входим в функцию')
    try:
        print(f'Следующее число {next}')
        print(10 / next)
    except ZeroDivisionError as exc:
        print(f'Обранужена ошибка {exc}')
    finally:
        print('Здесь код выполнится в любом случае')
    print('Выход из функции')
