class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def shout(self):
        print('Я личность')

class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._salary = 20000

    def get_salary(self):
        return self._salary

    # def shout(self):
    #     print('Я работник')

class Parent(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._kids = ['Tom', 'Bob']

    def get_kids(self):
        return self._kids

    # def shout(self):
    #     print('Я родитель')

class Citizen(Employee, Parent):
    pass


my_citizen = Citizen('Кирилл', 38)
print(my_citizen.get_salary(), my_citizen.get_kids())
my_citizen.shout()