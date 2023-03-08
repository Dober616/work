class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, some_name):
        self._name = some_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, some_age):
        if 0 < some_age < 100:
            self._age = some_age
        else:
            raise Exception('Возраст не может быть таким')

    def __repr__(self):
        return f'{self.name}: {self.age}'


person_1 = Person('Tom', 101)
person_2 = Person('Bob', 55)
person_3 = Person('Sam', 44)

person_list = [person_1, person_2, person_3]
print(person_list)
human_sorted = sorted(person_list, key=lambda elem: elem.age)
print(human_sorted)
print(person_1.age)