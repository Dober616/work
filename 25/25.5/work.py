class Person:
    """
    Базовый класс, описывающий человека

    __ count: общее количество человека

    Args:
        name(str): передается имя человека
        age(int): передается возраст человека

    Atributes:
        max_count: передается максимальное количество инстансов
    """
    __count = 0
    max_count = 5

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        self.__location = 'Калининград'
        if Person.__count > self.max_count:
            raise Exception('Слишком много народу')
        Person.__count += 1

    def get_age(self):
        """
        Геттер для получения возраста

        :return: __age
        :rtype: int
        """
        return self.__age

    def set_age(self, age):
        """
        Сеттер для установления возраста

        :param age: возраст
        :type age: int
        :raise Exception: если возраст не в границах, то вызывается исключение
        """
        if age in range(18, 65):
            self.__age = age
        else:
            raise Exception('Ваш возраст нам не подходит')

class Employee(Person):
    """
    Класс Работник. Родитель: Person

    Args:
        name(str): передается имя человека
        age(int): передается возраст человека
    Atributes:
    max_count(int): максимальное количество инстансов
    job(str): должность работника

    """
    def __init__(self):
        super().__init__()
        self.job = 'Менеджер по продажам'

    def get_job(self):
        return self.job

    def employ(self, value):
        self.job = value
        if value is None:
            self.job = 'безработный'

print(Person.__doc__)
