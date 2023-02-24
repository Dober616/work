from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, color: str, speed: int):
        self.color = color
        self.speed = speed

    @abstractmethod
    def sygnal(self):
        pass

    @abstractmethod
    def music(self):
        pass

class Car(Transport):
    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)

    def ride(self):
        print('Еду по земле')

    def sygnal(self):
        print('Бип-бип')

    def music(self):
        print('Playing some melody')

class Boat(Transport):
    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)

    def swim(self):
        print('Плыву по воде')

    def sygnal(self):
        print('Бип-бип')

    def music(self):
        print('Playing some melody')

class Amphibie(Car, Boat):
    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)




my_car = Car('red', 200)
my_car.ride()
my_car.sygnal()
my_car.music()

ttt = Amphibie('Black', 10)
ttt.ride()
ttt.swim()
ttt.sygnal()