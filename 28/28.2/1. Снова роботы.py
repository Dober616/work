class Robot:
    def __init__(self, name):
        self.__name = name

    def say(self):
        print(f'Я робот. Название {self.__name}.')

class CanFly(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.altitude = 0
        self.speed = 0

    def can_fly(self):
        print('Я могу летать!')

    def fly(self):
        self.altitude = 1000
        self.speed = 500
        print(f'Взлетаю, высота: {self.altitude}, скорость: {self.speed}')

    def ground(self):
        self.altitude = 0
        self.speed = 0
        print(f'Приземляюсь, высота:{self.altitude}, скорость: {self.speed}')


class Warrior(CanFly):
    def __init__(self, name):
        super().__init__(name)
        self.__weapon = 'Gatling Gun'

    def operate(self):
        print(f'Атакую противника с помощью {self.__weapon}')

class SpyDrone(CanFly):
    def __init__(self, name):
        super().__init__(name)

    def operate(self):
        print('Веду разведку с воздуха')


r2d2 = Warrior('R2D2')
r2d2.say()
r2d2.fly()
r2d2.operate()
r2d2.ground()
byrakhtar = SpyDrone('Байрахтар')
byrakhtar.say()
byrakhtar.fly()
byrakhtar.operate()
byrakhtar.ground()