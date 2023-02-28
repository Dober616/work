class Transport:
    def __init__(self, color, speed):
        self._color = color
        self._speed = speed

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if color == 'red' or color == 'green' or color == 'blue':
            self._color = color
        else:
            print('Такого цвета нет')

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed in range(1, 200):
            self._speed = speed
        else:
            print('Ну не может быть такой скорости')

    def __str__(self):
        return f'цвет: {self.color}; скорость: {self.speed}'

class CanDrive(Transport):
    def __init__(self, color, speed):
        super().__init__(color, speed)

    def drive(self):
        print('Едем по земле')

class CanSwim(Transport):
    def __init__(self, color, speed):
        super().__init__(color, speed)

    def swim(self):
        print('Плывем по воде')

class Car(CanDrive):
    def __init__(self, color, speed):
        super().__init__(color, speed)

class Boat(CanSwim):
    def __init__(self, color, speed):
        super().__init__(color, speed)

class Amfibie(CanSwim, CanDrive):
    def __init__(self, color, speed):
        super().__init__(color, speed)



ttt = Amfibie('red', 22)
print(ttt)
ttt.drive()
ttt.swim()