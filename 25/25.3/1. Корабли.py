class Ship:
    def __init__(self, name, model):
        self.__name = name
        self.__model = model

    def move(self, point):
        self.point = point
        print(f'{self.__model} корабль {self.__name} плывет в {self.point}')


class Warship(Ship):
    def __init__(self, weapon, name, model):
        super().__init__(name, model)
        self.weapon = weapon

    def attack(self, target):
        self.target = target
        print(f'Боевой корабль атакует {self.target}\n'
              f'Поражает цель')

class Cargoship(Ship):
    def __init__(self, cargo, name, model):
        super().__init__(name, model)
        self.cargo = cargo

    def load(self, container, capacity):
        self.container = container
        self.capacity = 0
        print(f'Корабль загружает {self.container} контейнеров')
        self.capacity += self.container
        print(f'Текущая загруженность корабля {self.capacity}')

    def unload(self, container):
        self.container = container
        if self.capacity < self.container:
            print('Да нет на корабле столько груза')
        else:
            print(f'Корабль прибыл в точку назначения и разгружает {self.container} контейнеров')
            self.capacity -= self.container
            print(f'Текущая загруженность корабля {self.capacity}')



avrora = Warship('Пушка', 'Аврора', 'БЧ-2')
avrora.move('Измаил')
avrora.attack('Пентагон')

romashka = Cargoship('Бананны', 'Ромашка', 'Торговый')
romashka.load(10, 0)
romashka.move('Африка')
romashka.unload(3)
romashka.move('Калининград')