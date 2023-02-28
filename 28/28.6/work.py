class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f'Человека зовут {self._name}. Ему {self._age} лет'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self._age = age
        else:
            print('Возраст не подходит под критерии')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print('Имя не подходит под критерии')

me_person = Person('egor', 22)
print(me_person)
print(me_person.name)
print(me_person.age)
me_person.name = 'Кирилл'
me_person.age = 36
print(me_person.age)
print(me_person)
print(me_person.name)