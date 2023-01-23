class Robot:
    def __init__(self, model_numm):
        self.__model_numm = model_numm

class Cleaner(Robot):
    def __init__(self, model_numm, bag, bag_capacity):
        super().__init__(model_numm)
        self.bag = 10
        self.bag_capacity = 0

    def clean(self):
        if self.bag_capacity == self.bag:
            print('Мешок для мусора полный, сначала вытряхните')
        else:
            print(f'Текущая заполненность мешка {self.bag_capacity}\n'
                  f'Начинаю убираться')
            while self.bag_capacity != self.bag:
                self.bag_capacity += 1
                print(f'Убрал 1 мусор, текущая загруженность {self.bag_capacity}')
            print('Мешок опять полный, вытряхните')

class Wariior(Robot):
    def __init__(self, model_numm, weapon, bullets):
        super().__init__(model_numm)
        self.__weapon = weapon
        self.bullets = 10

    def attack(self, target):
        self.target = target
        if self.bullets == 0:
            print(f'Да нечем нам атаковать, пуль осталось {self.bullets}')
        else:
            while self.bullets != 0:
                self.bullets -= 1
                print(f'Атакую {self.target}, осталось {self.bullets} патронов')
            print('патроны закончились, возвращаюсь на базу')

class Submarine(Wariior):
    def __init__(self, model_numm, weapon, bullets):
        super().__init__(model_numm, weapon, bullets)


    def water(self, depth):
        self.depth = depth
        print(f'Погружаюсь на глубину {self.depth}')





xiaomi = Cleaner('Ксяоми', 10, 0)
xiaomi.clean()
r2d2 = Wariior('R2D2', 'minigun', 10)
r2d2.attack('враг')
sub = Submarine('b52', 10, 0)
sub.water(10)
sub.attack('Враг')