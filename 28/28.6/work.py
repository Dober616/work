class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self._name}, {self._age}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 0 < age < 99:
            self._age = age


kirill = Person('Kirill', 22)
print(kirill)
print(kirill.age)
kirill._age = 36
print(kirill.age)
print(kirill.name)
print(kirill)