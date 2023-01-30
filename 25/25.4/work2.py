# class Person:
#     def __init__(self, name, age):
#         self.set_name(name)
#         self.set_age(age)
#
#     def __str__(self):
#         return 'Имя: {name}\nВозраст: {age}'.format(name=self.__name, age=self.__age)
#
#     def set_name(self, name):
#         if name.isalpha():
#             self.__name = name
#         else:
#             raise Exception('Недопустимый формат имени')
#
#     def get_name(self):
#         return self.__name
#
#     def set_age(self, age):
#         if age in range(0, 100):
#             self.__age = age
#         else:
#             raise Exception('Недопустимый возраст')
#     def get_age(self):
#         return self.__age
#
# class Student(Person):
#     def __init__(self, name, age, university):
#         super().__init__(name, age)
#         self.university = university
#
#     def __str__(self):
#         info = super.__str__(7)
#         info = info, f'\nУчится в {self.university}'
#         return info
#         # return f'Студенту {self.get_name()} {self.get_age()} лет, он учится в {self.university}'
#
#
#
#
#
# # class Worker(Person):
# #     def __init__(self, name, age, company, salary=120000):
# #         super().__init__(name, age)
# #         self.company = company
# #         self.salary = salary
# #
# #     def __str__(self):
# #         return f'{self.get_name()} {self.get_age()} лет, он работает в {self.company} и ' \
# #                f'получает зарплату {self.salary} рублей'
#
#
# # kirill = Worker('Кирилл', 38, 'Финтех')
# # print(kirill)
#
# egor = Student('Егор', 2, 'Детский сад')
# print(egor)

class Person:

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)


    def set_age(self, age):
        if age in range(0, 100):
            self.__age = age
        else:
            raise Exception('Недопустимый формат возраста')

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name
    def __str__(self):
        return f'Имя: {self.__name}\nВозраст: {self.__age}'

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def __str__(self):
        info = super().__str__()
        info = f'{info}\nСтудент учится в {self.university}'
        return info



class Worker(Person):
    def __init__(self, name, age, work_place, salary=120000):
        super().__init__(name, age)
        self.work_place = work_place
        self.selary = salary

    def __str__(self):
        info = super().__str__()
        info = f'{info}\nРаботник работает в {self.work_place}\nЗарплата: {self.selary}'
        return info




kirill = Student('Кирилл', 38, 'Skillbox')
egor = Worker('Егор', 22, 'Финтех')
print(kirill)
print()
print(egor)
