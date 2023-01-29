class Man:
    __count = 0
    def __init__(self, name, age=0):
        self.set_name(name)
        self.set_age(age)
        Man.__count += 1

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception('Недопустимый формат имени')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(0, 100):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст')

    def get_count(self):
        return self.__count
    def __str__(self):
        return f'Человека зовут: {self.__name}\n' \
               f'его возраст: {self.__age}'


kirill = Man('Кирилл', 33)
egor = Man('Егор')
maxim = Man('Максим', 2)
print(kirill)
print(egor)
print(maxim)
print(f'\nСчетчик: {egor.get_count()}')
print(egor.get_age())