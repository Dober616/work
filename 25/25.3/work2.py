class Ship:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'\nМодель корабля: {self.model}'

    def sail(self, point):
        self.point = point
        print(f'Корабль {self.model} поплыл в {self.point}')

class Warship(Ship):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.__weapon = weapon

    def attack(self, target):
        self.target = target
        print(f'Боевой корабль атакует {self.target} с помощью {self.__weapon}')

class Cargo_ship(Ship):
    def __init__(self, model, cargo_weight=0):
        super().__init__(model)
        self.cargo_weight = cargo_weight

    def loading(self, cargo):
        self.cargo = cargo
        print(f'Корабль загружается грузом общим весом {self.cargo}')
        self.cargo_weight += self.cargo
        print(f'Вес груза на корабле {self.cargo_weight}')

    def unloading(self, weight):
        self.weight = weight
        self.cargo_weight -= self.weight
        print(f'Корабль разгружается. Остаток груза = {self.cargo_weight}')




avrora = Warship('Аврора', 'Пушка')
print(avrora)
avrora.sail('Сомали')
avrora.attack('Enemy')

print()
cruiser = Cargo_ship('Крузенштерн')
print(cruiser)
cruiser.loading(100)
cruiser.sail('Буркинафасо')
cruiser.unloading(77)


