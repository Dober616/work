class Robot:
    def __init__(self, name, type):
        self.__name = name
        self.__type = type


class CanFly(Robot):
    def __init__(self, name, type, height, speed):
        super().__init__(name, type)
        self.__name = name
        self.__type = type
        self.__height = height
        self.__speed = speed

    def take_off(self):
        self.__speed = 300
        self.__height = 100
        print(f'Взлетаю. Скорость: {self.__speed}, высота: {self.__height}')

    def fly(self):
        self.__speed = 1000
        self.__height = 3000
        print(f'Лечу. Скорость: {self.__speed}, высота: {self.__height}')

    def ground(self):
        self.__speed = 0
        self.__height = 0
        print(f'Приземлился. Скорость: {self.__speed}, высота: {self.__height}')


    def __str__(self):
        return f'Я {self.__name}, тип: {self.__type} и я могу летать!!!'

class SpyDrone(CanFly):
    def __init__(self, name, type):
        super().__init__(name, type, height=0, speed=0)

    def action(self):
        print('Разведка местности')

class CombatDrone(CanFly):
    def __init__(self, name, type):
        super().__init__(name, type, height=0, speed=0)
        self.weapon = 'Gatling Gun'

    def action(self):
        print(f'Атакую цель c {self.weapon}!!!')


some_robot = CombatDrone(name='R2d2', type='war robot')
print(some_robot)
some_robot.take_off(), some_robot.fly(), some_robot.action(), some_robot.ground()
print()
one_more_robot = SpyDrone(name='Agent 007', type='Spy')
print(one_more_robot)
one_more_robot.take_off(), one_more_robot.fly(), one_more_robot.action(), one_more_robot.ground()