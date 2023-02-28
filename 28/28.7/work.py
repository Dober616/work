class Pet:
    TOTAL_SOUNDS = 0
    def __init__(self):
        self.__legs = 4
        self.__has_tail = True

    def __str__(self):
        tail = 'да' if self.__has_tail else 'нет'
        return f'Всего ног {self.__legs}. Наличие хвоста: {tail}'


class Cat(Pet):
    def __init__(self):
        super().__init__()

    @classmethod
    def sound(cls):
        cls.TOTAL_SOUNDS += 1
        print(cls.TOTAL_SOUNDS)
        print('Мяу')

class Dog(Pet):
    def __init__(self):
        super().__init__()

    @classmethod
    def sound(cls):
        cls.TOTAL_SOUNDS += 1
        print(cls.TOTAL_SOUNDS)
        print('Гав!')

Cat.sound()
Dog.sound()
Dog.sound()
