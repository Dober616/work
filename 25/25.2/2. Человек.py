class Men:
    __count = 0
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Men.__count += 1

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception('Недопустимый формат имени')

    def set_age(self, age):
        if isinstance(age, int) and age in range(1, 99):
            self.__age = age
        else:
            raise Exception('Недопустимый формат возраста')

    def get_info(self):
        return self.__name, self.__age

    def get_count(self):
        return Men.__count


egor = Men('Егор', 33)
max = Men('Макс', 11)
egor.set_age(44)
max.set_age(55)
print(egor.get_info())
print(max.get_info())
print(f'Количество объектов: {egor.get_count()}')
