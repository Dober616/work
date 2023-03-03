from contextlib import contextmanager
from collections.abc import Iterator
@contextmanager
def next_num(num: int) -> Iterator[int]:
    print('Входим в функцию')
    try:
        yield num + 1
    except ZeroDivisionError as exc:
        print(f'Обнаружена ошибка {exc}')
    finally:
        print('Здесь код выполнится в любом случае')
    print('Выход из функции')
with next_num(-1) as next:
    print(f'Следующее число = {next}')
    print(10 / next)