from abc import ABC, abstractmethod
class Transport(ABC):
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def sygnal(self):
        print('Бип-бип')

    def __str__(self):
        return f'Название: {self.name}, цвет: {self.color}, скорость: {self.speed}'

class Drive(Transport):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def drive(self):
        print('Машина едет')

class Seil(Transport):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def seil(self):
        print('Лодка плывет')

class PlayMusic(Transport):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def play_music(self):
        print('Музыка нааас связала, тайоною нааашей стала...')

class Car(Drive, PlayMusic):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


class Boat(Seil, PlayMusic):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


class Amphibie(Drive, Seil, PlayMusic):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


bmw = Car('Bmw', 'black', 200)
print(bmw)
bmw.drive(), bmw.sygnal(), bmw.play_music()
print()
beda = Boat('Беда', 'white', 20)
print(beda)
beda.seil(), beda.sygnal(), beda.play_music()
print()
amf = Amphibie('Русал', 'Черный', 10)
print(amf)
amf.drive(), amf.seil(), amf.sygnal(), amf.play_music()




