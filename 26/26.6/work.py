from collections.abc import Iterable

class Person:
    def __init__(self, name: str, age: int, friends: list) -> None:
        self.__name = name
        self.set_age(age)
        self.__friends = friends

    def __str__(self) -> str:
        return f'Имя: {self.__name}, возраст: {self.__age}, друзья: {self.__friends} '

    def set_age(self, age) -> None:
        if 0 < age < 100:
            self.__age = age
        else:
            raise Exception('Неподходящий возраст')

    def get_age(self) -> int:
        return self.__age

tom = Person('Kirill', 25, ['bob', 'max'])
print(tom)

def fibonacci(numm: int) -> Iterable[int]:
    cur_val = 0
    next_val = 1
    for i in range(numm):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val
        if cur_val > 10 ** 6:
            return

for i in fibonacci(10):
    print(i)