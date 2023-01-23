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



    def __str__(self):
        return f'Имя: {self.__name}\tвозраст: {self.__age}'

    def get_count(self):
        return self.__count


misha = Person('Миша', 25)
pasha = Person('Паша', 23)
roma = Person('Рома', 80)
print(misha)
print(pasha)
print(roma)
print(misha.get_count())
new_age = 80
misha.age = new_age
print(misha)
misha.set_age(new_age)
print(misha.get_age())
