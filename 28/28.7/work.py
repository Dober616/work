class Pet:
    TOTAL_SOUNDS = 0
    def __init__(self):
        self.__legs = 4
        self.__has_tail = True

    def __str__(self):
        tail = 'да' if self.__has_tail else 'нет'
        return f'всего ног: {self.__legs}, наличие хвоста: {tail}'


class Cat(Pet):
    @classmethod
    def sound(cls):
        cls.TOTAL_SOUNDS += 1
        print(cls.TOTAL_SOUNDS)
        print('Meow')

class Dog(Pet):
    @classmethod
    def sound(cls):
        cls.TOTAL_SOUNDS += 1
        print(cls.TOTAL_SOUNDS)
        print('Гав-гав')

Cat.sound()
Cat.sound()
Dog.sound()