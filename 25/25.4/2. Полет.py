# class CanFly:
#     height = 0
#     speed = 0
#
#     def takeoff(self):
#         pass
#
#     def fly(self):
#         pass
#
#     def ground(self, height=0):
#         self.height = height
#         print(f'Бабочка приземляется. Высота {self.height}\nскорость{self.speed}')
#
#     def __str__(self):
#         return f'Текущая высота: {self.height}\n{self.speed}'
#
# class Butterfly(CanFly):
#     def fly(self, height=1, speed=0.5):
#         self.height = height
#         self.speed = speed
#         print(f'Бабочка взлетает. Высота {self.height}\nСкорость: {self.speed}')
#
# class Rocket(CanFly):
#     def fly(self, height=500, speed=1000):
#         self.height = height
#         self.speed = speed
#
# butter = Butterfly()
# rock = Rocket()
# print(butter)
# butter.fly()
# print(butter)
# butter.ground()
# print(butter)

class CanFly:
    def __init__(self, name, height=0, speed=0):
        self.name = name
        self.height = height
        self.speed = speed

    def take_off(self):
        print(f'{self.name} взлетает')

    def fly(self):
        print(f'{self.name} летит')

    def ground(self):
        print(f'{self.name} приземлился')

    def __str__(self):
        return f'Летит {self.name}. Текущая высота: {self.height}, текущая скорость: {self.speed}'


class Butterfly(CanFly):
    def __init__(self, name, height=0, speed=0, can_hight=1, can_speed=0.5):
        super().__init__(name, height, speed)
        self.can_hight = can_hight
        self.can_speed = can_speed




class Rocket(CanFly):
    def __init__(self, name, height=0, speed=0, can_hight=500, can_speed=1000):
        super().__init__(name, height, speed)
        self.can_hight = can_hight
        self.can_speed = can_speed


butter = Butterfly('Елена')
butter.take_off()
butter.fly()
print(butter)
butter.ground()
print(butter)
