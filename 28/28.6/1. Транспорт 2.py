class Transport:
    def __init__(self, name, color, speed, can_drive, can_swim):
        self._name = name
        self._color = color
        self._speed = speed
        self._can_drive = can_drive
        self._can_swim = can_swim

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f'Название: {self._name}, цвет: {self._color}, скорость: {self._speed}, {self._can_drive}, {self._can_swim}'

class Ground(Transport):
    def __init__(self, name, color, speed, can_drive=True, can_swim=False):
        super().__init__(name, color, speed, can_drive, can_swim)


class Water(Transport):
    def __init__(self, name, color, speed, can_drive=False, can_swim=True):
        super().__init__(name, color, speed, can_drive, can_swim)
class Auto(Ground):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

class Boat(Water):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

class Amphibie(Water, Ground):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


ttt = Amphibie('Neptun', 'red', 100)
print(ttt)
print(ttt.name)