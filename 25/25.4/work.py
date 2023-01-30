class Pet():
    legs = 4
    has_tail = True

    def __str__(self):
        tail = 'да' if self.has_tail == True else 'нет'
        return f'Всего ног: {self.legs}\n' \
               f'Наличие хвоста: {tail}'

    def walk(self):
        print('Гуляет')

class Cat(Pet):
    type = 'Кот'

    def sound(self):
        print('Мяу')

class Dog(Pet):
    type = 'Пес'

    def sound(self):
        print('Гав')

class Frog(Pet):
    legs = 2
    type = 'Лягушка'
    has_tail = False

    def sound(self):
        print('Ква')

    def walk(self):
        print('Плавает')

cat = Cat()
dog = Dog()
frog = Frog()
print(cat.type)
print(cat)
cat.sound()
cat.walk()
print(dog.type)
print(dog)
dog.sound()
dog.walk()
print(frog.type)
print(frog)
print(frog.sound())
frog.walk()
