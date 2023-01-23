class Pet:
    legs = 4
    has_tail = True

    def __str__(self):
        tail = 'да' if self.has_tail else 'нет'
        return f'Всего ног: {self.legs}\nНаличие хвоста: {self.has_tail}'

    def voice(self):
        print('мяу')


class Cat(Pet):
    has_tail = True

    def voice(self):
        print('мяу')

class Dog(Pet):
    has_tail = False

    def voice(self):
        print('гав')

class Chicken(Pet):
    has_tail = False
    legs = 2

    def voice(self):
        print('ко-ко')


cat = Cat()
dog = Dog()
chicken = Chicken()
print(cat)
cat.voice()
print(dog)
dog.voice()
print(chicken)
chicken.voice()