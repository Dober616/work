class Person:
    __count = 0

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person.__count += 1

    def set_age(self, age):
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст')

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name


    def __str__(self):
        return f'\nИмя пользователя: {self.__name}\n' \
               f'его возраст: {self.__age}'

    def get_count(self):
        return self.__count

kirill = Person('Кирилл', 38)
kirill.set_age(89)
egor = Person('Егор', 2)


print(kirill, egor)
print(f'\nСчетчик равен: {kirill.get_count()}')


print(kirill.get_name())